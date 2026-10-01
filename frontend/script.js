const API_URL = "http://localhost:5000/api/tasks";


async function loadTasks() {

    const response = await fetch(API_URL);

    const tasks = await response.json();

    const taskList = document.getElementById("taskList");

    taskList.innerHTML = "";

    tasks.forEach(task => {

        const li = document.createElement("li");

        li.innerHTML = `
            <span>
                ${task.title}
            </span>

            <div>
                <button onclick="toggleTask(${task.id}, ${task.completed})">
                    ${task.completed ? "Undo" : "Complete"}
                </button>

                <button onclick="deleteTask(${task.id})">
                    Delete
                </button>
            </div>
        `;

        taskList.appendChild(li);
    });
}


async function addTask() {

    const input = document.getElementById("taskInput");

    const title = input.value.trim();

    if (!title) {

        alert("Please enter a task.");

        return;
    }

    await fetch(API_URL, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            title: title
        })
    });

    input.value = "";

    loadTasks();
}


async function toggleTask(id, completed) {

    await fetch(`${API_URL}/${id}`, {

        method: "PUT",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            completed: completed ? 0 : 1
        })
    });

    loadTasks();
}


async function deleteTask(id) {

    await fetch(`${API_URL}/${id}`, {

        method: "DELETE"
    });

    loadTasks();
}


loadTasks();