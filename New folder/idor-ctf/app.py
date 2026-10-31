from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "ctf-secret-key"

users = {
    1: {
        "username": "admin",
        "email": "admin@ctf.local",
        "flag": "flag{idor_admin_profile_disclosure}"
    },
    2: {
        "username": "guest",
        "email": "guest@ctf.local",
        "flag": "No flag here"
    }
}

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    session["user_id"] = 2
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/profile")
def profile():
    uid = int(request.args.get("id", 2))

    # IDOR Vulnerability!
    user = users.get(uid)

    return render_template("profile.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)