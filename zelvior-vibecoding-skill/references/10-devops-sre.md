# DevOps, Infrastructure, and SRE

## CI/CD and containers

- CI/CD: automated tests, build, and staged deploys. No manual production deploys.
- Docker: every service containerized. Multi-stage builds. Non-root user. Pinned base images.
- Kubernetes: orchestration at scale. Liveness and readiness probes on every pod. Resource limits on every container.
- Helm Charts: versioned, values-driven, reproducible installs.
- Build caching: cache dependencies and layers. Parallelize independent build steps.
- Dependency hell: pin versions, lock files, audit licenses, update on a schedule, remove unused deps.

## Infrastructure as code

- Infrastructure as code: all infra in versioned code. No click-ops in production.
- Terraform: cloud infrastructure in code. Remote state backend. Plan before apply.
- Service discovery: services find each other via registry, never hard-coded hosts.

## Deployments and rollbacks

- Blue-green deployment: two identical environments. Atomic traffic switch.
- Canary releases: small percentage first. Auto-rollback on error budget burn.
- Rolling deployments: update one batch at a time. Health-gated.
- Rollbacks: one-command rollback for every deploy. Test the rollback path.
- Feature flags: every risky change behind a flag. Kill switch per flag. Gradual rollout.
- Kill switch: global and per-feature switches without a deploy.
- OTA hotfix: signed, staged over-the-air updates where the platform allows it.
- Health checks: deep checks for dependencies, shallow checks for liveness.
- Liveness and readiness probes: liveness restarts dead pods, readiness removes unready pods from rotation.

## Scaling and performance at scale

- Autoscaling: scale on CPU, memory, queue depth, and latency. Min and max bounds set.
- Horizontal scaling: stateless services scale out. State lives in managed stores.
- Vertical scaling: stopgap only. Prefer horizontal.
- Load balancing: health-check based routing. Never send traffic to unhealthy instances.
- Reverse proxies and API gateways: TLS at the edge, timeouts, size limits, consistent errors.
- CDN, edge caching, and cache invalidation: event-driven plus TTL fallback.
- Throughput, P99, and tail latency: track p50, p95, p99, p999. Optimize the tail.
- Backpressure: slow the producer when downstream cannot keep up. Bounded queues.
- Memory leaks: profile in staging. Track heap over time. Alert on growth.
- Garbage collection: tune pause times. Monitor GC pressure. Avoid churn in hot paths.
- Thread safety: shared mutable state is locked or immutable. Race detector in CI.

## Observability

- Monitoring: golden signals (latency, traffic, errors, saturation) with dashboards and alerts.
- Logging: structured JSON logs with request IDs. No secrets in logs. Retention policy set.
- Distributed tracing: trace IDs across services. Head and tail based sampling.
- Metrics: RED and USE methods. Cardinality discipline. Alert on symptoms, not causes.
- Crash reporting: client crashes with breadcrumbs. No PII in reports.

## Incidents and operations

- Production incidents: runbooks, severity levels, comms templates, blameless response.
- On-call: rotations, handoff notes, alert fatigue control, escalation paths.
- Postmortems: timeline, root cause, action items with owners and dates. Publish internally.
- Cron jobs: distributed lock, idempotent jobs, run history, missed-run alerts.
- Dead letter queues: alert on depth. Replay tooling. Never silently drop events.
