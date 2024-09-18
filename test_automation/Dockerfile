# Use the Python 3.9 base image
FROM python:3.9-slim

# Install required dependencies
RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Selenium and other Python dependencies
RUN pip install selenium

# Add the test script to the container
COPY test_script.py /app/test_script.py

# Set the working directory
WORKDIR /app

# Run the test script when the container starts
CMD ["python", "test_script.py"]
