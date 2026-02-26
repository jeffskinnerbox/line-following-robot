# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.


## Project Overview

This is a **Claude Code skill-based course development system** for a volunteer makerspace instructor building documentation for a Line Following Robot (LFR) course at Makersmiths. The audience is mixed-age students (12–18 + adults/parents) with basic coding experience but no hardware background.

The course progresses through ~11 design sessions: from a simple IR-based LFR on a Raspberry Pi Pico W running CircuitPython, through PID control, Kalman filtering, and culminating in Q-Learning or Fuzzy Logic controllers. See `my-vision.md` for the full course vision.


## Commands

### Lint Markdown

```bash
markdownlint-cli2 "*.md"                  # lint all markdown files
markdownlint-cli2 "path/to/file.md"       # lint a specific file
```

The `.markdownlint-cli2.jsonc` config enables auto-fix, allows 300-char lines, and disables rules MD012, MD022, MD024, MD032, MD033, MD041, MD045.


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

### Custom Slash Commands (`.claude/commands/`)
- `/create-plan` → outputs `plan-[project-name].md`
- `/create-syllabus` → outputs `syllabus-[course-name].md`
- `/create-lesson-plan` → outputs `lesson-plan-[topic].md`


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
