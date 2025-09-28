# Dockerfile for iteminfod

# base image
FROM python:3.12.3

# directory name specification
WORKDIR /iteminfod

# dependencies/packages we need to install in our environment
RUN pip install "fastapi[standard]" pydantic

# copy everything under my local (/app directory) to container's (/code/app directory)
COPY ./app /iteminfod/app

# Use port 8080
EXPOSE 8080

CMD ["fastapi", "run", "app/main.py", "--port", "8080", "--host", "0.0.0.0"]