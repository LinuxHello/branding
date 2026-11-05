#!/usr/bin/env python3
"""Generate the Linux Hello logo variants from the master SVG.

The master (logo/linuxhello-logo.svg) is a colour-layer trace of
the original raster logo: one background rect and six stacked paths, each path
the union of its own colour and every colour drawn above it (order: navy,
shadow, mist, white, orange, ember). Every variant here is
the same paths, cropped, clipped or recoloured. Nothing is redrawn, so all
variants stay geometrically identical to the master.

Usage:
  scripts/brand-assets.py            # write SVG variants and PNG exports
  scripts/brand-assets.py --no-png   # SVG variants only
  scripts/brand-assets.py --check    # exit 1 if any committed SVG variant is stale

PNG export needs rsvg-convert (Debian/Ubuntu package librsvg2-bin).
Standard library only.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOGO_DIR = ROOT / "logo"
MASTER = LOGO_DIR / "linuxhello-logo.svg"
PNG_DIR = LOGO_DIR / "png"

# Geometry measured on the master trace (2048 x 2048 user units).
MARK = (686, 512, 1361, 1233)     # penguin bounding box: x0, y0, x1, y1
WORD = (374, 1340, 1673, 1534)    # wordmark bounding box
CAP = (1349, 1533)                # cap height of "H": top, baseline
SPLIT_Y = 1270                    # horizontal line between penguin and wordmark
PAD = 4                           # anti-alias margin on tight artboards

BLUE = "#248de0"
NAVY = "#1f2e45"
WHITE = "#ffffff"

PATH_RE = re.compile(r'<path fill="(#[0-9a-fA-F]{6})" transform="([^"]+)" d="([^"]+)"\s*/>', re.S)


def load_layers(master: Path) -> list[tuple[str, str, str]]:
    layers = PATH_RE.findall(master.read_text(encoding="utf-8"))
    if len(layers) != 6 or sum(f.lower() == WHITE for f, _, _ in layers) != 1:
        sys.exit(f"error: expected 6 colour layers, one of them white, in {master}")
    return layers


def paths(layers, fill: str | None = None, only_white: bool = False) -> str:
    # In the wordmark region every layer that contains white has the same
    # shape, so the white layer alone is the wordmark.
    chosen = [layer for layer in layers if layer[0].lower() == WHITE] if only_white else layers
    return "\n".join(
        f'    <path fill="{fill or f}" transform="{t}" d="{d}"/>' for f, t, d in chosen
    )


def svg(title: str, vb: tuple[float, float, float, float], body: str, size: tuple[int, int] | None = None) -> str:
    x, y, w, h = vb
    dims = f' width="{size[0]}" height="{size[1]}"' if size else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x:g} {y:g} {w:g} {h:g}"{dims} role="img">\n'
        f"  <title>{title}</title>\n{body}\n</svg>\n"
    )


CLIPS = (
    "  <defs>\n"
    f'    <clipPath id="lh-mark"><rect x="0" y="0" width="2048" height="{SPLIT_Y}"/></clipPath>\n'
    f'    <clipPath id="lh-word"><rect x="0" y="{SPLIT_Y}" width="2048" height="{2048 - SPLIT_Y}"/></clipPath>\n'
    "  </defs>\n"
)


def mark_group(layers) -> str:
    return f'  <g clip-path="url(#lh-mark)">\n{paths(layers)}\n  </g>'


def word_group(layers, fill: str) -> str:
    return f'  <g clip-path="url(#lh-word)">\n{paths(layers, fill=fill, only_white=True)}\n  </g>'


def tight(box) -> tuple[float, float, float, float]:
    x0, y0, x1, y1 = box
    return (x0 - PAD, y0 - PAD, x1 - x0 + 2 * PAD, y1 - y0 + 2 * PAD)


def horizontal(layers, word_fill: str) -> tuple[tuple[float, float, float, float], str]:
    """Mark left, wordmark right; wordmark cap height = 40 % of mark height."""
    mw, mh = MARK[2] - MARK[0], MARK[3] - MARK[1]
    cap = CAP[1] - CAP[0]
    s = round(0.40 * mh / cap, 4)
    gap = round(0.18 * mh)
    ww = (WORD[2] - WORD[0]) * s
    cx = (CAP[0] + CAP[1]) / 2
    body = (
        CLIPS
        + f'  <g transform="translate({-MARK[0]} {-MARK[1]})">\n{mark_group(layers)}\n  </g>\n'
        + f'  <g transform="translate({mw + gap} {mh / 2:g}) scale({s}) translate({-WORD[0]} {-cx:g})">\n'
        + word_group(layers, word_fill)
        + "\n  </g>"
    )
    width = mw + gap + ww
    return (-PAD, -PAD, round(width + 2 * PAD, 1), mh + 2 * PAD), body


def build(layers) -> dict[str, str]:
    out: dict[str, str] = {}
    bg = f'  <rect x="-4096" y="-4096" width="12288" height="12288" fill="{BLUE}"/>\n'

    # Square tile: penguin on blue, penguin height = 72 % of the side.
    side = round((MARK[3] - MARK[1]) / 0.72)
    cx, cy = (MARK[0] + MARK[2]) / 2, (MARK[1] + MARK[3]) / 2
    out["linuxhello-tile.svg"] = svg(
        "Linux Hello", (cx - side / 2, cy - side / 2, side, side), CLIPS + bg + mark_group(layers)
    )
    out["linuxhello-mark.svg"] = svg("Linux Hello", tight(MARK), CLIPS + mark_group(layers))
    out["linuxhello-wordmark-white.svg"] = svg("LinuxHello", tight(WORD), CLIPS + word_group(layers, WHITE))
    out["linuxhello-wordmark-navy.svg"] = svg("LinuxHello", tight(WORD), CLIPS + word_group(layers, NAVY))

    st = (min(MARK[0], WORD[0]), MARK[1], max(MARK[2], WORD[2]), WORD[3])
    out["linuxhello-stacked-navy.svg"] = svg(
        "Linux Hello", tight(st), CLIPS + mark_group(layers) + "\n" + word_group(layers, NAVY)
    )
    out["linuxhello-stacked-white.svg"] = svg(
        "Linux Hello", tight(st), CLIPS + mark_group(layers) + "\n" + word_group(layers, WHITE)
    )
    for name, fill in (("navy", NAVY), ("white", WHITE)):
        vb, body = horizontal(layers, fill)
        out[f"linuxhello-horizontal-{name}.svg"] = svg("Linux Hello", vb, body)

    # GitHub social preview, 1280 x 640 (2:1): horizontal lockup on blue,
    # lockup width 70 % of the card.
    vb, body = horizontal(layers, WHITE)
    lw, lh = vb[2], vb[3]
    cw = lw / 0.70
    ch = cw / 2
    out["linuxhello-social-preview.svg"] = svg(
        "Linux Hello",
        (vb[0] - (cw - lw) / 2, vb[1] - (ch - lh) / 2, round(cw, 1), round(ch, 1)),
        bg + body,
        size=(1280, 640),
    )
    return out


PNGS = [
    # (source svg, output png, width, height)
    ("linuxhello-logo.svg", "linuxhello-logo-1024.png", 1024, 1024),
    ("linuxhello-tile.svg", "linuxhello-tile-1024.png", 1024, 1024),
    ("linuxhello-tile.svg", "linuxhello-tile-512.png", 512, 512),
    ("linuxhello-tile.svg", "linuxhello-tile-180.png", 180, 180),
    ("linuxhello-tile.svg", "linuxhello-tile-64.png", 64, 64),
    ("linuxhello-tile.svg", "linuxhello-tile-32.png", 32, 32),
    ("linuxhello-mark.svg", "linuxhello-mark-512.png", None, 512),
    ("linuxhello-horizontal-navy.svg", "linuxhello-horizontal-navy-1200.png", 1200, None),
    ("linuxhello-horizontal-white.svg", "linuxhello-horizontal-white-1200.png", 1200, None),
    ("linuxhello-social-preview.svg", "linuxhello-social-preview-1280x640.png", 1280, 640),
]


def export_png() -> None:
    rsvg = shutil.which("rsvg-convert")
    if not rsvg:
        sys.exit("error: rsvg-convert not found (sudo apt install librsvg2-bin), or use --no-png")
    PNG_DIR.mkdir(exist_ok=True)
    for src, dst, w, h in PNGS:
        cmd = [rsvg, "--format=png", "-o", str(PNG_DIR / dst)]
        if w:
            cmd += ["-w", str(w)]
        if h:
            cmd += ["-h", str(h)]
        if w and h:
            cmd += ["--keep-aspect-ratio"]
        subprocess.run(cmd + [str(LOGO_DIR / src)], check=True)
        print(f"wrote {PNG_DIR.relative_to(ROOT) / dst}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--no-png", action="store_true", help="skip PNG export")
    ap.add_argument("--check", action="store_true", help="fail if committed SVG variants are stale")
    a = ap.parse_args()

    if not MASTER.is_file():
        sys.exit(f"error: master logo not found: {MASTER}")
    variants = build(load_layers(MASTER))

    if a.check:
        stale = [n for n, s in variants.items()
                 if not (LOGO_DIR / n).is_file() or (LOGO_DIR / n).read_text(encoding="utf-8") != s]
        if stale:
            sys.exit("stale or missing: " + ", ".join(stale) + " (run scripts/brand-assets.py)")
        print("brand assets up to date")
        return

    for name, text in variants.items():
        (LOGO_DIR / name).write_text(text, encoding="utf-8")
        print(f"wrote {(LOGO_DIR / name).relative_to(ROOT)}")
    if not a.no_png:
        export_png()


if __name__ == "__main__":
    main()
