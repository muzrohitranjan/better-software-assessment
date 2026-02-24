from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    if not data or not data.get("title"):
        return jsonify({"error": "Title required"}), 400

    task = Task(title=data["title"])
    db.session.add(task)
    db.session.commit()

    return jsonify({"id": task.id, "title": task.title}), 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "title": t.title} for t in tasks])

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)