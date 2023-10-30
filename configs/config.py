import os


class Config:
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/ad_copy'
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

    API_KEY = os.getenv("OPENAI_API_KEY")
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.json'
