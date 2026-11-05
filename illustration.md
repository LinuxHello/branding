---
type: note
subject: Linux Hello illustration and icon style
artifact: brand-guide
status: draft
owner: "@atterdag"
concepts: [branding, illustration]
tags: [branding, illustration]
sources: ["logo/linuxhello-logo.svg", "colour.md"]
date: 2026-11-03
---

# Illustration and icons

New artwork (spot illustrations, diagrams with characters, stickers, empty states) follows the logo's construction, so it looks like it belongs with the penguin.

## Style rules

1. **Flat vector.** Filled shapes only: no gradients, outlines, strokes, textures, drop shadows or blur.
2. **Split light.** Light comes from the viewer's left. Every rounded form is split by one vertical line through its centre: the left half in the lit tone, the right half in the shaded tone. Lit/shaded pairs:

   | Lit | Shaded |
   | :-- | :-- |
   | `navy` `#263A53` | `shadow` `#1F2E45` |
   | `white` `#FFFFFF` | `mist` `#E5E9ED` |
   | `orange` `#F8982A` | `orange` (small parts are not split) |

3. **Palette only.** The seven logo colours ([colour.md](colour.md)). `ember` only for openings and insides (the beak's mouth).
4. **Soft geometry.** Built from circles, ellipses and rounded rectangles; corners always rounded; no sharp points except the beak.
5. **Eyes.** A round navy pupil with a white catchlight in its upper right.
6. **Friendly, not cute.** One expression (calm, mildly cheerful). No tears, anger, winks or hearts. The penguin never appears injured, caged or defeated, including in error states.
7. **Background.** Hello Blue or white. Artwork on photos or gradients goes on a tile.

## The penguin as a character

- Proportions come from [linuxhello-mark.svg](logo/linuxhello-mark.svg): head and body one continuous shape, belly an egg shape, feet two orange ovals.
- New poses keep the head, eyes, beak and belly unchanged; only wings and feet move.
- Props are allowed and drawn in the same style: a key, a fingerprint, a shield, a laptop. Use them to explain, not to promise: no padlock-plus-checkmark "secure" badges (see the rule against unfalsifiable superlatives in [linux-hello's AGENTS.md](https://github.com/LinuxHello/linux-hello/blob/main/AGENTS.md#documentation-docs)).
- The penguin has no official name yet. Do not call it Tux.

## Icons

- **Product UI icons** come from the desktop's icon theme (Breeze in Plasma), not from this style.
- **Marketing and documentation icons**: 24 × 24 grid, 2 px corner radius, filled, one colour (`navy` on light, `white` on blue or dark), split light only at 48 px and above.

## Diagrams

Architecture diagrams stay in Mermaid and Structurizr DSL with their default themes; see [applications.md](applications.md#diagrams) for when to apply brand colours.
