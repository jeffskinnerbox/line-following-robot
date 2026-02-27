# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.


## Project Overview

This is a **Claude Code skill-based course development system** for a volunteer makerspace instructor building documentation for a Line Following Robot (LFR) course at Makersmiths. The audience is mixed-age students (12–18 + adults/parents) with basic coding experience but no hardware background.

The course progresses through ~11 design sessions: from a simple IR-based LFR on a Raspberry Pi Pico W running CircuitPython, through PID control, Kalman filtering, and culminating in Q-Learning or Fuzzy Logic controllers. See `my-vision.md` for the full course vision.


## Key Documents

| File | Purpose |
|:-----|:--------|
| `my-vision.md` | Instructor's full course vision — primary source of intent |
| `specification.md` | Detailed project spec generated from vision; primary reference for all doc generation |
| `development-plan.md` | Living build tracker — phases, deliverables, decisions, open questions; read this + `specification.md` at the start of every session |
| `my-claude-prompts.md` | Prompts used to generate each major artifact; resume session IDs are here |
| `Q-NNN-resolution.md` | Hardware/design research notes resolving a specific open question (e.g. `Q-001-resolution.md`) |

These files form the source-of-truth chain: vision → spec → course documents. `development-plan.md` is the session-to-session working context.


## New Session Startup

1. Read `development-plan.md` — check **Current Phase** header and **Document Status** section for immediate context
2. Read `specification.md` — for hardware, firmware, and tool specs
3. Act on any **Open Questions** listed in `development-plan.md` before starting new work


## Git Workflow

Single `main` branch; no feature branches. Tag `main` at each phase milestone:

```bash
git tag phase1-foundation-complete
git tag phase2-bangbang-sim-complete
git tag phase3-designer-reflectance-complete
git tag phase4-wifi-openloop-pid-complete
git tag phase5-kalman-qlearn-complete
git tag phase6-course-ready
```

Tag pattern: `phase{N}-{name}-complete`. Tags are created only after all phase deliverables and tests are complete (see `development-plan.md`).


## Commands

### Python Environment

All Python commands require the project virtualenv:

```bash
source .venv/bin/activate
```

### Lint Markdown

```bash
markdownlint-cli2 "*.md"                  # lint all markdown files
markdownlint-cli2 "path/to/file.md"       # lint a specific file
```

The `.markdownlint-cli2.jsonc` config enables auto-fix, allows 300-char lines, and disables rules MD012, MD022, MD024, MD032, MD033, MD041, MD045.

### Run Tests

```bash
pytest tests/unit/                        # Tier 1: unit tests (fast, no hardware)
pytest tests/sim/                         # Tier 2: simulator tests (headless pygame)
pytest                                    # all tests
pytest --cov=firmware --cov=simulator     # with coverage
```

For headless simulator tests, set `SDL_VIDEODRIVER=dummy` if not already in `pytest.ini`:

```bash
SDL_VIDEODRIVER=dummy pytest tests/sim/
```


## Architecture

### Skill System (`.claude/skills/`)
Skills are auto-invoked instruction sets loaded when Claude detects a matching task. Each skill lives in its own subfolder with `SKILL.md` as the main instruction file. See `.claude/skills/README.md` for the full system design.

**Project-local skills** (`.claude/skills/`):

| Skill | Purpose |
|:------|:--------|
| `syllabus-generator` | Course-level roadmap: topics, schedule, objectives |
| `lesson-plan-generator` | Per-session teaching guides for the instructor |
| `bill-of-materials-generator` | All costs, quantities, and sourcing — the single source of truth |
| `theory-of-operation` | Internal mechanics of systems/components |
| `history-and-application` | Origins and real-world applications of technology |
| `explainer` | Plain-language breakdowns of complex concepts |

**Global skills** (`~/.claude/skills/`): `code-doc-writer`, `code-reviewer`, `project-doc-writer`, `skill-generator`, `test-generator`

### Status Markers (used in `development-plan.md`)

```text
[ ]  Pending — not yet started
[~]  In Progress — actively being worked
[x]  Done — complete and tested
```

### Custom Slash Commands (`.claude/commands/`)
- `/create-plan [spec-file]` → reads spec file if provided; outputs `plan-[project-name].md`
- `/create-syllabus` → outputs `syllabus-[course-name].md`
- `/create-lesson-plan` → outputs `lesson-plan-[topic].md`

Skills may include a `references/` subdirectory for large content offloaded from `SKILL.md`.

### Component Build Layers (from `development-plan.md` §4)

Modules must be built in dependency order. Never start a module before its layer's dependencies exist:

```text
Layer 0  config.py, firmware/hal/base.py (ABCs only)
Layer 1  pico_hal.py, sim_hal.py, simulator/physics.py, simulator/track.py
Layer 2  firmware/sensors/ir_sensor.py, simulator/sensor_sim.py
Layer 3  firmware/controllers/bang_bang.py, simulator/visualization.py
Layer 4  simulator/ui.py, simulator/plugin.py, simulator/main.py
Layer 5  track_designer/ (all modules)
Layer 6  firmware/sensors/reflectance_array.py, firmware/wifi/web_server.py
Layer 7  speed_sensor.py, open_loop.py, pid.py
Layer 8  simulator/metrics.py, firmware/controllers/kalman.py
Layer 9  firmware/controllers/q_learning.py
```

A module may import only from layers below it — circular imports are a design error.


## Critical Rules

### Document Consistency
The three core course documents must stay in perfect sync — component names, phase structure, and materials must match exactly across all three:

| Document | Contains | Never Contains |
|:---------|:---------|:---------------|
| Syllabus | What, when, objectives, schedule | Costs, pricing, purchase links |
| Lesson Plans | How to teach, timing, troubleshooting | Costs, pricing, purchase links |
| BOM | All costs, quantities, sourcing, shipping | None — it IS the source of truth |

When updating any course document, check the other two for consistency.

### Markdown Formatting
- Use **reference-style links** (e.g., `[text][ref-id]` with `[ref-id]: url` at the bottom), not inline URLs
- HR dividers use `---------------` (15 dashes)
- List indentation: 4 spaces

### CircuitPython Dual-Runtime Constraint

Firmware modules (`firmware/`) run on **both** the Pico W (CircuitPython 9.x) and the desktop simulator (Python 3.12). When writing firmware code:

- No `typing` module imports — use string literals for forward refs or bare hints in comments
- No `dataclasses`, `threading`, or walrus operator (`:=`)
- `abc.ABC` / `abc.abstractmethod` are safe — they exist in CircuitPython 9.x
- f-strings are safe (CircuitPython 7+)
- All `import` statements must be at the top of each file (CircuitPython loader limitation)

### SKILL.md Files
- Keep under ~500 lines; offload large content to `references/` subdirectory
- YAML frontmatter `description` field is the primary activation trigger — make it descriptive
- Audience is Claude, not developers — no README-style onboarding prose


## Terminology (from `.claude/skills/shared/definitions.md`)
- **Course**: Full series of 2-hour classes on a specific subject
- **Class / Design Session**: Single 2-hour period; ~11 sessions in this course
- **Syllabus**: Course-level blueprint
- **Lesson Plan**: Instructor's step-by-step guide for one Design Session
- **BOM**: Bill of Materials — single source of truth for all costs/sourcing
- **Makersmiths**: The makerspace hosting the course
