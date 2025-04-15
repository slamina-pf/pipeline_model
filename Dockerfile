FROM apache/airflow:2.7.3

ENV DOCKER_WATCH=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create scripts directory with correct permissions
RUN mkdir -p /scripts && chown airflow:root /scripts

# Switch to airflow user
USER airflow

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy init script (ensure LF line endings, not CRLF)
COPY --chmod=+x scripts/init.sh /scripts/init.sh

ENTRYPOINT ["/scripts/init.sh"]