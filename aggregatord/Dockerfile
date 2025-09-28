# Dockerfile for aggregatord

# base image
FROM python:3.12.3

# directory name specification
WORKDIR /aggregatord

# dependencies/packages we need to install in our environment
RUN pip install "fastapi[standard]" pydantic requests

# copy everything under my local (/app directory) to container's (/code/app directory)
COPY ./app /aggregatord/app

# Use port 8082
EXPOSE 8082

CMD ["fastapi", "run", "app/main.py", "--port", "8082", "--host", "0.0.0.0"]