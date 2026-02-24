# Backend – Task Manager (Flask API)

This is the Flask backend for the Task Manager application.

It provides RESTful APIs for managing tasks and uses SQLite for storage.

---

## Tech Stack

- Python
- Flask
- SQLite

---

## How to Run Backend

From project root:

```bash
cd backend
python -m venv venv
source venv/Scripts/activate   # Windows
pip install -r requirements.txt
python app.py

## API

GET /tasks  
POST /tasks  

Backend runs at: http://127.0.0.1:5000