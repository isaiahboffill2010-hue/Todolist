from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todo_list = []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task").strip()

        if task != "":
            todo_list.append(task)

        return redirect("/")

    return render_template("index.html", todo_list=todo_list)


@app.route("/delete/<int:task_index>")
def delete_task(task_index):
    if 0 <= task_index < len(todo_list):
        todo_list.pop(task_index)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)