from flask import Flask, render_template
import datetime

app = Flask(__name__)

current_year = datetime.datetime.now().year

@app.route("/")
def home():
    return render_template("index.html", year = current_year)

@app.route("/aboutme")
def get_aboutme():
    return render_template("aboutme.html")

@app.route("/projects")
def get_projects():
    return render_template("projects.html", year = current_year)

if __name__ == "__main__":
    app.run(debug=True)