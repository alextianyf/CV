import glob
import os

# Get the directory of the current script: /CV/project-template/
script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the root directory: one level up from the script directory (i.e., /CV/)
root_dir = os.path.dirname(script_dir)

# Define file paths
start_path = os.path.join(script_dir, "projects_template_start.html")
end_path = os.path.join(script_dir, "projects_template_end.html")
project_card_dir = os.path.join(script_dir, "projects")
output_path = os.path.join(root_dir, "projects.html")  

# Generate the final projects.html file
with open(start_path, 'r') as start, open(end_path, 'r') as end, open(output_path, 'w') as out:
    out.write(start.read())

    for file in sorted(glob.glob(os.path.join(project_card_dir, "*.html"))):
        with open(file) as f:
            out.write(f.read())

    out.write(end.read())

print(f"projects.html has been generated at: {output_path}")