from kafka import KafkaProducer
import csv

# Kafka broker configuration
kafka_broker = 'kafka:9092'  # Use the service name 'kafka' as it will be the hostname inside Docker.

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers=kafka_broker)

# Read data from CSV and produce to Kafka topic
with open('/data/order.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        message = f"{row['orderId']},{row['productId']},{row['quantity']},{row['price']}"
        producer.send('order_topic', value=message.encode('utf-8'))

# Close Kafka producer
producer.close()
