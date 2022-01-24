from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1><a href=\"/login\">Login</a>"


@app.route("/login")
def login():
    return "<h1>Login Page</h1><a href=\"/dashboard\">Dashboard</a>"


@app.route("/dashboard")
def dashboard():
    return "<h1>Dashboard</h1><a href=\"/\">start</a>"


@app.route("/api/me")
def me_api():
    return {
        "username": "t.ngo",
        "theme": "Dark",
        "image": "/images/tung.jpg",
    }
