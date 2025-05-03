from flask_mail import Mail, Message

class SMTPMailer:
    def __init__(self):
        """Initialize mailer without an app."""
        self.mail = None

    def init_app(self, app):
        """Configure and initialize Flask-Mail with the existing Flask app."""
        app.config['MAIL_SERVER'] = 'smtp.gmail.com'
        app.config['MAIL_PORT'] = 587
        app.config['MAIL_USE_TLS'] = True
        app.config['MAIL_USE_SSL'] = False
        app.config['MAIL_USERNAME'] = 'al.baraka.teamwork@gmail.com'
        app.config['MAIL_PASSWORD'] = 'mpzugpdcadcbkuoa'  # Use App Password, NOT Gmail password
        app.config['MAIL_DEFAULT_SENDER'] = 'al.baraka.teamwork@gmail.com'  # FIXED!

        self.mail = Mail(app)

    def send_email(self, to, subject, body):
        """Send an email using Flask-Mail."""
        if not self.mail:
            raise ValueError("Mail instance is not initialized. Call init_app(app) first.")

        msg = Message(subject, recipients=[to], body=body)
        self.mail.send(msg)
        return "Email sent successfully!"
