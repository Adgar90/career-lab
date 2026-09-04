# Current Level

## Global context

Current global stage:

**Software Developer with initial autonomy**

Current development objective:

**Develop stronger Software Engineering fundamentals and progressively increase technical ownership.**

Only the current learning stage is defined in detail.

Future stages will be designed after completing the current checkpoint.

---

# Stage 1.1 — Understand an application end-to-end

## Objective

Understand and explain the complete basic lifecycle of a small application.

At the end of this stage I should be able to explain:

- what happens when a request reaches the application;
- where the application runs;
- how it is configured;
- where its data is persisted;
- what dependencies it has;
- how I can understand what it is doing;
- what happens when something fails;
- how a new version reaches a running environment.

The goal is not to master infrastructure or cloud.

The goal is to construct a correct mental model of a running application.

---

## Learning project

Use one small backend application as the learning vehicle.

Preferred stack:

- Python
- FastAPI
- PostgreSQL
- Docker

Additional technologies should only be introduced when required by a learning objective.

The project should remain intentionally small.

No frontend is required.

AI functionality is not required during this stage.

---

# Micro-objectives

## 1.1.1 — Request lifecycle

### Question

> What happens from the moment a client sends a request until it receives a response?

### Minimum concepts

- HTTP request
- HTTP response
- method
- URL
- route
- headers
- body
- status code
- serialization
- endpoint
- application logic

### Evidence

I can draw and explain the request flow without reading the implementation.

### Done when

I can explain the lifecycle of one real request through my application.

---

## 1.1.2 — Runtime and execution

### Question

> What exactly am I executing and where is it running?

### Minimum concepts

- source code
- Python runtime
- process
- operating system
- port
- server
- image
- container

### Evidence

I can explain the difference between:

- source code;
- runtime;
- process;
- Docker image;
- Docker container.

### Done when

I can run the application outside the IDE and explain what is running.

---

## 1.1.3 — Configuration

### Question

> How does the same application behave differently depending on its environment?

### Minimum concepts

- application configuration
- environment variables
- connection strings
- secrets
- development environment
- production environment

### Evidence

I can change application configuration without modifying application code.

### Done when

I can explain what another machine would need in order to run the application.

---

## 1.1.4 — Persistence

### Question

> Where does the application's information live?

### Minimum concepts

- database
- connection
- persistence
- transaction
- migration
- basic indexing concept

### Evidence

The application persists and retrieves real data from PostgreSQL.

I can explain what happens when the database becomes unavailable.

### Done when

I understand the basic relationship between application and database.

---

## 1.1.5 — Dependencies

### Question

> What does this application need in order to run, and what happens when one of
> those things is not there?

### Minimum concepts

- direct dependency
- transitive dependency
- Python interpreter resolution
- virtual environment
- version pinning
- base image
- external service dependency
- dependency failure

### Evidence

I can list what my application depends on and explain how each dependency is
resolved when the application starts.

I can make one dependency unavailable, predict the failure and confirm it.

### Done when

I can explain the difference between what the application needs installed or
reachable and what it needs configured, and I can demonstrate one dependency
failure.

---

## 1.1.6 — Basic observability

### Question

> How do I know what my application is doing?

### Minimum concepts

- logs
- log levels
- contextual information
- request identifier
- error
- latency

Conceptual introduction only:

- metrics
- traces

### Evidence

I can intentionally cause a simple failure and investigate it using application logs without immediately using the debugger.

### Done when

My first debugging question becomes:

> What evidence does the application give me?

---

## 1.1.7 — Delivery

### Question

> How does a change in source code become a running version of the application?

### Minimum concepts

- Git commit
- build
- tests
- artifact
- Docker image
- deployment

### Evidence

I can explain and manually perform the basic path:

```text
Code
 |
 v
Tests
 |
 v
Image
 |
 v
Running application
```

### Done when

I understand the basic software delivery lifecycle.

---

# Stage checkpoint

Stage 1.1 is complete when I can explain a small application through these seven perspectives:

1. Request
2. Execution
3. Configuration
4. Persistence
5. Dependencies
6. Observability and failures
7. Delivery

The explanation should be based on the application I have built.

---

# Completion criteria

A course or tutorial does not complete this stage.

Completion requires:

### Understand

I can explain the concepts using my own words.

### Apply

I have used them in the learning project.

### Diagnose

I can investigate a simple failure related to them.

---

# Scope exclusions

The following are explicitly outside the current stage unless required by a specific problem:

- Kubernetes
- Terraform
- advanced cloud architecture
- microservices
- distributed transactions
- advanced messaging
- advanced networking
- advanced security
- high availability
- complex CI/CD
- AI agents
- RAG
- production-grade MLOps

These may belong to future stages.

They are not current objectives.

---

# Current focus

**1.1.2 — Runtime and execution**

Everything else is NEXT.

Do not optimize for Stage 1.1.7 while working on Stage 1.1.2.
