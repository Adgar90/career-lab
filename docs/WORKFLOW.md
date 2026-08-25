# Career Lab Workflow

## Purpose

This document describes the human and operational process for Career Lab.

This document is not required during normal technical learning sessions.

Agents should use `AGENTS.md` for context routing and load this document only
when the workflow itself is relevant.

---

# 1. Sources of truth

Each file has one primary responsibility.

## `README.md`

Describes what Career Lab is, its philosophy and its repository structure.

## `AGENTS.md`

Defines permanent agent behaviour and routes context to specialized documents.

## `CURRENT_LEVEL.md`

Defines the active learning scope.

It is the source of truth for:

- current stage;
- current micro-objective;
- objectives;
- minimum concepts;
- expected evidence;
- completion criteria;
- scope exclusions.

## `context/profile.md`

Provides stable learner context.

Use it only when personal or professional context affects a decision.

## `specs/`

Contains project or exercise specifications.

Use only the relevant specification for the current task.

## `PROGRESS.md`

Maintains compact aggregate learning state.

It is not the detailed session history.

## `progress/sessions/`

Contains compact session snapshots approved at session close.

## `evals/`

Contains checkpoint and evaluation material.

## `prompts/`

Contains reusable session prompts.

---

# 2. Session startup

A normal session starts from the minimum context needed.

The agent should:

1. use already-known context from the current conversation;
2. read `CURRENT_LEVEL.md` only if the active focus is unknown, stale or changed;
3. read the most recent relevant snapshot in `progress/sessions/` when continuing
   the same micro-objective across sessions;
4. read any other document only when routed by `AGENTS.md`.

Do not load all Markdown files by default.

Do not inspect the repository root or full directories merely to rediscover
documented context.

---

# 3. Select one question

Each learning session should have one primary question.

Examples:

- What happens when this request reaches my application?
- What process is actually running?
- Why can this request not reach the service?
- What happens if PostgreSQL disappears?

If a session contains several unrelated learning goals, reduce the scope.

---

# 4. Establish the starting point

Before receiving a full explanation, the learner should state what they
currently believe when that information is not already known.

Useful forms:

- short written explanation;
- diagram;
- prediction;
- list of steps;
- hypothesis.

Do not ask for the same starting point again if the learner already provided it
in the current session, unless the goal is retention or reformulation after
feedback.

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

During a session, classify new topics as:

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

A meaningful session should ideally produce at least one evidence item.

Examples:

- learner-created diagram;
- independent explanation;
- successful experiment;
- failure diagnosis;
- prediction confirmed or disproved;
- learner-written implementation;
- comparison between alternatives.

Evidence should show understanding, not only activity.

---

# 9. Session closure

When the learner wants to close a session, the agent proposes a closure before
writing any progress files.

The proposal should include:

- snapshot path;
- state changes, if any;
- evidence to validate, if any;
- open gaps;
- one next action.

Example:

```text
Closure proposal

Snapshot:
progress/sessions/YYYY-MM-DD-topic.md

Proposed changes:
- 1.1.1: NOT STARTED -> IN PROGRESS
- evidence X: validated
- evidence Y: pending

Next:
[one action]

Do you approve this closure?
```

The learner may approve, correct or reject any proposed change.

---

# 10. Session snapshots

After closure approval, create one compact snapshot under
`progress/sessions/`.

Use the naming convention:

```text
YYYY-MM-DD-topic.md
```

Recommended format:

```md
# Session - YYYY-MM-DD - [Topic]

## Focus
Micro-objective worked on.

## Starting point
Initial mental model or starting situation.

## Work done
What was investigated, discussed or tested.

## Key learning
What changed or became clearer.

## Evidence
What the learner demonstrated.

## Open gaps
What remains unclear.

## Agreed status changes
Only changes explicitly approved by the learner.

## Next
One next action.
```

Snapshots should be compact.

They are not conversation transcripts.

---

# 11. Updating `PROGRESS.md`

After human approval:

1. update aggregate status only when approved;
2. mark evidence as validated only when approved;
3. reference the latest relevant session snapshot;
4. record one agreed next action.

Avoid recording low-value details merely because they occurred.

Allowed micro-objective states:

- `NOT STARTED`;
- `IN PROGRESS`;
- `COMPLETE`.

Evidence checkboxes mean:

- `[ ]` pending;
- `[x]` validated.

Do not use percentages or complex scoring systems.

---

# 12. Checkpoints

Use the relevant file in `evals/` only for:

- checkpoints;
- formal evidence review;
- completion decisions;
- stage transitions.

The checkpoint should test connected understanding, not isolated vocabulary.

The final decision requires human approval.

AI may recommend a status but must not approve completion autonomously.

---

# 13. Transitioning to the next stage

Only after the current stage checkpoint:

1. review demonstrated strengths;
2. review remaining gaps;
3. review new questions discovered through practice;
4. consider current professional needs when relevant;
5. design the smallest useful next stage.

Do not automatically continue the original roadmap.

The next stage may differ from earlier assumptions.

---

# 14. When to modify the system

Do not improve Career Lab infrastructure merely because an improvement is
possible.

Modify the environment when real friction appears.

Examples of justified improvements:

- repeated manual progress formatting;
- difficulty finding current context;
- repeated agent behaviour mistakes;
- need to compare checkpoint history;
- need to automate a proven repetitive task.

Avoid speculative infrastructure.

Future AI-first capabilities may include automation, indexing or specialized
tools, but they should be introduced only when they solve observed friction.
