import os

SECRET_KEY = os.getenv("JWT_SECRET_KEY","f8c9d3a4e8b1f2c0d7e6a9b3c4f1e5d2a8c7b6d3e9f2c0a1d5e6b4c3a7f9e8d1")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/email_db")
IMAP_SERVER = "imap.gmail.com"
SMTP_SERVER = "smtp.gmail.com"
