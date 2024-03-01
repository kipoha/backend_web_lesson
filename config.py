from decouple import config

SECRET_KEY = config("SECRET_KEY")
PASSWORD = config("PASSWORD")
EMAIL = config("EMAIL")