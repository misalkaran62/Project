from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# -----------------------------
# DATABASE INIT
# -----------------------------
def init_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS stories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# -----------------------------
# HOME - SHOW ALL STORIES
# -----------------------------
@app.route("/")
def home():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM stories")
    data = cur.fetchall()
    conn.close()
    return render_template("index.html", stories=data)

# -----------------------------
# ADD STORY
# -----------------------------
@app.route("/add", methods=["POST"])
def add_story():
    title = request.form["title"]
    content = request.form["content"]

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO stories (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))

# -----------------------------
# DELETE STORY
# -----------------------------
@app.route("/delete/<int:id>")
def delete_story(id):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM stories WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))

# -----------------------------
# UPDATE STORY PAGE
# -----------------------------
@app.route("/edit/<int:id>")
def edit_story(id):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM stories WHERE id = ?", (id,))
    story = cur.fetchone()
    conn.close()
    return render_template("edit.html", story=story)

# -----------------------------
# UPDATE STORY SAVE
# -----------------------------
@app.route("/update/<int:id>", methods=["POST"])
def update_story(id):
    title = request.form["title"]
    content = request.form["content"]

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("UPDATE stories SET title = ?, content = ? WHERE id = ?", (title, content, id))
    conn.commit()
    conn.close()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
