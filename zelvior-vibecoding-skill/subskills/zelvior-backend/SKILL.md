---
name: zelvior-backend
description: Zelvior backend subskill. Use for any backend, API, database, realtime, queue, caching, or scale work — whenever the user wants to build, set up, wire up, create, add, make, implement, write, develop, put together, or get going on an API, endpoint, backend, backend service, database, DB, realtime feature, queue, cache, or needs to scale, optimize, speed up, restructure, or rework backend code, or says "I need an API", "can you build the backend", "how do I set up the database", "wire up realtime", "help me with the server-side". Part of zelvior-vibecoding-skill.
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
