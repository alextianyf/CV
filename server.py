from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year = current_year)

@app.route("/aboutme")
def get_aboutme():
    return render_template("aboutme.html")

@app.route("/projects")
def get_projects():
    return render_template("projects.html")

if __name__ == "__main__":
    app.run(debug=True)