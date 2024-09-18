# Use an official Apache HTTPD image
FROM httpd:2.4

# Install necessary tools
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy the HTML files into the Apache web root
COPY ./html/ /usr/local/apache2/htdocs/
