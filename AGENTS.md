# AGENTS.md

Rules for coding agents in this repository. The rules of [linux-hello's AGENTS.md](https://github.com/LinuxHello/linux-hello/blob/main/AGENTS.md) apply here where they fit (roles, invariants 5 to 9, commits and pull requests, communication); this file adds what is specific to the brand repository.

- Follow [CONTRIBUTING.md](CONTRIBUTING.md): DCO sign-off by the human who submits, `Assisted-by:` trailers, no secrets or machine details.
- Never hand-edit generated logo files. Change the master or `scripts/brand-assets.py`, regenerate, and run `scripts/brand-assets.py --check` before calling a change done; quote its output.
- Colour values live in `tokens/tokens.json`; keep `tokens/tokens.css`, [colour.md](colour.md) and `swatches/` in step with it.
- Do not decide the logo's licence or use policy, the penguin's name, or application IDs; those need an ADR in linux-hello.
