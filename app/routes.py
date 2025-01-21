from flask import Blueprint, render_template, request, jsonify, redirect, flash, url_for
from flask_mail import Message
from app import mail  # Import the mail object

# Allowed extensions and max file size (25 MB)
ALLOWED_EXTENSIONS = {'mp3'}
MAX_FILE_SIZE = 25 * 1024 * 1024  # 25 MB

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/artists')
def artists():
    return render_template('artists.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/releases')
def releases():
    return render_template('releases.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/demos')
def demos():
    return render_template('demos.html')

# Demo submission route
@main.route('/submit_contact', methods=['POST'])
def submit_contact():
    try:
        print("DEBUG: Inside submit_contact route")  # Debug statement
        
        # Retrieve form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        demo_file = request.files.get('demo')

        print(f"DEBUG: Received form data - Name: {name}, Email: {email}, Message: {message}, File: {demo_file}")  # Debug statement

        # Check for missing fields
        if not name or not email or not message or not demo_file:
            flash('Lütfen tüm alanları doldurun ve MP3 demo dosyanızı ekleyin.', 'warning')
            print("DEBUG: Missing required fields")  # Debug statement
            return redirect(url_for('main.demos'))

        # Check if file is allowed
        if not allowed_file(demo_file.filename):
            flash('Sadece MP3 formatında dosyalar yükleyebilirsiniz.', 'danger')
            print("DEBUG: Invalid file type")  # Debug statement
            return redirect(url_for('main.demos'))

        # Check file size
        demo_file.seek(0, 2)  # Move the cursor to the end of the file
        file_size = demo_file.tell()  # Get file size
        demo_file.seek(0)  # Reset cursor to the beginning
        if file_size > MAX_FILE_SIZE:
            flash('Dosya boyutu 25 MB sınırını aşıyor. Lütfen daha küçük bir dosya yükleyin.', 'danger')
            print(f"DEBUG: File size too large - {file_size} bytes")  # Debug statement
            return redirect(url_for('main.demos'))

        # Create email
        msg = Message(f"New Demo Submission from {name}",
                      recipients=['telvedigital@gmail.com'])  # Change to your email address
        msg.body = f"""
        Name: {name}
        Email: {email}
        Message: {message}
        """

        print("DEBUG: Email body created")  # Debug statement

        # Attach demo file
        msg.attach(demo_file.filename, demo_file.content_type, demo_file.read())
        print(f"DEBUG: Attached file - {demo_file.filename}")  # Debug statement

        # Send email
        mail.send(msg)
        print("DEBUG: Email sent successfully")  # Debug statement

        # Flash success message and redirect
        flash('Demo Submitted Successfuly!', 'success')
        return redirect(url_for('main.demos'))

    except Exception as e:
        print(f"Hata: {e}")  # Print the exception
        flash('An Error Occured! Please Try Again.', 'danger')
        return redirect(url_for('main.demos'))
