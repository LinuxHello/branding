---
type: note
subject: Linux Hello logo, variants, construction and usage rules
artifact: brand-guide
status: draft
owner: "@atterdag"
concepts: [branding, logo]
tags: [branding, logo]
sources: ["logo/linuxhello-logo.svg", "scripts/brand-assets.py"]
date: 2026-11-03
---

# Logo

The logo has two parts: the **mark** (the waving penguin) and the **wordmark** ("LinuxHello", with "Linux" in a regular weight and "Hello" in bold). The wordmark is artwork, not typed text: always use the files, never retype it in a font (see [typography.md](typography.md#the-wordmark-is-not-a-font)).

## Variants

All files are in [logo/](logo/); PNG exports in [logo/png/](logo/png/).

| File | Content | Background | Use |
| :-- | :-- | :-- | :-- |
| `linuxhello-logo.svg` | Stacked: mark over wordmark, white text | Brand blue, square, generous margin (master) | README header, title slides, posters |
| `linuxhello-tile.svg` | Mark only, penguin height 72 % of the side | Brand blue, square | Avatars, app icon, favicon, any dark or busy background |
| `linuxhello-mark.svg` | Mark only, tight artboard | Transparent | Light backgrounds only |
| `linuxhello-stacked-navy.svg` | Stacked, navy text | Transparent | Light backgrounds |
| `linuxhello-stacked-white.svg` | Stacked, white text | Transparent | Brand-blue backgrounds only |
| `linuxhello-horizontal-navy.svg` | Mark left, wordmark right, navy text | Transparent | Page headers and footers on light backgrounds |
| `linuxhello-horizontal-white.svg` | Same, white text | Transparent | Brand-blue bands only |
| `linuxhello-wordmark-navy.svg` | Wordmark only, navy | Transparent | Where the mark is already shown nearby |
| `linuxhello-wordmark-white.svg` | Wordmark only, white | Transparent | Brand blue, Navy or Shadow backgrounds |
| `linuxhello-social-preview.svg` | Horizontal lockup, white text, 1280 × 640 | Brand blue | Repository social preview |

PNG exports: tile at 1024, 512, 180, 64 and 32 px; master at 1024 px; mark at 512 px high; horizontal lockups at 1200 px wide; social preview at 1280 × 640.

## Construction

- **Stacked lockup (master):** the wordmark is centred under the mark; the wordmark is 1.92 × the mark's width.
- **Horizontal lockup:** the wordmark's cap height (the height of the "H") is 40 % of the mark's height; the gap between mark and wordmark is 18 % of the mark's height; the wordmark is centred vertically on the mark.
- **Tile:** the penguin is centred, its height 72 % of the side, so it survives the rounded or circular crops that GitHub, chat apps and launchers apply.

## Clear space

Keep other elements outside the clear space.

| Variant | Clear space on every side |
| :-- | :-- |
| Lockups and wordmark | **x** = the cap height of the "H" in the wordmark as placed |
| Mark alone | a quarter of the mark's height |
| Tile | none beyond its own edge; the margin is built in |

## Minimum sizes

| Variant | Minimum | Reason |
| :-- | :-- | :-- |
| Tile | 16 px (checked legible at 32 px) | The penguin's silhouette and beak still read |
| Mark | 24 px high | Below this the eyes merge with the face |
| Stacked lockup | 120 px wide | The wordmark's cap height drops below 17 px |
| Horizontal lockup | 160 px wide | The wordmark's cap height drops below 16 px |

Below the lockup minimums, use the tile and set the name in text next to it.

## Backgrounds

The penguin's body is navy, so the transparent mark needs a light background. Use these combinations only.

| Background | Allowed variants |
| :-- | :-- |
| White, Mist, light neutral | mark, `*-navy` |
| Hello Blue `#248DE0` | `linuxhello-logo`, tile, `*-white` |
| Navy, Shadow, any dark surface, dark mode | tile, `linuxhello-wordmark-white` |
| Photos, gradients, patterns | tile only |

On a dark surface the transparent mark's body disappears and leaves floating eyes and a belly. This is the most common mistake; use the tile.

## Do not

- Retype the wordmark, change its weights or swap the weight split ("Linux" regular, "Hello" bold).
- Recolour the penguin, or use colours outside the [palette](colour.md).
- Remove the split light (lit left half, shaded right half); it is part of the mark.
- Add outlines, strokes, drop shadows, glows, gradients or 3D effects.
- Stretch, skew, rotate or mirror the logo. The penguin waves with its left wing (viewer's right).
- Crop the penguin or place text inside the clear space.
- Put the white-text variants on anything other than brand blue (or the white wordmark on Navy or Shadow).
- Animate the logo without a maintainer-approved design.
- Call the penguin Tux, or combine it with Tux or other projects' logos in a way that suggests endorsement.
