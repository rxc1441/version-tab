# Stage 1: Build Stage
# Use a full Python image for building, as it contains tools needed for pip.
FROM python:3.9-slim-buster as builder

# Set the working directory inside the container for this stage.
WORKDIR /app

# Copy only the requirements file first to leverage Docker's build cache.
# If requirements.txt doesn't change, this layer won't be rebuilt.
COPY requirements.txt .

# Install dependencies in a virtual environment.
# This makes the environment self-contained and avoids system-wide installs.
# We also clean up pip cache to keep the image size small.
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt && \
    /opt/venv/bin/pip install uvicorn

# Stage 2: Production Stage
# Use a smaller base image for the final production image.
# This reduces the final image size and attack surface.
FROM python:3.9-slim-buster

# Set the working directory inside the container for this stage.
WORKDIR /app

# Copy the virtual environment from the builder stage.
# This ensures all dependencies are present without needing to reinstall.
COPY --from=builder /opt/venv /opt/venv

# Set the PATH to include the virtual environment's bin directory.
# This allows the container to find commands like 'uvicorn' without specifying full path.
ENV PATH="/opt/venv/bin:$PATH"

# Copy the application code and static files.
# The '.' copies everything from the current host directory (where Dockerfile is)
# into the /app directory in the container.
COPY . .

# Expose the port your FastAPI application will listen on.
# This signals to Docker that the container uses this port.
EXPOSE 8000

# Define the command to run when the container starts.
# This command starts your FastAPI application using uvicorn.
# '--host 0.0.0.0' makes the server accessible from outside the container.
# '--port 8000' specifies the port it listens on.
# We explicitly avoid --reload for production as it's for development.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
