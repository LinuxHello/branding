---
type: note
subject: Applying the Linux Hello brand to GitHub, documents, the desktop, diagrams and slides
artifact: brand-guide
status: draft
owner: "@atterdag"
concepts: [branding]
tags: [branding]
sources: ["logo.md", "colour.md", "typography.md"]
date: 2026-11-03
---

# Applications

## GitHub

| Place | File | Notes |
| :-- | :-- | :-- |
| Organisation avatar | [png/linuxhello-tile-1024.png](logo/png/linuxhello-tile-1024.png) | Upload limit 1 MB; GitHub crops to a rounded square |
| Repository social preview | [png/linuxhello-social-preview-1280x640.png](logo/png/linuxhello-social-preview-1280x640.png) | Repository settings, General, Social preview |
| README header | [linuxhello-logo.svg](logo/linuxhello-logo.svg) at `width="240"`, centred | Used by [linux-hello's README](https://github.com/LinuxHello/linux-hello/blob/main/README.md) |

The README header uses the blue master because it reads the same in GitHub's light and dark modes. A transparent variant would lose either its navy body (dark mode) or its white text (light mode).

## Web pages and documents

- Load [tokens/tokens.css](tokens/tokens.css); it defines the palette, the surfaces for light and dark mode and the font stacks.
- Page header: `linuxhello-horizontal-navy.svg` on the light surface, `linuxhello-horizontal-white.svg` on a Hello Blue band. In dark mode switch the header to a blue band rather than placing a transparent logo on Shadow.
- Favicon: [linuxhello-tile.svg](logo/linuxhello-tile.svg), with [png/linuxhello-tile-32.png](logo/png/linuxhello-tile-32.png) as a fallback and [png/linuxhello-tile-180.png](logo/png/linuxhello-tile-180.png) as the Apple touch icon.

```html
<link rel="icon" href="linuxhello-tile.svg" type="image/svg+xml">
<link rel="icon" href="linuxhello-tile-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="linuxhello-tile-180.png">
```

## Plasma and application icons

Linux Hello's own UI (prompts, greeter and lock-screen integration, enrolment, settings) follows the user's desktop, not the brand:

- **Colours and fonts** come from the active Plasma colour scheme and system font (Kirigami theme properties in QML). Do not hard-code brand colours or brand typefaces in the UI. Users choose their scheme for reasons such as high contrast or colour blindness, and an authentication prompt that ignores the system theme looks like a foreign window, which is the wrong signal on a prompt that asks for a PIN.
- **Status colours** (error, warning, success) come from the colour scheme, never from the brand palette.
- **The brand appears** in the About page, the first page of enrolment, and the application icon.
- **Application icon:** until a Breeze-style icon is drawn, use [linuxhello-tile.svg](logo/linuxhello-tile.svg), installed to `hicolor/scalable/apps/` and named after the application ID (`io.github.LinuxHello.*`; the exact IDs are a naming decision for an ADR). The transparent mark is not used as an icon because its navy body disappears on dark panels.

## Diagrams

- **In the linux-hello docs vault** (Mermaid and Structurizr): keep the default themes. GitHub and Obsidian switch them for dark mode; a forced brand theme would put navy text on a dark page.
- **Exported for slides or print**, use the brand theme:

```text
%%{init: {"theme": "base", "themeVariables": {
  "fontFamily": "Noto Sans, sans-serif",
  "primaryColor": "#E5E9ED", "primaryTextColor": "#1F2E45", "primaryBorderColor": "#263A53",
  "secondaryColor": "#FFFFFF", "tertiaryColor": "#FFFFFF",
  "lineColor": "#263A53", "textColor": "#1F2E45",
  "clusterBkg": "#FFFFFF", "clusterBorder": "#248DE0"
}}}%%
```

Structurizr styles for the same purpose: elements `background #E5E9ED`, `color #1F2E45`, `stroke #263A53`; the software system in focus `background #248DE0`, `color #FFFFFF`.

## Slides

- **Title slide:** Hello Blue background, [linuxhello-stacked-white.svg](logo/linuxhello-stacked-white.svg) or the master, title in Quicksand 700 white.
- **Content slides:** white background, `linuxhello-horizontal-navy.svg` small in a bottom corner (at least 160 px wide), headings Quicksand 600 in Shadow, body Noto Sans 24 px or larger.
- **Section dividers:** Navy or Shadow background, white Quicksand heading, no logo, or the tile.
- **Accent:** orange for one highlight per slide at most, on Navy or Shadow only.

## Stickers, print and merchandise

- Use the tile or the master (the blue field holds the navy penguin on any surface).
- Print colours are not specified yet. Convert from the hex values and proof before a print run.

## Writing about the project

- **Linux Hello** in prose, **LinuxHello** only in the wordmark and in identifiers such as the GitHub organisation and `io.github.LinuxHello.*`.
- Not "LH", "Linux-Hello" or "linuxhello" in prose.
- Describe what it does, plainly; no unfalsifiable superlatives ("bulletproof", "fully secure").
