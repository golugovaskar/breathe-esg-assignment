# MODEL.md

# Data Model Design

This prototype was designed to ingest sustainability and emissions-related activity data from multiple enterprise systems, normalize it, and support analyst review before audit sign-off.

The design prioritizes:

- Multi-tenancy
- Scope 1 / 2 / 3 categorization
- Source-of-truth tracking
- Unit normalization
- Review workflow
- Audit trail

---

# 1. Tenant Model

Purpose:

A client company onboarded into the system.

Example:

- ABC Manufacturing
- Tata Steel
- Siemens India

Why?

Breathe ESG works with multiple enterprise customers. A tenant model enables logical separation of data between companies.

Fields:

- id
- name
- created_at
- updated_at

Relationship:

One tenant can have:

- many emission records
- many data sources

---

# 2. DataSource Model

Purpose:

Tracks where data originated from.

Supported prototype sources:

- SAP fuel/procurement export
- Utility electricity export
- Corporate travel export

Why?

The assignment requires source-of-truth tracking.

We must know:

- which source produced a row
- when it entered the system
- provenance of uploaded data

Fields:

- tenant
- source_type
- created_at
- updated_at

Example values:

- SAP
- UTILITY
- TRAVEL

Design decision:

The prototype uses CSV ingestion because enterprise sustainability teams commonly work with exports from operational systems rather than direct integrations during onboarding.

---

# 3. EmissionRecord Model

Purpose:

Stores normalized sustainability activity rows.

This acts as the core business entity.

Example records:

Fuel:

Diesel | 500 L

Electricity:

4500 kWh

Travel:

Flight | DEL → BLR

Fields:

- tenant
- source
- activity_type
- raw_value
- raw_unit
- normalized_value
- normalized_unit
- scope
- suspicious
- status
- created_at
- updated_at

Why this model?

Enterprise sustainability data is inconsistent.

The model stores:

Raw values:

Example:

200 GAL

Normalized values:

Example:

757.08 L

This preserves traceability and enables auditability.

Status values:

- PENDING
- APPROVED
- REJECTED

Scope categorization:

Scope 1

- fuel combustion
- diesel
- petrol

Scope 2

- purchased electricity

Scope 3

- corporate travel

Suspicious flag:

Used to surface unusual or potentially invalid rows.

Examples:

- zero electricity usage
- invalid travel category
- missing travel location

---

# 4. ReviewAction Model

Purpose:

Captures analyst review decisions.

Why?

Analysts must review and sign off before auditors.

Each review stores:

- who reviewed
- action taken
- comment
- timestamp

Actions:

- APPROVED
- REJECTED

Relationship:

One emission record can have multiple review actions.

This preserves review history.

---

# 5. AuditLog Model

Purpose:

Immutable history of analyst actions.

Why?

Audit readiness requires change tracking.

Examples:

- approved record
- rejected record
- comment added

Stored:

- emission record
- action
- changed_by
- change_note
- timestamp

This supports audit traceability.

---

# Relationships

Tenant
    ↓
DataSource
    ↓
EmissionRecord
    ↓
ReviewAction
    ↓
AuditLog

---

# Why This Model

This model was optimized for:

1. realistic ingestion from enterprise systems

2. explainable audit trail

3. analyst usability

4. prototype simplicity within assignment constraints

Instead of overengineering integrations, the prototype prioritizes a defendable architecture that can realistically evolve into production.