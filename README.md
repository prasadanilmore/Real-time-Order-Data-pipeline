# Real-Time Order Data Pipeline

This project implements a real-time data engineering pipeline for handling order data. It uses Kafka for data ingestion, Apache Spark for data transformation, and PostgreSQL for data storage. The entire pipeline is orchestrated using Apache Airflow.

## Project Structure

The project is structured as follows:

- `kafka-producer/`: Contains the Kafka producer script and Dockerfile.
- `spark-transform/`: Contains the Spark transformation script and Dockerfile.
- `airflow-dag/`: Contains the Apache Airflow DAG definition and Dockerfile.
- `postgres/`: Contains utility scripts for PostgreSQL.
- `order.csv`: Sample order data in CSV format.
- `docker-compose.yml`: Docker Compose file to orchestrate the services.
- `README.md`: This documentation.

## Prerequisites

Before running the project, make sure you have the following installed:

- Docker
- Docker Compose

## How to Run

Follow these steps to set up and run the project:

1. Clone this repository to your local machine.

2. Navigate to the project directory:

   ```bash
   cd real-time-order-data-pipeline

3. Build the Docker images and start the services using Docker Compose:
   ```bash
   docker-compose up --build
## Accessing the Apache Airflow Web UI

To access the Apache Airflow web UI, follow these steps:

1. Open a web browser.

2. Navigate to [http://localhost:8080](http://localhost:8080).

You can use the Airflow web UI to monitor the status of your pipeline and trigger it manually.

### Triggering the Data Pipeline

In the Airflow web UI, you can manually trigger the `order_data_pipeline` DAG to start the data pipeline.

## Sample Output

Here's what you can expect in terms of output and results:

- **Kafka Producer** (kafka-producer/producer.py): This component reads data from `order.csv` and produces messages to the `order_topic` Kafka topic. You will see logs in the terminal indicating the successful production of messages.

- **Spark Transformation Job** (spark-transform/transform.py): This component reads data from the `order_topic` Kafka topic, processes it (calculates the total price), and writes it to the PostgreSQL database. You will see logs in the terminal indicating the processing of data.

- **PostgreSQL Database**: You can query the `order_data` table in the PostgreSQL database to view the transformed data. You can use tools like `psql` or a database client to connect to the database and run SQL queries.

- **Airflow Web UI**: In the Apache Airflow web UI, you can monitor the progress of the DAG execution, check logs, and trigger manual runs.

## Configuration

You can customize various configurations by modifying the relevant configuration files and environment variables. These configurations include Kafka settings, Spark settings, and database connection details. Refer to the respective component directories for configuration files.

   
