# Use an official Ubuntu base image
FROM ubuntu:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies, Python 3, and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install --trusted-host pypi.python.org -r requirements.txt

# Set environment variable
ENV NAME World

# Change to the docker_project directory
WORKDIR /app/docker_project

# Set the entry point and default command
ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

