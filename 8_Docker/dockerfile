#Use an official Python runtime s parent image
FROM python:3.8-slim

# Set the Working directory in the container
WORKDIR /app

# Copy the current directory contents into the container ar /app
COPY . /app

#  Install any neede pakages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container0
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run the Flask app
CMD ["flask","run","--host=0.0.0.0","--port=5000"]