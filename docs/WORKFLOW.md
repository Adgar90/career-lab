# Career Lab Workflow

## Purpose

This document defines how learning sessions, progress tracking and level transitions work inside Career Lab.

It is the operational reference for the system.

---

# 1. Sources of truth

Each file has one primary responsibility.

## `README.md`

Defines what Career Lab is and its general philosophy.

## `AGENTS.md`

Defines permanent behavioural rules for AI assistants.

## `context/profile.md`

Provides stable learner context.

## `CURRENT_LEVEL.md`

Defines the active learning scope.

This is the source of truth for:

- current stage;
- current micro-objective;
- completion criteria;
- scope exclusions.

## `specs/`

Defines what should be built or exercised to support learning.

## `PROGRESS.md`

Records meaningful learning evidence and unresolved gaps.

It is not a daily diary.

## `evals/`

Defines checkpoints used to evaluate learning.

## `prompts/`

Contains reusable session-specific prompts.

---

# 2. Session startup

A normal learning session should begin by reading:

1. `AGENTS.md`
2. `CURRENT_LEVEL.md`

Then read only the additional context needed for the session.

Possible additional files:

- `context/profile.md`
- the relevant file in `specs/`
- relevant previous entries in `PROGRESS.md`
- the relevant mentor prompt in `prompts/`

Avoid loading the entire repository without a reason.

---

# 3. Select one question

Each session should have one primary learning question.

Examples:

- What happens when this request reaches my application?
- What process is actually running?
- Why can this request not reach the service?
- What happens if PostgreSQL disappears?

If the session contains several unrelated learning goals, reduce the scope.

---

# 4. Establish the initial mental model

Before receiving a full explanation, the learner should state what they currently believe.

Possible formats:

- short written explanation;
- diagram;
- prediction;
- list of steps;
- hypothesis.

This provides a baseline and makes misconceptions visible.

---

# 5. Investigate

Prefer direct investigation whenever reasonable.

Possible evidence sources:

- source code;
- application behaviour;
- command output;
- logs;
- HTTP requests;
- process information;
- containers;
- database state;
- official documentation;
- small experiments.

AI should support investigation rather than replace it.

---

# 6. AI mentoring loop

The default loop is:

```text
Question
  ->
Learner hypothesis
  ->
Experiment
  ->
Evidence
  ->
Learner explanation
  ->
Mentor feedback
```

If the learner is blocked, assistance should increase gradually:

1. question;
2. small hint;
3. stronger hint;
4. conceptual explanation;
5. complete solution only when explicitly requested.

---

# 7. Scope management

During a session, new topics will appear.

Classify them as:

## NOW

Required to answer the current learning question.

Investigate now.

## LATER

Relevant but not required for the current objective.

Record briefly if useful, then return to the current question.

## NOISE

Interesting but currently unrelated.

Do not add it to the roadmap.

The existence of a concept does not create a learning obligation.

---

# 8. Evidence creation

A meaningful learning session should ideally produce at least one evidence item.

Examples:

- learner-created diagram;
- independent explanation;
- successful experiment;
- failure diagnosis;
- prediction confirmed or disproved;
- commit implementing learner-written work;
- comparison between alternatives.

Evidence should show understanding, not only activity.

---

# 9. Progress proposal

At the end of a meaningful session, AI may propose an update for `PROGRESS.md`.

The proposal should separate:

### Demonstrated

What the learner actually showed.

### Gap detected

What remains unclear or incorrect.

### Evidence

What supports the claim.

### Next action

The smallest useful continuation.

Do not inflate progress.

---

# 10. Human validation

The learner reviews the proposed progress update.

Only the learner can approve:

- writing the permanent progress entry;
- changing a micro-objective status;
- marking evidence checkboxes;
- declaring a checkpoint complete.

AI can recommend changes but cannot approve them autonomously.

---

# 11. Updating `PROGRESS.md`

After human approval:

1. add the relevant session or milestone entry;
2. update evidence checkboxes only when demonstrated;
3. update status if appropriate;
4. record remaining open questions.

Avoid recording low-value details merely because they occurred.

---

# 12. Micro-objective completion

A micro-objective should normally demonstrate three dimensions:

## Understand

The learner can explain the concept in their own words.

## Apply

The learner can use the concept in the project.

## Diagnose

The learner can investigate a simple failure or unexpected behaviour related to the concept.

Not every concept requires equal depth, but completion should not rely only on memorization.

---

# 13. Stage checkpoint

When all micro-objectives are sufficiently developed:

1. use the corresponding file in `evals/`;
2. evaluate using project evidence;
3. record gaps;
4. complete the final reflection;
5. decide stage status with human approval.

The checkpoint should test connected understanding, not isolated vocabulary.

---

# 14. Designing the next stage

Only after the current stage checkpoint:

1. review demonstrated strengths;
2. review remaining gaps;
3. review new questions discovered through practice;
4. consider current professional needs;
5. design the smallest useful next stage.

Do not automatically continue the original roadmap.

The next stage may differ from earlier assumptions.

---

# 15. Document lifecycle

## Stable documents

Change infrequently:

- `README.md`
- `AGENTS.md`
- `context/profile.md`
- `docs/WORKFLOW.md`

## Iterative documents

Change as learning evolves:

- `CURRENT_LEVEL.md`
- `PROGRESS.md`

## Stage-bound documents

Usually created per stage:

- `specs/stage-X.Y-project.md`
- `evals/stage-X.Y-checkpoint.md`

## Reusable prompts

Change when the interaction method improves:

- `prompts/mentor.md`

---

# 16. When to modify the system itself

Do not improve the Career Lab infrastructure merely because an improvement is possible.

Modify the environment when a real friction appears.

Examples of justified improvements:

- repeated manual progress formatting;
- difficulty finding current context;
- repeated agent behaviour mistakes;
- need to compare checkpoint history;
- need to automate a proven repetitive task.

Avoid speculative infrastructure.

---

# 17. AI-first evolution

Future AI-first capabilities may include:

- automatic context selection;
- progress proposals based on session history;
- evidence indexing;
- checkpoint preparation;
- structured evaluations;
- prompt/version tracking;
- agent tools;
- automated environment checks.

These should be added incrementally.

The same rule applies:

> Introduce infrastructure to solve observed friction, not anticipated complexity.

---

# 18. Session close checklist

Before ending a meaningful session:

- [ ] Did I answer one concrete learning question?
- [ ] Can I explain the result in my own words?
- [ ] Did I generate evidence?
- [ ] Did I identify any incorrect assumption?
- [ ] Is there one clear next action?
- [ ] Does `PROGRESS.md` need an update?
- [ ] Did I stay inside the current scope?

If the answer to most of these is yes, the session was productive.
