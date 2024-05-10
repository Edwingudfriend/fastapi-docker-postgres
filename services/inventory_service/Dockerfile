FROM python:3.9-slim

# Install pip (assuming it's not pre-installed in the base image)
RUN pip install --upgrade pip

# Set the working directory in the container
WORKDIR /app

# Copy the local code to the container
COPY . /app

# Install Poetry
RUN pip install poetry

# Configure Poetry
RUN poetry config virtualenvs.create false

# Install psycopg2-binary
RUN pip install psycopg2-binary

# Install dependencies using Poetry
RUN poetry install --no-dev

# Install curl
RUN apt-get update && apt-get install -y curl

# Download and install Flyway binary using curl
RUN curl -o flyway.tar.gz https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/10.12.0/flyway-commandline-10.12.0-linux-x64.tar.gz && \
    tar -xzf flyway.tar.gz && \
    mv flyway-10.12.0 /usr/local/lib/flyway && \
    ln -s /usr/local/lib/flyway/flyway /usr/local/bin/flyway && \
    rm flyway.tar.gz

# Copy the flyway.conf file into the container
COPY flyway.conf /app/flyway.conf

# Set permissions for the flyway.conf file
RUN chmod a+rwx /app/flyway.conf

# Expose port 80
EXPOSE 8082

# Command to run the application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8082"]