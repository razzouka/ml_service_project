# ml_service_project

# ML Service MVP

A scalable machine learning service that allows users to upload models, run predictions through a REST API, and pay for successful requests using an internal credit system.

## Project overview

The goal of this project is to develop a scalable ML service that provides prediction functionality based on uploaded machine learning models, while automatically charging internal credits for each successful request.The project was implemented as a university assignment and includes authentication, billing, monitoring, testing, and API documentation.

## Functional requirements

The system includes the following functional blocks:

- User management: registration, authentication with JWT, and personal account management.
- ML functionality: uploading Scikit-learn models and running predictions through the API.
- Billing: tracking user credit balance and charging credits for successful prediction requests.
- Analytics: dashboard for displaying service usage and credit consumption statistics.
- API: REST API with automatic Swagger/OpenAPI documentation.

## Technology stack

The project uses the following technologies:

- **Language:** Python.
- **Framework:** FastAPI.
- **ML:** Scikit-learn.
- **Database:** PostgreSQL.
- **Containerization:** Docker, Docker Compose.
- **Monitoring:** Prometheus and Grafana.
- **Testing:** Pytest with code coverage above 70%.

## Architecture

The service is organized into several core modules.

- **Authentication module** handles user registration, login, and JWT-based authorization.
- **Prediction module** accepts uploaded models and performs inference requests through the API.
- **Billing module** manages credit transactions and deducts credits after successful predictions.
- **Promo code module** implements Option A from the brief by allowing users to redeem promo codes with activation limits and expiration dates.
- **Monitoring module** exposes metrics for Prometheus and visualizes them through Grafana.

## Implemented features

The following features were implemented in the MVP:

- User registration and login with JWT authentication.
- Model upload and storage.
- Prediction requests using uploaded ML models.
- Internal credit balance tracking.
- Credit deduction for successful prediction requests.
- Promo code activation with validation of expiration date and usage limits.
- Swagger/OpenAPI API documentation.
- Docker Compose deployment.
- Prometheus and Grafana integration.
- Automated tests with coverage above 70%.

## Project structure

An example project structure is shown below:

```text
ml_service/
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   └── services/
├── dashboard/
├── tests/
├── docker-compose.yml
├── Dockerfile
├── prometheus.yml
├── requirements.txt
└── README.md
```

## Setup and run

Clone the repository and move to the project directory:

```bash
git clone <repository_url>
cd ml_service
```

Create and activate a virtual environment if needed:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project with Docker Compose:

```bash
docker compose up --build
```

According to the acceptance criteria, the project should be runnable with a single Docker Compose command.

## Environment variables

Create a `.env` file and define the required environment variables, for example:

```env
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/ml_service
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

The brief explicitly recommends using environment variables for secrets and database credentials.

## API documentation

After startup, the API documentation is available through Swagger/OpenAPI.

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Monitoring

The project includes monitoring with Prometheus and Grafana as required by the brief.

- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000`

These tools are used to collect and visualize service metrics.

## Testing

The project includes unit tests with code coverage above 70%, which is one of the acceptance criteria.

Run tests:

```bash
python -m pytest -q
```

Run tests with coverage:

```bash
python -m pytest --cov=app --cov-fail-under=70
```

Current result:

- 9 tests passed.
- Total coverage: 85.38%, which satisfies the project requirement.

## Acceptance criteria status

| Criterion | Status |
|---------|--------|
| JWT authentication works correctly | Done |
| Billing subsystem deducts credits correctly | Done |
| ML model integration works | Done |
| Swagger documentation is available | Done |
| Project starts with Docker Compose | Done |
| Monitoring with Grafana is configured | Done |
| Test coverage above 70% | Done, 85.38% |
| Short business plan included | Done |

## Business plan

### Unique value proposition

This project provides a scalable ML service that allows users to upload machine learning models, run predictions through an API, and pay only for successful requests using an internal credit system.

### Target audience

The service is aimed at students, developers, and small teams who need a simple way to deploy and use machine learning models without building a full production ML infrastructure from scratch. It is especially suitable for educational use, prototyping, and small-scale internal services.

### Problem statement

Many users can train a machine learning model locally, but they do not have a convenient platform for secure access management, prediction execution, billing logic, and service monitoring in one integrated system. This project solves that problem by combining these components into a single platform.

### Monetization model

The project follows a credit-based monetization model. Users receive or purchase internal credits, and each successful prediction request consumes a fixed amount of credits. As part of Option A from the brief, promo codes are used as a marketing mechanism to grant bonus credits or discounts under controlled conditions such as expiration date and limited activation count.

### Simplified financial model

For an educational MVP, the financial model is simplified and focuses on the main business logic rather than detailed market forecasting. Revenue is generated through balance top-ups that allow users to purchase internal credits for prediction requests. The main cost categories include server infrastructure, database and storage support, monitoring tools, and maintenance time. A reasonable pilot scenario for such a service is a small user group of 20 to 50 active users in the first stage, which is sufficient to demonstrate the viability of the billing model and usage tracking.

### Competitive advantage

The main advantage of the project is that it combines machine learning inference, authentication, billing, promo code support, monitoring, and API documentation in one lightweight educational MVP. This makes it more complete than a simple prediction demo and better aligned with real service architecture principles.

## Conclusion

The developed ML Service MVP satisfies the core technical and business requirements described in the project brief. It demonstrates how a machine learning prediction service can be combined with authentication, billing, promotional mechanics, monitoring, and automated testing in a scalable architecture.
