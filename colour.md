---
type: note
subject: Linux Hello colour palette, roles and contrast
artifact: brand-guide
status: draft
owner: "@atterdag"
concepts: [branding, colour, accessibility]
tags: [branding, colour]
sources: ["logo/linuxhello-logo.svg", "tokens/tokens.json", "https://www.w3.org/TR/WCAG22/#contrast-minimum"]
date: 2026-11-03
---

# Colour

## Logo palette

These seven colours are the logo. They were measured from the original raster logo (median of each colour cluster) and are the only colours in the logo files.

| Swatch | Token | Hex | RGB | In the logo | Role |
| :-- | :-- | :-- | :-- | :-- | :-- |
| ![#248DE0](swatches/248de0.svg) | `blue` (Hello Blue) | `#248DE0` | 36 141 224 | Background | Primary brand field |
| ![#263A53](swatches/263a53.svg) | `navy` | `#263A53` | 38 58 83 | Body, lit half | Ink, dark surface |
| ![#1F2E45](swatches/1f2e45.svg) | `shadow` | `#1F2E45` | 31 46 69 | Body, shaded half | Ink, darkest surface |
| ![#FFFFFF](swatches/ffffff.svg) | `white` | `#FFFFFF` | 255 255 255 | Belly and face, lit half; text | Light surface, text on blue |
| ![#E5E9ED](swatches/e5e9ed.svg) | `mist` | `#E5E9ED` | 229 233 237 | Belly and face, shaded half | Secondary light surface |
| ![#F8982A](swatches/f8982a.svg) | `orange` (Beak Orange) | `#F8982A` | 248 152 42 | Beak, feet | Accent |
| ![#E46030](swatches/e46030.svg) | `ember` | `#E46030` | 228 96 48 | Inside of the beak | Illustration only |


## Derived colours

Hello Blue is too light for text on white (3.52:1). These shades keep its hue (HSL) and reach the WCAG 2.2 thresholds.

| Token | Hex | Contrast | Use |
| :-- | :-- | :-- | :-- |
| ![#1C7AC5](swatches/1c7ac5.svg) `blue-600` | `#1C7AC5` | 4.53:1 on white; white text on it 4.53:1 | Links and buttons on light surfaces; filled buttons with white text |
| ![#155C95](swatches/155c95.svg) `blue-800` | `#155C95` | 7.01:1 on white | Body-size blue text where AAA is wanted |
| ![#85C0EE](swatches/85c0ee.svg) `blue-300` | `#85C0EE` | 7.02:1 on Shadow | Links and highlights on dark surfaces |

## Contrast matrix

WCAG 2.2 contrast ratios between the logo colours. Thresholds: **4.5** for body text (AA), **3** for large text (24 px, or 18.66 px bold) and for icons and UI parts.

|  | blue | navy | shadow | orange | ember | mist | white |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| **blue** | — | 3.29 | 3.88 | 1.60 | 1.01 | 2.89 | 3.52 |
| **navy** | 3.29 | — | 1.18 | 5.25 | 3.32 | 9.49 | 11.59 |
| **shadow** | 3.88 | 1.18 | — | 6.20 | 3.92 | 11.21 | 13.68 |
| **orange** | 1.60 | 5.25 | 6.20 | — | 1.58 | 1.81 | 2.21 |
| **ember** | 1.01 | 3.32 | 3.92 | 1.58 | — | 2.86 | 3.49 |
| **mist** | 2.89 | 9.49 | 11.21 | 1.81 | 2.86 | — | 1.22 |
| **white** | 3.52 | 11.59 | 13.68 | 2.21 | 3.49 | 1.22 | — |

What follows from it:

- **White on Hello Blue** (3.52) is for large text, headlines and the logo only. For body text on blue use `blue-600` as the field.
- **Navy or Shadow on white or Mist** (9.5 to 13.7) is the default text pairing.
- **Orange is never text on light or blue surfaces** (2.21 on white, 1.60 on blue). On Navy or Shadow it passes as text (5.25 and 6.20).
- **Ember never carries meaning**; it is a shading colour inside illustrations.
- **Navy against Hello Blue** (3.29) is enough for icons and UI parts, not for body text.

## Surfaces

| Surface | Background | Text | Secondary text | Link | Accent |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Light | `white` | `shadow` | `navy` | `blue-600` | `blue` (large areas), `orange` (small marks next to navy) |
| Light, alternate | `mist` | `shadow` | `navy` | `blue-600` | as above |
| Brand | `blue` | `white` (large only) | — | `white`, underlined | `shadow` |
| Dark | `shadow` | `white` | `mist` | `blue-300` | `orange` |
| Dark, raised | `navy` | `white` | `mist` | `blue-300` | `orange` |

Proportion on any branded piece: about 60 % blue or the neutral surface, 30 % navy and white, 10 % or less orange.

## Status colours

Brand colours do not signal status. Product UI uses the desktop's own colours for errors, warnings and success (see [applications.md](applications.md#plasma-and-application-icons)). Never use orange to mean "warning" in Linux Hello material: it is the beak, not a signal.
