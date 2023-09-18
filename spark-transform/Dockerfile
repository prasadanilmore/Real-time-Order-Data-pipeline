# Use an official Spark runtime as a parent image
FROM apache/spark:3.1.2

# Copy transform.py into the container
COPY transform.py /transform.py

# Define the command to run your script
CMD spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 /transform.py
