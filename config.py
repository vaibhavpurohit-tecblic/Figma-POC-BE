import os
# from sqlalchemy import create_engine
# from sqlalchemy.exc import OperationalError
# from dotenv import load_dotenv

# load_dotenv()


class Config:
    # if os.getenv("ENV") == "dev":
    #     print("Running dev database")
    #     SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/ad_copy'
    # else:
    #     print("Running Prod database")
    #     SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    # if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    #     SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

    # try:
    #     # Create a database engine and attempt to connect
    #     engine = create_engine(SQLALCHEMY_DATABASE_URI)
    #     connection = engine.connect()

    #     # If the connection is successful, print a success message
    #     print("Database connection established.")

    #     # Close the connection
    #     connection.close()
    # except OperationalError as e:
    #     # If there's an error, print an error message
    #     print("Error: Could not connect to the database.")
    #     print(e)
    #     exit()

    # API_KEY = os.getenv("OPENAI_API_KEY")
    # ASSISTANT_ID = "asst_gDLEqS0GBXwg5AJX1sq96PqA"
    # SWAGGER_URL = '/api/docs'
    # API_URL = '/static/swagger.json'
    # API_ENDPOINT_ACCESS_TOKEN = os.getenv("API_ENDPOINT_ACCESS_TOKEN")
    # FILE_KEY = '5N9Is95rRTnY73yhNfEQC5'
    FIGMA_TOKEN = ''
