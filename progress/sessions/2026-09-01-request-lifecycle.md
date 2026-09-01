# Session snapshot — 2026-09-01

## Focus

Stage 1.1 — Understand an application end-to-end
Micro-objective: 1.1.1 — Request lifecycle

Status: `COMPLETE`

---

## Concepts covered

- HTTP method and URL/endpoint as method+resource pair (same URL, different methods).
- Headers as the channel for metadata (authentication token), distinct from URL and body.
- Body used for larger/structured payloads (e.g. batch operations), as a trade-off against URL limitations.
- Status codes: 2xx / 4xx / 5xx ranges, and the 401 vs 403 distinction (401 = identity not established, 403 = identity known but not permitted) — initially reversed, corrected through guided reasoning.
- Serialization vs deserialization as inverse operations (incoming message → internal objects vs internal objects → outgoing message).
- Full request cycle: Client → Uvicorn → FastAPI app instance → routing → endpoint function → response.
- Role separation between Uvicorn (ASGI server: sockets, TCP, raw HTTP parsing) and FastAPI (routing and application logic).

---

## Practical evidence

Created `app/main.py` with a minimal `GET /hello` endpoint (FastAPI + Uvicorn), returning `{"status": "ok", "message": "Hello World"}`. Server run inside a `.venv`.

Real request log observed and interpreted:

```
GET / HTTP/1.1" 404 Not Found
GET /favicon.ico HTTP/1.1" 404 Not Found
GET /hello HTTP/1.1" 200 OK
```

- `/` → 404 explained as a manual request to an undefined route.
- `/favicon.ico` → 404 explained as the browser's automatic favicon request, not user-initiated.
- `/hello` → 200 OK, full cycle described in the learner's own words including the module:instance import mechanics.

## Diagram (learner-produced)

```
Cliente -> Uvicorn -> modulo main.py -> instancia FastAPI (app) -> endpoint /hello GET -> función hello_world() -> respuesta -> Cliente
```

Refined during the session: the module/app instance is loaded once at server startup, not per request; routing, execution and serialization happen per request.

---

## Incidents diagnosed during the session

1. **Module reference / working directory issue.** Running `uvicorn main:app` from the project root failed with `Could not import module "main"` because the file lived in `app/main.py`. The learner understood the `module:instance` syntax (module = the `.py` file, `app` = the FastAPI instance variable inside it) and resolved it by running `uvicorn app.main:app` from the project root.

2. **Multiple Python interpreters on PATH.** `pip install fastapi uvicorn` installed into the Python 3.14 interpreter (first on PATH), but the `uvicorn` command resolved to a separate Python 3.11 installation that never had `fastapi` installed, producing `ModuleNotFoundError: No module named 'fastapi'`. Diagnosed via `where python` / `where pip` / `where uvicorn`. Resolved by creating and activating a `.venv`, which isolates the interpreter/pip/uvicorn resolution for the project.

## Note on deserialization

For `GET /hello`, there was no application body to deserialize — but the raw HTTP request is still parsed and interpreted by the server stack (Uvicorn/FastAPI) regardless of whether an application-level body is present.

---

## Evidence checklist (1.1.1)

- [x] I can draw the request lifecycle.
- [x] I can explain every major step.
- [x] I can follow one request through my application.
- [x] I can explain the response that is returned.

---

## Next agreed action

Continue with 1.1.2 — Runtime and execution, building on what was already surfaced this session about `.venv`, multiple Python interpreters, and starting the server from outside the IDE.
