# Stage 1.1 Checkpoint

## Purpose

This checkpoint evaluates whether Stage 1.1 produced a usable mental model of a small running application.

It is not a certification exam.

It should identify:

- what is consolidated;
- what is partially understood;
- what still requires practice.

The evaluation should use the project in `/app` as evidence.

---

## Evaluation rule

A concept is not considered demonstrated because:

- a course was completed;
- documentation was read;
- AI explained it;
- code exists in the repository.

The learner should be able to explain, apply or investigate it independently.

---

## Rating scale

Use only these three states:

### NOT YET

The learner cannot yet explain or demonstrate the concept without substantial guidance.

### PARTIAL

The learner understands the main idea but has gaps, uncertainty or needs meaningful prompting.

### DEMONSTRATED

The learner can explain and demonstrate the concept with reasonable independence.

A micro-objective does not require perfection.

---

# Evaluation

## A. Request lifecycle

Ask the learner to choose one real request in the application.

Without reading the implementation first, ask:

> Walk me through what happens from the moment the client sends this request until the client receives the response.

Look for understanding of:

- HTTP request;
- route / endpoint;
- input data;
- application logic;
- response;
- status code;
- serialization at an appropriate level.

Rating:

`NOT YET / PARTIAL / DEMONSTRATED`

Evidence:

---

## B. Runtime and execution

Ask:

> What exactly is running when this application is available locally?

Then ask the learner to distinguish:

- source code;
- Python runtime;
- server process;
- port;
- Docker image;
- Docker container.

Ask the learner to start the application outside the IDE.

Rating:

`NOT YET / PARTIAL / DEMONSTRATED`

Evidence:

---

## C. Configuration

Ask:

> What information does the environment need to provide for this application to run correctly?

Ask the learner to demonstrate one configuration change without changing application logic.

Look for an appropriate mental model of:

- configuration;
- environment variables;
- environment-specific values;
- connection information;
- secret handling at a basic level.

Rating:

`NOT YET / PARTIAL / DEMONSTRATED`

Evidence:

---

## D. Persistence

Ask:

> When I create a task, where does that information actually live?

Then stop or disconnect the database.

Ask:

> What do you predict will happen now?

Have the learner test the prediction and inspect the result.

Rating:

`NOT YET / PARTIAL / DEMONSTRATED`

Evidence:

---

## E. Observability and failure investigation

Introduce or select a simple failure.

Do not tell the learner the cause.

Ask:

> How would you investigate this without immediately opening the debugger?

Look for use of:

- available logs;
- error context;
- request information;
- timing or status information;
- hypothesis and evidence.

Then ask:

> What is the difference between a log, a metric and a trace?

A conceptual answer is sufficient for metrics and traces at this stage.

Rating:

`NOT YET / PARTIAL / DEMONSTRATED`

Evidence:

---

## F. Delivery

Ask:

> You changed one line of application behaviour. What needs to happen before users can execute the new version?

Ask the learner to perform the local delivery path used by the project.

Look for understanding of:

- source change;
- test;
- artifact / package concept;
- image;
- running version.

Rating:

`NOT YET / PARTIAL / DEMONSTRATED`

Evidence:

---

# Cross-cutting questions

These questions test whether concepts have connected into a system model.

### Question 1

> If the API returns HTTP 500, what different layers could contain the cause?

### Question 2

> If the application process is running but requests cannot reach it, what categories of things would you investigate?

### Question 3

> If the source code has not changed but behaviour differs between two environments, what would you investigate?

### Question 4

> If the application restarts, which information survives and why?

### Question 5

> Draw the complete system as you currently understand it.

The drawing does not need formal notation.

---

# Stage decision

Stage status:

`NOT COMPLETE / COMPLETE WITH GAPS / COMPLETE`

Recommended default:

- mark **NOT COMPLETE** if one or more core areas remain `NOT YET`;
- mark **COMPLETE WITH GAPS** if the model is coherent but some areas remain partial;
- mark **COMPLETE** when the learner demonstrates a coherent end-to-end model with reasonable independence.

The final decision requires human approval.

AI may recommend a status but must not approve completion autonomously.

---

## Final reflection

### What can I now explain that I could not explain before?

---

### Which concept changed my mental model the most?

---

### Where did I rely too much on memorized steps instead of understanding?

---

### What remains unclear?

---

### What new questions appeared?

---

## Next-stage rule

Do not design the next stage before completing this reflection.

The next stage should be based on demonstrated gaps and newly discovered needs, not on the original long-term roadmap.
