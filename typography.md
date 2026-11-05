---
type: note
subject: Linux Hello typefaces, weights and type scale
artifact: brand-guide
status: draft
owner: "@atterdag"
concepts: [branding, typography]
tags: [branding, typography]
sources: ["https://fonts.google.com/specimen/Quicksand", "https://fonts.google.com/noto/specimen/Noto+Sans", "https://openfontlicense.org/"]
date: 2026-11-03
---

# Typography

## Typefaces

| Role | Typeface | Weights | Licence | Use |
| :-- | :-- | :-- | :-- | :-- |
| Display | **Quicksand** | 500, 600, 700 | SIL OFL 1.1 | Headlines, titles, slide headings, social cards, short labels at 20 px and above |
| Text | **Noto Sans** | 400, 600, 700 | SIL OFL 1.1 | Body text, tables, captions, UI copy outside the desktop |
| Code | **Noto Sans Mono** | 400, 700 | SIL OFL 1.1 | Code, commands, D-Bus names, file paths |

All three are free under the SIL Open Font License and available from Google Fonts; Noto Sans and Noto Sans Mono are also in the Ubuntu packages `fonts-noto-core` and `fonts-noto-mono`. Whether Quicksand is packaged for Ubuntu is unverified; take it from Google Fonts otherwise. Do not commit font files to this repository; reference them.

Fallback stacks (also in [tokens/tokens.css](tokens/tokens.css)):

```css
--lh-font-display: "Quicksand", "Nunito", "Varela Round", system-ui, sans-serif;
--lh-font-text: "Noto Sans", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
--lh-font-code: "Noto Sans Mono", "Hack", ui-monospace, "DejaVu Sans Mono", monospace;
```

## The wordmark is not a font

The "LinuxHello" wordmark is traced artwork, not text set in an existing typeface. Fifteen rounded and geometric candidates were rendered and compared with the traced wordmark by pixel overlap (intersection over union):

| Typeface | "Linux" best overlap | "Hello" best overlap |
| :-- | :-- | :-- |
| Quicksand | 0.84 (500) | 0.83 (700) |
| Rubik | 0.81 (400) | 0.84 (600) |
| Varela Round | 0.83 (400) | 0.66 (400, only weight) |
| Lexend | 0.69 (300) | 0.89 (600) |
| Nunito | 0.81 (500) | 0.76 (800) |

No single family matches both words above 0.9, and the best match differs per word, so the wordmark is treated as a drawing. Quicksand is the display face because it fits the whole wordmark best and shares its rounded stroke ends. "Hello" in the wordmark is heavier than Quicksand's heaviest weight (700). The comparison is reproducible: render each candidate with the fonts from the `@fontsource` npm packages, crop to the word, scale to the wordmark's bounding box and compute overlap.

Consequences:

- Never retype "LinuxHello" in Quicksand as a substitute for the logo files.
- When the name is set in text, write **Linux Hello** (two words) in the running typeface. Do not imitate the wordmark's regular/bold split in text.

## Type scale

For web pages, slides and printed material. Sizes are in px at 1×; line height is unitless.

| Level | Typeface | Weight | Size | Line height | Letter spacing |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Display | Quicksand | 700 | 48 | 1.1 | −0.01 em |
| H1 | Quicksand | 700 | 36 | 1.15 | −0.01 em |
| H2 | Quicksand | 600 | 28 | 1.2 | 0 |
| H3 | Quicksand | 600 | 22 | 1.25 | 0 |
| Body | Noto Sans | 400 | 16 | 1.5 | 0 |
| Small | Noto Sans | 400 | 14 | 1.45 | 0 |
| Caption, table | Noto Sans | 400 | 13 | 1.4 | 0 |
| Code | Noto Sans Mono | 400 | 14 | 1.5 | 0 |

For slides, multiply by 1.5 to 2 and keep body text at 24 px or more.

## Rules

- Quicksand below 20 px looks thin; use Noto Sans for anything smaller.
- Sentence case for headings and buttons ("Set up a PIN", not "Set Up A PIN").
- Use weight, not colour, to show hierarchy; text colours come from [colour.md](colour.md#surfaces).
- Inside the Plasma desktop, Linux Hello uses the system font, not these typefaces (see [applications.md](applications.md#plasma-and-application-icons)).
