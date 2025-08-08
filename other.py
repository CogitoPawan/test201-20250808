anomaly-detection/
├── anomaly_detector/
│   ├── __init__.py
│   ├── detector.py
│   └── utils.py
├── api/
│   ├── __init__.py
│   ├── app.py
│   └── endpoints.py
├── config.py
├── requirements.txt
├── run.py
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_detector.py
└── README.md

Flask==2.2.2
fastapi==0.92.0
uvicorn==0.20.0
SQLAlchemy==1.4.41
psycopg2-binary==2.9.5
redis==4.4.0
requests==2.28.1
scikit-learn==1.1.2
pandas==1.4.2
azure-cognitiveservices-vision-customvision==3.1.0

# Anomaly Detection System

## Overview

This project is designed to detect anomalies in weekly sales data utilizing a microservices architecture with FastAPI and Flask for API endpoints. It employs an Isolation Forest algorithm to detect anomalies in the data.

## Architecture

1. **Microservices Architecture**.
2. **Automated CI/CD Pipeline** using Azure DevOps.
3. **Cloud-native Services** with Azure Cognitive Services.
4. **Scalable Data Infrastructure** with PostgreSQL and Redis.
5. **Security Best Practices** with OAuth 2.0 and JWT.
6. **Observability and Monitoring** with Application Insights and Log Analytics.

## Setup Instructions

1. **Clone the repository:**

2. **Create a Virtual Environment:**

3. **Install dependencies:**

4. **Run the application:**

5. **Access the API:**
    Open your browser or use a tool like Postman to access [http://localhost:5000/api](http://localhost:5000/api)

## Testing

1. **Run the tests:**

## API Endpoints

- `GET /` - Root endpoint
- `POST /api/detect-anomalies` - Detect anomalies in the provided data

## Configuration

The configuration is managed through environment variables:

- `SECRET_KEY` - Secret key for the application
- `DATABASE_URL` - URL of the PostgreSQL database
- `REDIS_URL` - URL of the Redis instance
- `COGNITIVE_SERVICES_API_KEY` - API key for Azure Cognitive Services