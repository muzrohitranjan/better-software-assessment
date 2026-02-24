# Better Software Assessment – Task Manager

This is a small full-stack task management system built as part of the Better Software Associate Software Engineer assessment.

The goal of this project is not feature richness, but clarity, correctness, and maintainability.

---

## Architecture

- Backend: Flask REST API  
- Database: SQLite  
- Frontend: React  
- Communication: JSON over HTTP  

The frontend communicates with the Flask backend using REST APIs.  
All business logic and validation are handled on the backend.

---

## Project Structure

```text
better-software-assessment/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── README.md
├── frontend/
│   ├── src/
│   ├── package.json
│   └── README.md
├── README.md
├── ai_guidance.md
└── demo.png

## Backend Design

Endpoints:

- GET /tasks – Fetch all tasks
- POST /tasks – Create a new task

Data Model:

Task:
- id (integer)
- title (string)

## Key Technical Decisions

- Flask chosen for lightweight API development.
- SQLite chosen for simple relational storage.
- Backend handles validation.
- Virtual environments excluded from repository.
- Project kept intentionally small.

## AI Usage

ChatGPT was used to:
- Bootstrap Flask boilerplate
- Review API design
- Suggest folder structure

All generated code was manually reviewed and tested.

## Risks

- No authentication
- No rate limiting
- SQLite not production scale

## Extension Plan

- Add PUT/DELETE APIs
- React frontend
- Validation schemas
- Automated tests
- Docker support