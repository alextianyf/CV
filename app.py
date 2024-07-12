from flask import Flask, render_template
from flask_frozen import Freezer
import shutil
import os
import logging

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
    # Freeze the application
    freezer.freeze()
    
    # Define source and destination paths
    source_path = os.path.join('build', 'index.html')
    destination_path = os.path.join('index.html')
    
    try:
        # Copy index.html from build folder to root folder
        shutil.copyfile(source_path, destination_path)
        logging.info(f'Copied {source_path} to {destination_path}')
    except FileNotFoundError:
        logging.error(f'The file {source_path} does not exist')
    except Exception as e:
        logging.error(f'An error occurred while copying the file: {e}')