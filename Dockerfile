# Base on offical Python Alpine image
FROM python:3.11-alpine

# Set working directory
WORKDIR /usr/app
RUN adduser --system --no-create-home nonroot

# Copy package.json and package-lock.json before other files
# Utilise Docker cache to save re-installing dependencies if unchanged
COPY ./requirements ./requirements

# Install pnpm
RUN pip install -r ./requirements/requirements.txt

# Copy all files
COPY ./ ./

# Expose the listening port
# EXPOSE 3000

# Run container as non-root (unprivileged) user
USER nonroot

# Run npm start script with PM2 when container starts
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]