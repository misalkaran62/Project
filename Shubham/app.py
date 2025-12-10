from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

contacts = {}     # name → {age,email,mobile}


@app.route("/")
def home():
    return render_template("contact.html", contacts=contacts, total=len(contacts))


# ADD CONTACT
@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    age = request.form["age"]
    email = request.form["email"]
    mobile = request.form["mobile"]

    contacts[name] = {"age": age, "email": email, "mobile": mobile}
    return redirect("/")


# DELETE CONTACT
@app.route("/delete/<name>")
def delete(name):
    if name in contacts:
        del contacts[name]
    return redirect("/")


# UPDATE CONTACT PAGE
@app.route("/update/<name>")
def update_page(name):
    data = contacts.get(name)
    return render_template("update.html", name=name, data=data)


# SAVE UPDATED CONTACT
@app.route("/update/save/<name>", methods=["POST"])
def update(name):
    age = request.form["age"]
    email = request.form["email"]
    mobile = request.form["mobile"]

    contacts[name] = {"age": age, "email": email, "mobile": mobile}
    return redirect("/")


# SEARCH CONTACT
@app.route("/search", methods=["POST"])
def search():
    key = request.form["search"]
    result = None

    if key in contacts:
        result = contacts[key]

    return render_template("search.html", key=key, result=result)


# EXIT / CLOSE (AUTO)
@app.route("/exit")
def exit_app():
    return "<h1>Application Closed Automatically ✔</h1>"


if __name__ == "__main__":
    app.run(debug=True)
