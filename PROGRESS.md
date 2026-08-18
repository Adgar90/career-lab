# Learning Progress

This document records meaningful learning progress.

It is not a daily diary.

Only record information that helps demonstrate:

- what I understood;
- what I misunderstood;
- what I discovered;
- what evidence I created;
- what questions remain open.

---

# Current stage

**Stage 1.1 — Understand an application end-to-end**

Current micro-objective:

**1.1.1 — Request lifecycle**

---

# Progress template

Use the following structure for each meaningful learning session or milestone.

---

## YYYY-MM-DD — [Topic]

### Question

What question was I trying to answer?

### Initial mental model

What did I believe before investigating?

Write this before asking AI for the full explanation whenever possible.

### Investigation

What did I inspect or test?

Examples:

- documentation;
- logs;
- source code;
- experiments;
- debugger;
- network request;
- database;
- container.

### What I learned

Explain the concept using my own words.

Avoid copying documentation or AI responses.

### Incorrect assumptions

What did I believe that turned out to be incorrect?

Why was it incorrect?

### Evidence

What demonstrates that I understood or applied the concept?

Examples:

- diagram;
- working experiment;
- explanation;
- commit;
- debugging result;
- comparison;
- technical decision.

### Open questions

What do I still not understand?

Only record questions that are relevant to the current level.

### Next action

What is the smallest useful next step?

---

# Checkpoints

## 1.1.1 — Request lifecycle

Status: NOT STARTED

Evidence:

- [ ] I can draw the request lifecycle.
- [ ] I can explain every major step.
- [ ] I can follow one request through my application.
- [ ] I can explain the response that is returned.

Notes:

---

## 1.1.2 — Runtime and execution

Status: NOT STARTED

Evidence:

- [ ] I can explain what process runs my application.
- [ ] I understand the role of the runtime.
- [ ] I understand ports at a basic level.
- [ ] I can explain image vs container.
- [ ] I can run the application outside my IDE.

Notes:

---

## 1.1.3 — Configuration

Status: NOT STARTED

Evidence:

- [ ] I understand configuration vs application code.
- [ ] I can use environment variables.
- [ ] I understand why secrets should not live in source code.
- [ ] I can configure the application for another environment.

Notes:

---

## 1.1.4 — Persistence

Status: NOT STARTED

Evidence:

- [ ] The application persists real data.
- [ ] I understand the basic application/database relationship.
- [ ] I can explain what happens when the database is unavailable.

Notes:

---

## 1.1.5 — Basic observability

Status: NOT STARTED

Evidence:

- [ ] The application generates useful logs.
- [ ] I can correlate a failure with log information.
- [ ] I can investigate one intentional failure without using the debugger.
- [ ] I understand the conceptual difference between logs, metrics and traces.

Notes:

---

## 1.1.6 — Delivery

Status: NOT STARTED

Evidence:

- [ ] I can explain code -> build -> artifact -> deployment.
- [ ] I can build the application environment from scratch.
- [ ] I can deploy a new version manually.
- [ ] I understand what could later be automated by CI/CD.

Notes:

---

# Stage 1.1 final checkpoint

Status: NOT STARTED

I can explain:

- [ ] what happens when a request enters the application;
- [ ] what is running;
- [ ] where it runs;
- [ ] how it is configured;
- [ ] where its data lives;
- [ ] what happens when dependencies fail;
- [ ] how I inspect application behaviour;
- [ ] how a new version is delivered.

Final reflection:

To be completed when Stage 1.1 finishes.
