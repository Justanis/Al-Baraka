import os

class Config:
    # MS SQL Server connection string (update with your details)
    SQLALCHEMY_DATABASE_URI = (
    "mssql+pyodbc://@localhost/Baraka?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Other configuration variables can be added here
    SECRET_KEY = 'your-secret-key'


    # MAILER CONFIG
    EMAIL = 'example.com'
    MAILERAPPPASSWORD = 'yikbylkylwanbdwx'
