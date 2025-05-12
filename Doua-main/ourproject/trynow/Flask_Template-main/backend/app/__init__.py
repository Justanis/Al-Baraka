from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from .mailer import SMTPMailer
from flask_cors import CORS

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app) 
    app.config.from_object(Config)

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    # Initialize mailer
    mailer = SMTPMailer()
    mailer.init_app(app)
    # Import and register blueprints or routes
    from .routes import api_bp
    app.register_blueprint(api_bp)
    # Store mailer inside app for later use in routes
    app.mailer = mailer 
    

    return app

