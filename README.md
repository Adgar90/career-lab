# Career Lab

Career Lab is a personal environment for iterative technical learning and
professional development.

Its purpose is to build Software Engineering understanding through small,
practical learning projects.

The goal is not to accumulate courses, technologies or large roadmaps.

The goal is to understand enough to take the next useful step, produce evidence,
and reassess from there.

---

## Philosophy

Career Lab is based on a few principles:

- learn from concrete technical questions;
- use small projects as learning vehicles;
- understand fundamentals before focusing on tools;
- prefer evidence over content consumption;
- keep the active scope small;
- evolve the roadmap iteratively.

When a concept appears, the learning process can go one layer deeper, understand
what is needed, then return to the original problem.

---

## Learning model

Learning is organized as:

```text
Global direction
    |
    +-- Current stage
          |
          +-- Micro-objective
          +-- Micro-objective
          +-- Checkpoint
```

Only the current stage is defined in detail.

Future stages are designed after reviewing evidence from the current one.

---

## Current state

The active learning scope is defined in `CURRENT_LEVEL.md`.

Aggregate progress is tracked in `PROGRESS.md`.

Detailed session history belongs in `progress/sessions/`.

---

## Repository structure

```text
career-lab/
+-- app/                  Practical learning project
+-- context/              Stable learner context
+-- docs/                 Human workflow and operational notes
+-- evals/                Checkpoints and evaluations
+-- progress/sessions/    Compact approved session snapshots
+-- prompts/              Reusable session prompts
+-- scripts/              Optional small utilities
+-- specs/                Project and exercise specifications
+-- AGENTS.md             Permanent AI rules and context router
+-- CURRENT_LEVEL.md      Active learning scope
+-- PROGRESS.md           Compact aggregate progress state
+-- README.md
```

---

## AI usage

AI is part of Career Lab as a mentor, instructor and reviewer.

By default, AI should help the learner reason independently rather than act as
the default implementer.

Permanent agent rules and context routing are defined in `AGENTS.md`.

---

## Operating workflow

The detailed human workflow is documented in `docs/WORKFLOW.md`.

Normal technical learning sessions do not need to load every repository document.
Context should be loaded progressively, according to the task.

---

## Main principle

> Do not try to learn everything needed for the final destination.
>
> Learn only what is needed to climb the next step.
