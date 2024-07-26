# Kafka Web Scraping and REST API Example
a Dockerized solution for integrating Kafka with web scraping and REST API services.

This repository provides a complete example of using Kafka for data streaming, integrating web scraping with Kafka producers, and building a RESTful API to access and query stored data. It includes scripts and configurations for the following tasks:

- Installing Kafka using Docker.
- Creating Kafka topics using Kafka CLI commands.
- Sending messages to Kafka topics using Kafka CLI commands.
- Consuming messages from Kafka topics using Kafka CLI commands.
- Implementing a Python script to scrape data from a web page and publish it to a Kafka topic in JSON format at 1-second intervals.
- Saving the data written to the Kafka topic into a file.
- Developing a REST API service (using Flask or FastAPI) to access and query the saved data from the file.
- Dockerizing the entire application for easy deployment and scalability.
- 
## Setup Instructions

### Prerequisites

- Docker installed on your machine.
- Python 3.x installed (for running the web scraping script).

### Installation and Usage

1. **Install Kafka using Docker:**

   ```bash
   docker-compose up -d
