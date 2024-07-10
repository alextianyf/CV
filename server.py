from flask import Flask, render_template, request, redirect, url_for
import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

current_year = datetime.datetime.now().year

@app.route("/")
def home():
    return render_template("index.html", year = current_year)


@app.route("/projects")
def get_projects():
    return render_template("projects.html", year = current_year)

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    sender_email = os.environ.get("yunfeitian@uvic.ca")
    receiver_email = os.environ.get("yunfeitian@uvic.ca")
    sendgrid_api_key = os.environ.get("All20160520.")

    email_content = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    
    message = Mail(
        from_email=sender_email,
        to_emails=receiver_email,
        subject="New Contact Form Personal Website Submission",
        plain_text_content=email_content)

    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        sg.send(message)
    except Exception as e:
        app.logger.error(f"Failed to send email: {e}")
        return "Failed to send email. Please try again later.", 500

    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)