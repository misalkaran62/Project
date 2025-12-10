from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data
students = {
    1: {"name": "Aaru", "roll": "101", "course": "BSc", "year": "1", "marks": 100},
    2: {"name": "Sana", "roll": "102", "course": "BSc", "year": "2", "marks": 200}
}
next_id = 3  # Next student ID

@app.route("/")
def index():
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():
    global next_id
    name = request.form.get("name").strip()
    roll = request.form.get("roll").strip()
    course = request.form.get("course").strip()
    year = request.form.get("year").strip()
    marks = int(request.form.get("marks"))
    students[next_id] = {"name": name, "roll": roll, "course": course, "year": year, "marks": marks}
    next_id += 1
    return redirect(url_for("index"))

@app.route("/update/<int:id>", methods=["POST"])
def update_student(id):
    if id in students:
        students[id]["name"] = request.form.get("name").strip()
        students[id]["roll"] = request.form.get("roll").strip()
        students[id]["course"] = request.form.get("course").strip()
        students[id]["year"] = request.form.get("year").strip()
        students[id]["marks"] = int(request.form.get("marks"))
    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete_student(id):
    if id in students:
        students.pop(id)
    return redirect(url_for("index"))

@app.route("/search", methods=["POST"])
def search_student():
    query = request.form.get("search").strip().lower()
    result = {id: s for id, s in students.items() if query in s["name"].lower() or query in s["roll"]}
    return render_template("index.html", students=result)

@app.route("/stats/<stat>")
def stats(stat):
    if not students:
        return redirect(url_for("index"))
    if stat == "highest":
        id_ = max(students, key=lambda x: students[x]["marks"])
        message = f"Highest Marks: {students[id_]['name']} → {students[id_]['marks']}"
    elif stat == "lowest":
        id_ = min(students, key=lambda x: students[x]["marks"])
        message = f"Lowest Marks: {students[id_]['name']} → {students[id_]['marks']}"
    elif stat == "count":
        message = f"Total Students: {len(students)}"
    else:
        message = ""
    return render_template("index.html", students=students, message=message)

if __name__ == "__main__":
    app.run(debug=True)
