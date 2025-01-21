from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

# Flask-Mail nesnesi oluşturuluyor
mail = Mail()

def create_app():
    app = Flask(__name__)

     # Secret key ayarı
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_default_secret_key')

    # E-posta ayarları yapılandırılıyor
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Gmail SMTP sunucusu
    app.config['MAIL_PORT'] = 587  # SMTP portu
    app.config['MAIL_USE_TLS'] = True  # Güvenli bağlantı için TLS
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # .env'den çekiliyor
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # .env'den çekiliyor
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')  # .env'den çekiliyor

    # Flask-Mail uygulamaya bağlanıyor
    mail.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
