FROM ubuntu:latest
WORKDIR /app
COPY requirements.txt /app
COPY docker_project /app
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install -r requirements.txt && \
    cd docker_project

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
