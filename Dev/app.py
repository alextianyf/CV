from flask import Flask, render_template
from flask_frozen import Freezer
import shutil
import os
import logging

app = Flask(__name__)
freezer = Freezer(app)

def copy_and_override(src, dst):
    # Check if the destination folder exists
    if os.path.exists(dst):
        # Remove the destination folder and its contents
        shutil.rmtree(dst)
    
    # Copy the source folder to the destination
    shutil.copytree(src, dst)
    print(f"Folder copied from {src} to {dst}")

@app.route('/home.html')
def get_home():
    return render_template('home.html')

@app.route('/projects_page_dev.html')
def get_projects():
    return render_template('projects_page_dev.html')

@app.route('/contact_page_dev.html')
def get_contact():
    return render_template('contact_page_dev.html')

if __name__ == '__main__':
    # Freeze the application
    freezer.freeze()
    
    # Define source and destination paths
    source_path = os.path.join('Dev', 'build', 'home.html')
    destination_path = os.path.join('index.html')
    
    try:
        # Copy index.html from build folder to root folder
        shutil.copyfile(source_path, destination_path)
        logging.info(f'Copied {source_path} to {destination_path}')
    except FileNotFoundError:
        logging.error(f'The file {source_path} does not exist')
    except Exception as e:
        logging.error(f'An error occurred while copying the file: {e}')


    # Define source and destination paths
    source_path = os.path.join('Dev', 'build', 'contact_page_dev.html')
    destination_path = os.path.join('contact_page.html')
    
    try:
        # Copy index.html from build folder to root folder
        shutil.copyfile(source_path, destination_path)
        logging.info(f'Copied {source_path} to {destination_path}')
    except FileNotFoundError:
        logging.error(f'The file {source_path} does not exist')
    except Exception as e:
        logging.error(f'An error occurred while copying the file: {e}')

    # Define source and destination paths
    source_path = os.path.join('Dev', 'build', 'projects_page_dev.html')
    destination_path = os.path.join('projects_page.html')
    
    try:
        # Copy index.html from build folder to root folder
        shutil.copyfile(source_path, destination_path)
        logging.info(f'Copied {source_path} to {destination_path}')
    except FileNotFoundError:
        logging.error(f'The file {source_path} does not exist')
    except Exception as e:
        logging.error(f'An error occurred while copying the file: {e}')
    
    # Define source and destination paths
    src = 'D:\Project_Hub\WebDev Workspace\CV\Dev\static'
    dst = 'D:\Project_Hub\WebDev Workspace\CV\static'

    # Copy the folder and override if it exists
    try:
        copy_and_override(src, dst)
    except Exception as e:
        print(f"Error: {e}")