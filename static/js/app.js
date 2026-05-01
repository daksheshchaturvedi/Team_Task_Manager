function openModal() {
    window.location.href = "/create-project/";
}
let currentProjectId = null;

function openProject(projectId) {
    currentProjectId = projectId;

    document.getElementById("board").classList.remove("hidden");
    document.getElementById("taskInput").classList.remove("hidden");

    fetch(`/tasks/get/${projectId}/`)
        .then(res => res.json())
        .then(data => renderTasks(data));
}

function renderTasks(tasks) {
    document.getElementById("todo").innerHTML = "";
    document.getElementById("inprogress").innerHTML = "";
    document.getElementById("done").innerHTML = "";

    tasks.forEach(task => {
        const div = document.createElement("div");
        div.className = "task";
        div.innerText = task.title;

        div.onclick = () => moveTask(task.id, task.status);

        if (task.status === "TODO") {
            document.getElementById("todo").appendChild(div);
        } else if (task.status === "IN_PROGRESS") {
            document.getElementById("inprogress").appendChild(div);
        } else {
            document.getElementById("done").appendChild(div);
        }
    });
}

function moveTask(taskId, currentStatus) {
    let newStatus;

    if (currentStatus === "TODO") {
        newStatus = "IN_PROGRESS";
    } else if (currentStatus === "IN_PROGRESS") {
        newStatus = "DONE";
    } else {
        newStatus = "TODO";
    }

    fetch("/tasks/update/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            task_id: taskId,
            status: newStatus
        })
    })
    .then(() => {
        location.reload();
    });
}

function addTask() {
    const title = document.getElementById("taskTitle").value;

    fetch("/tasks/create/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: title,
            project_id: currentProjectId
        })
    })
    .then(res => res.json())
    .then(() => {
        openProject(currentProjectId);
    });
}