# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variables
ENV ENV="prod"
ENV FLASK_APP=app
ENV FLASK_ENV=development
ENV PORT=5000
ENV API_ENDPOINT_ACCESS_TOKEN=None

# Run Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.__init__:create_app()"]
