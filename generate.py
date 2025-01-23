import os

# Building a reading template
def load_template(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return ''
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return ''

# Ensure the generated file folder exsits
os.makedirs('pages', exist_ok=True)

'''
@objective: Loading header, contact, footer for public page HTML
'''
header_content = load_template('templates/header.html')
contact_content = load_template('templates/contact.html')
footer_content = load_template('templates/footer.html')

'''
@objective: Loading Home Page HTML Content
'''
# Read the home page desired section
navbar_content = load_template('templates/home-page/navbar.html')
profile_content = load_template('templates/home-page/profile.html')
aboutme_content = load_template('templates/home-page/aboutme.html')
skills_content = load_template('templates/home-page/skills.html')
projects_content = load_template('templates/home-page/projects.html')

placeholders = {
    '{{ nav-bar }}': navbar_content,
    '{{ profile }}': profile_content,
    '{{ aboutme }}': aboutme_content,
    '{{ skills }}': skills_content,
    '{{ projects }}': projects_content,
    '{{ contact }}': contact_content,
    '{{ footer }}': footer_content,
}

home_page_base = load_template('templates/home-page/base.html')
home_page = home_page_base.replace('{{ header }}', header_content)

for placeholder, content in placeholders.items():
    home_page = home_page.replace(placeholder, content)

with open('index.html', 'w', encoding='utf-8') as f:
        f.write(home_page)
print(f"Generated: homepage")

'''
@objective: Loading Project Page HTML Content
'''
navbar_content = load_template('templates/projects-page/navbar.html')
profile_content = load_template('templates/projects-page/profile.html')
content_content = load_template('templates/projects-page/content.html')

placeholders = {
    '{{ nav-bar }}': navbar_content,
    '{{ profile }}': profile_content,
    '{{ content }}': content_content,
    '{{ footer }}': footer_content,
}

projects_page_base = load_template('templates/projects-page/base.html')
projects_page = projects_page_base.replace('{{ header }}', header_content)

for placeholder, content in placeholders.items():
    projects_page = projects_page.replace(placeholder, content)

with open('projects_page.html', 'w', encoding='utf-8') as f:
        f.write(projects_page)
print(f"Generated: projects_page")

'''
@objective: Loading Contact Page HTML Content
'''
navbar_content = load_template('templates/contact-page/navbar.html')
profile_content = load_template('templates/contact-page/profile.html')

placeholders = {
    '{{ nav-bar }}': navbar_content,
    '{{ profile }}': profile_content,
    '{{ contact }}': contact_content,
    '{{ footer }}': footer_content,
}

contact_page_base = load_template('templates/contact-page/base.html')
contact_page = contact_page_base.replace('{{ header }}', header_content)

for placeholder, content in placeholders.items():
    contact_page = contact_page.replace(placeholder, content)

with open('contact_page.html', 'w', encoding='utf-8') as f:
        f.write(contact_page)
print(f"Generated: contact_page")