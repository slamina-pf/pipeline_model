#!/bin/bash
# scripts/init.sh

# Initialize the database
airflow db init

# Create an admin user
airflow users create \
    --username admin \
    --password admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com

# Start the scheduler in the background
airflow scheduler &

# Start the webserver in the foreground
exec airflow webserver