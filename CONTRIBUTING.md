# Contributing

This repository follows the conventions of [linux-hello](https://github.com/LinuxHello/linux-hello/blob/main/CONTRIBUTING.md).

## Developer Certificate of Origin

Every commit must be signed off (`git commit -s`), certifying the [DCO](https://developercertificate.org/). The human who submits a commit signs it off and is accountable for it; an agent never signs off for anyone else.

## Changing the brand

- Branch from `main` and open a pull request; it is squash merged. Never push to `main`.
- The master logo, `logo/linuxhello-logo.svg`, is the only hand-supplied logo file. Do not edit the other files in `logo/`: change `scripts/brand-assets.py` or the master and regenerate.

  ```sh
  scripts/brand-assets.py           # regenerate SVG variants and PNG exports (needs rsvg-convert: apt install librsvg2-bin)
  scripts/brand-assets.py --check   # exit 1 if a committed SVG variant is stale; run before every pull request
  ```

- Keep `tokens/tokens.json` and `tokens/tokens.css` in step; a colour change also updates [colour.md](colour.md), its swatches and its contrast figures.
- Licence, naming and use-policy changes are one-way doors: they need an ADR in linux-hello first.

## AI-assisted contributions

Name the tool behind a substantial part of a change with an `Assisted-by:` trailer, one per tool:

```text
Assisted-by: Claude Code (<model>)
Assisted-by: GitHub Copilot
```

Name a local model by family and size at most, never by host or endpoint.

## Public repository

Never write secrets, tokens, personal data, or details of anyone's machines (hostnames, home paths, hardware, local endpoints) into files, commit messages or pull requests.

## Writing

Plain, direct prose. Describe what something does; no unfalsifiable superlatives ("bulletproof", "fully secure").

## Licence

By contributing you agree that your contribution is licensed under LGPL-3.0-or-later.
