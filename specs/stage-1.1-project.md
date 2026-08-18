# Stage 1.1 Project Specification

## Project purpose

This project is a learning vehicle for:

**Stage 1.1 — Understand an application end-to-end**

The goal is not to build an impressive product.

The goal is to create a small system that is simple enough to understand completely and realistic enough to expose the lifecycle of a backend application.

---

## Working name

**Task Service**

The name and domain are intentionally unimportant.

Do not spend learning time on branding, UI design or product complexity.

---

## Functional scope

The application represents a minimal task-management backend.

It should eventually support a small set of operations such as:

- create a task;
- retrieve a task;
- list tasks;
- update a task status.

The exact API design should be decided by the learner during the relevant micro-objective.

The specification intentionally does not prescribe endpoint names, data models or implementation code.

---

## Technical constraints

Preferred learning stack:

- Python
- FastAPI
- PostgreSQL
- Docker

The learner should decide the concrete implementation details.

Additional libraries should only be added when a current learning need justifies them.

---

## Progressive build strategy

Do not implement the full project at the beginning.

The project should grow with the active micro-objective.

### 1.1.1 — Request lifecycle

Minimum project capability:

- application can start;
- at least one HTTP request can be sent;
- the request reaches application logic;
- a response is returned.

No database is required yet.

Primary question:

> What happens from client request to application response?

---

### 1.1.2 — Runtime and execution

Extend the same application so that the learner can investigate:

- Python runtime;
- running process;
- server;
- port;
- execution outside the IDE;
- Docker image;
- Docker container.

Primary question:

> What exactly is running and where?

---

### 1.1.3 — Configuration

Introduce external configuration.

The application should need at least some configuration that can change without editing application code.

Examples of configuration categories:

- database connection;
- log level;
- environment name.

Do not introduce secrets merely to create artificial complexity.

Primary question:

> What does this application need from its environment?

---

### 1.1.4 — Persistence

Introduce PostgreSQL.

The application should persist and retrieve task data.

The learner should be able to observe what happens when the database is:

- available;
- unavailable.

Primary question:

> Where does application state live and how does the application reach it?

---

### 1.1.5 — Basic observability

Introduce useful application logging.

The learner should deliberately create simple failure scenarios and investigate them.

Examples:

- invalid request;
- unexpected application error;
- unavailable database.

Metrics and traces are conceptual extensions only unless they become useful for a concrete experiment.

Primary question:

> What evidence does the application provide when something happens?

---

### 1.1.6 — Delivery

The learner should be able to move from a source-code change to a new running version.

At minimum this should expose:

- source change;
- tests;
- build/package step where applicable;
- Docker image;
- running application version.

Automation is optional.

Primary question:

> How does a change become a running version?

---

## Non-functional learning constraints

The project must remain intentionally small.

Prefer:

- clarity;
- inspectability;
- easy failure injection;
- easy local execution.

Avoid unnecessary:

- abstractions;
- frameworks;
- distributed components;
- frontend;
- authentication;
- production hardening;
- cloud architecture;
- microservices;
- message brokers;
- AI functionality.

These may be introduced in future stages if justified.

---

## AI constraint

AI assistants must not implement the project by default.

They may:

- ask questions;
- review learner-written code;
- explain concepts;
- propose experiments;
- point to documentation;
- challenge design reasoning.

They must not provide copy-paste implementation solutions unless the learner explicitly leaves Mentor Mode.

---

## Definition of project success

The project is successful when it enables the learner to explain and demonstrate:

1. request flow;
2. runtime and execution;
3. configuration;
4. persistence;
5. dependency failure;
6. basic observability;
7. delivery of a new version.

Project size, feature count and code sophistication are not success metrics.
