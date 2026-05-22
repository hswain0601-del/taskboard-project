from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Setup Jenkins pipeline", "status": "In Progress", "priority": "High"},
    {"id": 2, "title": "Dockerize TaskBoard app", "status": "Todo", "priority": "Medium"},
    {"id": 3, "title": "Deploy to Kubernetes", "status": "Todo", "priority": "High"},
]

next_id = 4


@app.route("/", methods=["GET", "POST"])
def index():
    global next_id

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        status = request.form.get("status", "Todo")
        priority = request.form.get("priority", "Medium")

        if title:
            tasks.append(
                {
                    "id": next_id,
                    "title": title,
                    "status": status,
                    "priority": priority,
                }
            )
            next_id += 1

        return redirect(url_for("index"))

    return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("index"))


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/ready")
def ready():
    return {"status": "ready"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)