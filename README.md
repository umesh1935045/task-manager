# 📝 Task Manager

A simple and efficient **Task Manager web application** for creating, viewing, updating, and deleting tasks. The project uses a **Flask REST API** for the backend, **SQLite** for data storage, and a web-based frontend for interacting with tasks.

---

## 🚀 Features

* ✅ Create new tasks
* 📋 View all tasks
* ✏️ Mark tasks as completed or incomplete
* 🗑️ Delete tasks
* 💾 Persistent task storage using SQLite
* 🔌 RESTful API built with Flask
* 🌐 Cross-Origin Resource Sharing (CORS) enabled
* 🧪 Automated API testing using Pytest
* ⚡ Lightweight and easy to run locally

---

## 🛠️ Tech Stack

| Technology             | Purpose                      |
| ---------------------- | ---------------------------- |
| 🐍 Python              | Backend programming language |
| 🌶️ Flask              | REST API framework           |
| 🗄️ SQLite             | Database                     |
| 🌐 Flask-CORS          | Cross-origin API requests    |
| 🧪 Pytest              | Automated testing            |
| 📄 HTML/CSS/JavaScript | Frontend                     |

---

## 📁 Project Structure

```text
task-manager/
│
├── backend/
│   ├── __init__.py
│   ├── app.py
│   └── tasks.db
│
├── tests/
│   └── test_api.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── venv/
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/task-manager.git
```

Navigate into the project:

```bash
cd task-manager
```

---

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

You should see:

```text
(venv)
```

at the beginning of your terminal prompt.

---

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

If you don't have a `requirements.txt` yet:

```powershell
pip install Flask Flask-CORS pytest
```

You can generate one using:

```powershell
pip freeze > requirements.txt
```

---

## ▶️ Running the Application

Navigate to the backend:

```powershell
cd backend
```

Start the Flask server:

```powershell
python app.py
```

The API will run at:

```text
http://localhost:5000
```

You should see:

```text
* Running on http://127.0.0.1:5000
```

Keep this terminal running while using the application.

---

# 🔌 API Documentation

The backend provides a RESTful API for managing tasks.

## Get All Tasks

### `GET /api/tasks`

Returns all tasks ordered by newest first.

Example:

```http
GET http://localhost:5000/api/tasks
```

Example response:

```json
[
    {
        "id": 2,
        "title": "Learn Flask",
        "completed": 0
    },
    {
        "id": 1,
        "title": "Build Task Manager",
        "completed": 1
    }
]
```

---

## Create a Task

### `POST /api/tasks`

Creates a new task.

Example:

```http
POST http://localhost:5000/api/tasks
```

Request body:

```json
{
    "title": "Complete project documentation"
}
```

Example response:

```json
{
    "id": 3,
    "title": "Complete project documentation",
    "completed": 0
}
```

HTTP status:

```text
201 Created
```

---

## Update a Task

### `PUT /api/tasks/<task_id>`

Updates the completion status of a task.

Example:

```http
PUT http://localhost:5000/api/tasks/3
```

Request body:

```json
{
    "completed": 1
}
```

Example response:

```json
{
    "message": "Task updated"
}
```

---

## Delete a Task

### `DELETE /api/tasks/<task_id>`

Deletes a task from the database.

Example:

```http
DELETE http://localhost:5000/api/tasks/3
```

Example response:

```json
{
    "message": "Task deleted"
}
```

---

# 🗄️ Database

The application uses **SQLite** to store tasks.

The `tasks` table contains:

| Column      | Type    | Description                           |
| ----------- | ------- | ------------------------------------- |
| `id`        | INTEGER | Unique task identifier                |
| `title`     | TEXT    | Task description                      |
| `completed` | INTEGER | `0` for incomplete, `1` for completed |

The database is automatically initialized when the Flask application starts or is imported.

---

# 🧪 Testing

The project includes automated API tests using **Pytest**.

From the project root:

```powershell
python -m pytest -v
```

Example output:

```text
============================= test session starts =============================

tests/test_api.py::test_get_tasks PASSED
tests/test_api.py::test_create_task PASSED
tests/test_api.py::test_update_task PASSED

============================== 3 passed ==============================
```

### Test Coverage

The tests verify important API functionality including:

* GET tasks
* POST new tasks
* API response status codes
* Task creation behavior
* Database operations

---

# 🧪 Testing the API Manually

You can test the API directly from PowerShell.

### Get tasks

```powershell
Invoke-RestMethod `
  -Uri http://localhost:5000/api/tasks `
  -Method Get
```

### Create a task

```powershell
Invoke-RestMethod `
  -Uri http://localhost:5000/api/tasks `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"title":"Learn Python"}'
```

### Update a task

```powershell
Invoke-RestMethod `
  -Uri http://localhost:5000/api/tasks/1 `
  -Method Put `
  -ContentType "application/json" `
  -Body '{"completed":1}'
```

### Delete a task

```powershell
Invoke-RestMethod `
  -Uri http://localhost:5000/api/tasks/1 `
  -Method Delete
```

---

# 🔄 Application Flow

```text
        ┌──────────────────┐
        │   Web Frontend   │
        └────────┬─────────┘
                 │
                 │ HTTP Requests
                 ▼
        ┌──────────────────┐
        │   Flask REST API │
        └────────┬─────────┘
                 │
                 │ SQL Queries
                 ▼
        ┌──────────────────┐
        │   SQLite Database│
        │     tasks.db     │
        └──────────────────┘
```

The frontend communicates with the Flask backend through HTTP requests. Flask processes the requests and performs the required operations on the SQLite database.

---

# 🔐 Error Handling

The API validates incoming requests and returns appropriate HTTP status codes.

For example, attempting to create an empty task:

```json
{
    "error": "Task title is required"
}
```

Attempting to update or delete a task that doesn't exist:

```json
{
    "error": "Task not found"
}
```

---

# 📌 Future Improvements

Possible improvements for future versions include:

* 🔐 User authentication
* 👤 Multiple user accounts
* 📅 Task due dates
* 🏷️ Task categories and tags
* 🔥 Task priorities
* 🔎 Search and filtering
* 📊 Task statistics and dashboards
* 🌙 Dark mode
* 📱 Responsive mobile design
* ☁️ Cloud database integration
* 🚀 Deployment using Docker
* 🔔 Task reminders and notifications

---

# 🤝 Contributing

Contributions are welcome!

### 1. Fork the repository

### 2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

### 3. Make your changes

### 4. Run the tests

```bash
python -m pytest -v
```

### 5. Commit your changes

```bash
git add .
git commit -m "Add new feature"
```

### 6. Push your branch

```bash
git push origin feature/new-feature
```

### 7. Open a Pull Request

---

# 📄 License

This project is available for educational and personal use.

---


## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!

---

**Built with Python 🐍, Flask 🌶️, SQLite 🗄️ and JavaScript ⚡**

