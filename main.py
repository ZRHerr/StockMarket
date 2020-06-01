import hashlib
import os
import sqlite3

import aggregator as agg
from flask import *

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = set(["jpeg", "jpg", "png", "gif"])


def getLoginDetails():
    with sqlite3.connect("database.db") as conn:
        cur = conn.cursor()
        if "email" not in session:
            loggedIn = False
            firstName = ""
            noOfItems = 0
        else:
            loggedIn = True
            cur.execute("SELECT userId, firstName FROM users WHERE email = ?", (session["email"],))
            userId, firstName = cur.fetchone()
            cur.execute("SELECT count(symbolId) FROM watchList WHERE userId = ?", (userId,))
            noOfItems = cur.fetchone()[0]
    conn.close()
    return (loggedIn, firstName, noOfItems)


@app.route("/")
def root():
    loggedIn, firstName, noOfItems = getLoginDetails()
    with sqlite3.connect("database.db") as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT symbolId, name, currentPrice, closePrice, openPrice, percentageChange, description, image FROM symbols"
        )
        itemData = cur.fetchall()
    itemData = parse(itemData)
    return render_template(
        "main.html", itemData=itemData, loggedIn=loggedIn, firstName=firstName, noOfItems=noOfItems
    )


@app.route("/loginForm")
def loginForm():
    if "email" in session:
        return redirect(url_for("root"))
    else:
        return render_template("loginForm.html", error="")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if is_valid(email, password):
            session["email"] = email
            return redirect(url_for("root"))
        else:
            error = "Invalid UserId / Password"
            return render_template("loginForm.html", error=error)


@app.route("/registerationForm")
def registrationForm():
    return render_template("registerationForm.html")


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS


def parse(data):
    ans = []
    i = 0
    while i < len(data):
        curr = []
        for j in range(7):
            if i >= len(data):
                break
            curr.append(data[i])
            i += 1
        ans.append(curr)
    return ans


if __name__ == "__main__":
    app.run(debug=True)
