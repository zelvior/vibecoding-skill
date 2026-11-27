---
name: zelvior-backend
description: Zelvior backend subskill. Use for absolutely any request that involves, touches, or concerns a backend, API, database, realtime, queue, caching, server-side, or scale — no matter the wording or register. Matches whether the user wants to build, set up, wire up, create, add, make, implement, write, develop, code, put together, spin up, or get going on an API, endpoint, backend, backend service, server, server-side, database, DB, data store, realtime feature, live data, queue, job queue, cache, or needs to scale, optimize, speed up, restructure, rework, tune, or refactor backend code — or says I need an API, I need a backend, can you build the backend, can you build the API, how do I set up the database, how do I create an endpoint, wire up realtime, help me with the server-side, help me with the backend, set up the DB, add an endpoint, and anything even loosely like it. Part of zelvior-vibecoding-skill.
---

# Zelvior Backend Subskill

Build resilient, observable, production-grade backends. Read `../../references/03-backend.md` and `../../references/04-frontend-data.md` for full detail.

## Must-have

Rate limiting, caching (API responses and expensive queries), load balancing, reverse proxies, API gateways, service discovery, circuit breakers, timeouts, retries with exponential backoff, idempotency keys, message queues, pub/sub, event-driven architecture, sagas over distributed transactions, dead letter queues, cron jobs with locking, WebSockets, long polling, server-sent events, throughput and P99/tail latency tracking, network partition handling, clock skew discipline, DNS, TCP vs UDP, HTTP/2 and HTTP/3, GPC respect, API and semantic versioning, database indexing, query optimization, N+1 elimination, connection pooling, read replicas, sharding, partitioning, leader election, CAP tradeoffs, optimistic and pessimistic locking, distributed locks, race and deadlock prevention, code splitting, pagination, minification, lazy loading, deferred scripts, SQL injection protection, onboarding, empty/loading/network states, data persistence, crash reporting, accessibility, user flows, Argon2id password hashing, bot protection, session expirations, CSRF protection, kill switches, OTA hotfix, restore purchase, internal links, breadcrumbs.

## Rules

- Every public endpoint: rate limit, timeout, validation, structured errors.
- Every mutating endpoint: idempotency key. Every downstream call: timeout plus circuit breaker.
- Never string-concatenate SQL. Parameterized queries only.
- Never trust client clocks or client-supplied IDs. Authorize every object server-side.
