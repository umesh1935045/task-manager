
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = "tasks.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    """)

    connection.commit()
    connection.close()



initialize_database()


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    connection = get_db_connection()

    tasks = connection.execute(
        "SELECT * FROM tasks ORDER BY id DESC"
    ).fetchall()

    connection.close()

    return jsonify([dict(task) for task in tasks])


@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({
            "error": "Task title is required"
        }), 400

    title = data["title"].strip()

    if not title:
        return jsonify({
            "error": "Task title cannot be empty"
        }), 400

    connection = get_db_connection()

    cursor = connection.execute(
        "INSERT INTO tasks (title) VALUES (?)",
        (title,)
    )

    connection.commit()

    task_id = cursor.lastrowid

    connection.close()

    return jsonify({
        "id": task_id,
        "title": title,
        "completed": 0
    }), 201


@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    if not data or "completed" not in data:
        return jsonify({
            "error": "Completed status is required"
        }), 400

    completed = data["completed"]

    connection = get_db_connection()

    cursor = connection.execute(
        "UPDATE tasks SET completed = ? WHERE id = ?",
        (int(completed), task_id)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()

        return jsonify({
            "error": "Task not found"
        }), 404

    connection.close()

    return jsonify({
        "message": "Task updated"
    }), 200


@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    connection = get_db_connection()

    cursor = connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()

        return jsonify({
            "error": "Task not found"
        }), 404

    connection.close()

    return jsonify({
        "message": "Task deleted"
    }), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
