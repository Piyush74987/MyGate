from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Simple demo auth
        if username in ["resident", "guard", "admin"] and password == "password":
            if username == "resident":
                return redirect(url_for("dashboard"))
            elif username == "guard":
                return redirect(url_for("visitors"))
            else:
                return redirect(url_for("dashboard"))
        else:
            error = "Invalid credentials"
    return render_template("login.html", error=error)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/visitors")
def visitors():
    return render_template("visitors.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
