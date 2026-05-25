# Breathe ESG Assignment

A prototype ESG data ingestion and analyst review platform built for the Breathe ESG engineering assignment.

## Overview

This project simulates enterprise sustainability data ingestion from multiple operational systems and provides an analyst workflow for reviewing, validating, and approving records before audit.

Supported ingestion sources:

- SAP-style fuel/procurement exports
- Utility electricity exports
- Corporate travel exports

The system supports:

- ingestion
- normalization
- suspicious row detection
- analyst review workflow
- audit traceability
- dashboard analytics

---

## Features

### Data Ingestion

Upload CSV files for:

- SAP operational activity
- Utility consumption
- Corporate travel

### Normalization

Supports raw and normalized values for auditability.

Example:

200 GAL → 757.08 L

### Review Workflow

Analysts can:

- approve records
- reject records
- review suspicious rows

### Dashboard

Includes:

- ingestion visibility
- record summaries
- suspicious record indicators
- analytics metrics

---

## Tech Stack

### Backend

- Django
- Django REST Framework
- PostgreSQL
- Gunicorn
- WhiteNoise

### Frontend

- React
- Vite
- Axios

### Deployment

- Render (backend)
- Render (frontend)

---

## Live URLs

Frontend:

[YOUR_FRONTEND_URL](https://breathe-esg-frontend-zbca.onrender.com/)

Backend:

[YOUR_BACKEND_URL](https://breathe-esg-backend-7usx.onrender.com)

Admin:

[YOUR_BACKEND_URL/admin](https://breathe-esg-backend-7usx.onrender.com/admin/)

---

## Project Structure

backend/

frontend/

docs/

---

## Documentation

Detailed design decisions are available in:

- docs/MODEL.md
- docs/DECISIONS.md
- docs/TRADEOFFS.md
- docs/SOURCES.md

---

## Local Setup

### Backend

```bash
cd backend
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
