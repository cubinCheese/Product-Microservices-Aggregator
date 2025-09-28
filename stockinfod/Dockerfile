# Dockerfile for stockinfod

# base image
FROM python:3.12.3

# directory name specification
WORKDIR /stockinfod

# dependencies/packages we need to install in our environment
RUN pip install "fastapi[standard]" pydantic

# copy everything under my local (/app directory) to container's (/code/app directory)
COPY ./app /stockinfod/app

# Use port 8081
EXPOSE 8081

CMD ["fastapi", "run", "app/main.py", "--port", "8081", "--host", "0.0.0.0"]