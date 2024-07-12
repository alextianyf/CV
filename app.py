from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/index.html')
def get_home():
    return render_template('index.html')

@app.route('/projects_page.html')
def get_projects():
    return render_template('projects_page.html')

@app.route('/contact_page.html')
def get_contact():
    return render_template('contact_page.html')

if __name__ == '__main__':
    freezer.freeze()