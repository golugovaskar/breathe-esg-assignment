# TRADEOFFS.md

# Deliberate Tradeoffs

This prototype intentionally prioritizes realistic ingestion and analyst workflow over feature breadth.

---

# 1. No live third-party integrations

Not built:

- SAP OData/BAPI integrations
- Concur/Navan APIs
- utility provider APIs

Why?

The assignment timeline was limited and the objective was to demonstrate ingestion architecture, normalization, and analyst review rather than production-grade integrations.

Tradeoff:

CSV uploads were used to simulate realistic enterprise exports while keeping the prototype explainable and testable.

Future version:

Replace CSV ingestion with connector-based pipelines.

---

# 2. No authentication or role-based permissions

Not built:

- login system
- analyst/admin permissions
- tenant authentication

Why?

The assignment emphasized analyst workflow and ingestion quality.

Adding authentication would increase engineering complexity without materially improving the prototype evaluation goals.

Tradeoff:

The system assumes a trusted analyst environment.

Future version:

Add role-based access control and tenant isolation.

---

# 3. No advanced emissions calculations

Not built:

- emission factor computation
- airport-distance calculation
- tariff-based electricity modeling
- procurement category mapping

Why?

The assignment context explicitly emphasized ingestion and normalization over carbon computation.

Focus was placed on:

- ingestion quality
- suspicious row detection
- normalization
- analyst review

Tradeoff:

The prototype stores normalized activity data but does not calculate final carbon outputs.

Future version:

Integrate emissions factors and carbon calculation pipelines.