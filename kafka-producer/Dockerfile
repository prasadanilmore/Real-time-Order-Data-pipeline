# Use an official Python runtime as a parent image
FROM python:3.8

# Install Kafka Python library
RUN pip install kafka-python

# Copy producer.py into the container
COPY producer.py /producer.py

# Define the command to run your script
CMD ["python", "/producer.py"]
