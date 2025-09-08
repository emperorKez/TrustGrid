# TrustGrid

A Scalable, Real-Time Fraud Detection Microservice API

TrustGrid is a high-performance microservice designed to integrate fraud and anomaly detection into any application. Built with FastAPI, it provides a simple RESTful API to evaluate transactions, user actions, and events for potential risk, returning a calculated trust score and actionable recommendations.

## Features

- **RESTful API**: Simple, standardized JSON-based API for easy integration.
- **Real-Time Evaluation**: Low-latency processing suitable for synchronous workflows (e.g., payment processing).
- **AI-Powered Detection**: Leverages machine learning to identify complex fraud patterns.
- **Versatile Risk Scoring**: Returns a quantitative trust score and qualitative risk level and flags.
- **Framework Agnostic**: Can be consumed by any application—FinTech, E-commerce, Crypto, or Ride-Hailing.
- **Comprehensive Documentation**: Automatic interactive API documentation (Swagger UI and ReDoc).
- **Docker Ready**: Containerized for easy deployment and scaling in microservice architectures.

## Project Structure

The project is organized into a feature-based structure to ensure modularity and scalability.

```
.
├── src
│   ├── __init__.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── celery.py
│   │   ├── constants.py
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   ├── logger.py
│   │   └── utils.py
│   ├── features
│   │   ├── __init__.py
│   │   └── fraud_detection
│   │       ├── __init__.py
│   │       ├── ml
│   │       │   ├── __init__.py
│   │       │   ├── model.py
│   │       │   └── preprocessor.py
│   │       ├── models.py
│   │       ├── router.py
│   │       ├── schemas.py
│   │       └── services.py
│   └── main.py
├── .gitignore
├── LICENSE
└── README.md
```

- **`src/core`**: Contains common modules and utilities shared across the application, such as database connections, logging, and constants.
- **`src/features`**: Each subdirectory within `features` represents a distinct feature of the application (e.g., `fraud_detection`).
  - **`router.py`**: Defines the API endpoints for the feature.
  - **`schemas.py`**: Contains Pydantic models for data validation and serialization.
  - **`services.py`**: Implements the business logic for the feature.
  - **`models.py`**: Defines the database models.
  - **`ml/`**: Contains machine learning specific code, including models and preprocessors.
- **`src/main.py`**: The entry point of the application.

## Getting Started

### Prerequisites

- Python 3.9+
- Poetry (for dependency management)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/TrustGrid.git
   cd TrustGrid
   ```

2. **Install dependencies:**
   ```bash
   poetry install
   ```

## Usage

To run the application, use the following command:

```bash
poetry run uvicorn src.main:app --reload
```

The API documentation will be available at `http://127.0.0.1:8000/docs`.

## Running Tests

To run the test suite, use the following command:

```bash
poetry run pytest
```
