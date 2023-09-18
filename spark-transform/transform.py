from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder \
    .appName("OrderTransformation") \
    .getOrCreate()

# Read data from Kafka topic
raw_data = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "order_topic") \
    .load()

# Define schema for the data
schema = ["orderId", "productId", "quantity", "price"]
transformed_data = raw_data.selectExpr("CAST(value AS STRING)").selectExpr(*schema)

# Perform transformations
transformed_data = transformed_data.withColumn("total_price", col("quantity") * col("price"))

# Write transformed data to Postgres
transformed_data.writeStream \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/mydatabase") \
    .option("dbtable", "order_data") \
    .option("user", "myuser") \
    .option("password", "mypassword") \
    .start()

# Start Spark streaming
spark.streams.awaitAnyTermination()
