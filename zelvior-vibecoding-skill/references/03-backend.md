# Backend, APIs, Data, and Realtime

Senior-level backend patterns. Apply by default. Every public endpoint gets rate limiting, timeouts, validation, and structured errors.

## Request handling

- Rate limiting: token bucket or sliding window per user, IP, and API key. Return 429 with Retry-After. Different limits for auth, forms, reads, and writes.
- Timeouts: connect, read, and total timeouts on every network call. No infinite waits. Fail fast.
- Retries: transient failures only, with jitter and exponential backoff. Cap attempts at 3. Never retry non-idempotent writes without an idempotency key.
- Circuit breakers: around every downstream call. Open after N failures, half-open probe, close on success. Never cascade failures.
- Backpressure: when downstream cannot keep up, slow the producer. Bounded queues. Shed load with 503 and Retry-After, never unbounded buffering.
- Idempotency: Idempotency-Key on all mutating endpoints. Store key, request hash, and response for 24 hours. Same key plus different payload returns 422.
- API versioning: URL or header versioning. Never break a published version. Deprecate with notice and a sunset date.
- Semantic versioning: MAJOR.MINOR.PATCH for packages and APIs. Breaking changes bump MAJOR. Changelog every release.

## Architecture

- Load balancing: health-check based routing across instances. Never send traffic to unhealthy instances.
- Reverse proxy: in front of every service. TLS termination at the edge. Request size limits. Timeout enforcement.
- API gateway: routing, auth, rate limiting, versioning, and consistent errors. One entry point.
- Service discovery: services find each other via registry, never hard-coded hosts.
- Message queues: async work off the request path. Durable, ordered where needed, with visibility timeouts.
- Pub/Sub: fan-out events. At-least-once delivery. Idempotent consumers. Schema version on every event.
- Event-driven architecture: decoupled domains. Events carry IDs, timestamps, and schema versions. Consumers handle duplicates.
- Distributed transactions: prefer sagas over two-phase commit. Every step has a compensating action.
- Saga pattern: multi-service workflows with idempotent, compensatable steps. Orchestrate or choreograph, document the choice.
- Dead letter queues: poison messages land in a DLQ. Alert on depth. Replay tooling. Never silently drop.
- Cron jobs: distributed lock so only one instance runs. Idempotent jobs. Run history and alerting on missed runs.
- WebSockets: bidirectional realtime. Heartbeats, reconnect with backoff, resume tokens, per-channel auth.
- Long polling: fallback where WebSockets are unavailable. Same event model.
- Server-Sent Events: one-way server push. Automatic reconnect. Named event types. Heartbeat comments.
- Throughput: design for peak, measure sustained rate, shed load gracefully. Load test before launch.
- P99 and tail latency: track p50, p95, p99, p999. Optimize the slowest 1 percent. Cache, precompute, or isolate slow paths.
- Network partitions: assume they happen. Degrade gracefully. Never lose committed writes silently.
- Clock skew: never trust client clocks. Server timestamps and monotonic IDs for ordering.
- CAP theorem: choose CP or AP per data set. Document the tradeoff. Never claim both.
- Leader election: single leader per shard or cluster. Fencing tokens prevent split brain.
- Distributed locks: proven store only (Redis, etcd, database advisory locks). Always set TTL. Never roll your own lock.
- Race conditions: atomic check-and-set. Never read-then-write without a lock or version.
- Dead locks: consistent lock ordering. Short transactions. Detect and retry with backoff.
- Optimistic locking: version columns for low-contention writes. Retry on conflict.
- Pessimistic locking: row locks for high-contention critical sections. Keep transactions short.

## Networking and protocols

- DNS: correct A, AAAA, CNAME, MX, TXT records. TTLs tuned per record type. Propagation checks in CI.
- TCP vs UDP: TCP for reliable ordered delivery. UDP for low-latency realtime where loss is acceptable (media, games).
- HTTP/2 and HTTP/3: enable both. HTTP/3 over QUIC where the platform supports it. No downgrade.
- GPC (Global Privacy Control): respect Sec-GPC. Treat GPC as opt-out of sale and sharing. Honor it server-side, not just in UI.
- CDN: all static assets and cacheable pages. Purge on deploy. Cache keys include vary headers.
- Edge caching: cache close to users. Vary on the right headers. Never cache personalized or sensitive responses publicly.
- Cache invalidation: event-driven invalidation plus TTL fallback. Never serve stale money, auth, or permission data.

## Data

- Database indexing: index foreign keys, filters, and joins. Measure with EXPLAIN. Drop unused indexes.
- Query optimization: profile slow queries. Rewrite N+1. Add covering indexes. Set statement timeouts.
- N+1 queries: eager load, batch, or join. Never query in a loop.
- Connection pooling: pool size tuned to database limits. Timeouts on acquire. No connection leaks. Pool per service, not per request.
- Read replicas: reads to replicas, writes to primary. Accept replication lag. Pin consistency-critical reads to primary.
- Sharding: shard by a stable key. Document the shard key and rebalancing plan before launch.
- Partitioning: partition large tables by time or tenant. Prune partitions in queries.
- Cache API responses and expensive queries. Define TTL and invalidation per resource. Stampede protection with request coalescing.
- SQL injection protection: parameterized queries only. Never string-concatenate SQL. ORM with bound parameters.
- Data persistence: server is source of truth. Local storage for drafts and prefs only. Handle conflicts with versioning.
- Hashed passwords and secrets: Argon2id for passwords. Secrets in a vault, never in code or logs.

## Frontend data patterns

- Split code into chunks. Route-level splitting. Heavy features load on demand.
- Paginate large lists. Cursor pagination for feeds. Never load unbounded lists.
- Eliminate unnecessary re-renders. Memoize, virtualize long lists, keep state close to usage.
- Minify CSS and JS. Tree-shake dead code. Remove legacy polyfills for modern browsers.
- Lazy load images and non-critical embeds. Eager load only the LCP image.
- Defer non-critical scripts. Async or defer everything off the critical path.
- Onboarding: progressive, skippable, completable in under 2 minutes.
- Empty states, loading states, and network states on every surface. Offline and slow-network handling with retry.
- Crash reporting: capture client crashes with breadcrumbs. No PII in reports.
- User flows: map every flow end to end. No dead ends. Every step has back, cancel, and error paths.
- Kill switch: global and per-feature switches that take effect without a deploy.
- OTA hotfix: signed, staged over-the-air updates where the platform allows it.
- Restore purchase: restore receipts and entitlements on every platform. Handle refunds and revocations.
