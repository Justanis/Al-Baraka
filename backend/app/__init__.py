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
    app = Flask(__name__) # create Flask app
    CORS(app) # Enable CORS for all routes
    app.config.from_object(Config) # Load configuration from Config class

    # Initialize extensions with app
    db.init_app(app) # Bind SQLAlchemy to app
    migrate.init_app(app, db) # Bind migration tool to app and db

    # Initialize mailer
    mailer = SMTPMailer() # Create instance of my custom mailer
    mailer.init_app(app) # Initialize it with app configuration
    # Import and register blueprints or routes
    from .routes import api_bp
    app.register_blueprint(api_bp)
    
    # Store mailer inside app for later use in routes
    app.mailer = mailer 
    

    return app

