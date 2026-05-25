# SOURCES.md

# Research Sources and Assumptions

This document explains the real-world formats researched, what subset was handled, and assumptions made.

---

# 1. SAP Fuel / Procurement Data

Research summary

SAP data is commonly exposed through:

- IDoc
- BAPI
- OData services
- flat file exports (CSV/Excel)

Decision

The prototype uses CSV upload to represent SAP flat-file exports.

Why?

During sustainability onboarding, exported operational reports are commonly shared before deep ERP integrations exist.

Sample data used

Example:

Diesel,500,L
Petrol,200,GAL

What was learned

Real-world SAP exports contain:

- inconsistent units
- internal plant codes
- ERP-specific naming
- inconsistent formatting

What would break in production

- multilingual SAP fields
- plant lookup dependencies
- nested ERP exports
- live sync reliability

---

# 2. Utility Electricity Data

Research summary

Facilities teams commonly obtain utility data through:

- provider portals
- billing exports
- PDFs
- APIs (less common)

Decision

CSV upload was chosen to simulate portal export.

Sample data used

Example:

meter_id,billing_start,billing_end,usage_kwh

What was learned

Electricity data includes:

- meter readings
- billing periods
- tariff structures
- inconsistent reporting windows

What would break in production

- tariff complexity
- PDF extraction
- non-standard billing periods
- provider-specific schemas

---

# 3. Corporate Travel Data

Research summary

Corporate travel systems (Concur/Navan) expose:

- flights
- hotels
- ground transport
- airport/location codes

Decision

CSV upload was used to simulate exported travel activity.

Sample data used

Example:

employee_id,travel_type,from_location,to_location,date

What was learned

Travel systems often provide:

- incomplete distance data
- airport codes only
- category-specific travel records

What would break in production

- missing location resolution
- emission factor selection
- incomplete travel records
- vendor schema differences