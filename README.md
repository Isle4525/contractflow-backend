# Payouts Modular Monolith

## Overview
Payouts Modular Monolith is a Django-based application designed to manage complex payout workflows. It follows a **Modular Monolith** architecture, which allows for a clean separation of concerns between different business domains while maintaining the operational simplicity of a single deployment unit.

## Architecture
The system is divided into several independent modules (Django apps), each responsible for a specific domain:

- **IAM (Identity and Access Management)**: Handles user authentication, authorization, roles, and permissions.
- **Contracts**: Manages legal agreements and contract terms for entities receiving payouts.
- **Documents**: Centralized storage and management for supporting documentation and attachments.
- **Payments**: The core engine responsible for calculating, processing, and tracking payout transactions.
- **Submissions**: Manages the intake and validation of payout requests.
- **Tasks**: Handles workflow orchestration, task assignments, and approval processes.
- **Notifications**: Manages multi-channel alerts and system communications.

## Tech Stack
- **Framework**: [Django](https://www.djangoproject.com/)
- **API**: [Django REST Framework](https://www.django-rest-framework.org/)
- **Database**: [PostgreSQL 15](https://www.postgresql.org/)
- **Environment**: [python-dotenv](https://github.com/theskumar/python-dotenv)
- **Containerization**: [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)

## Prerequisites
- Python 3.10+
- Docker & Docker Compose
- PostgreSQL (if running locally without Docker)

## Getting Started

### 1. Clone and Prepare
```bash
git clone <repository-url>
cd payouts-modular-monolith
```

### 2. Environment Configuration
Copy the example environment file and adjust the values as needed:
```bash
cp .env.example .env
```

### 3. Database Setup (Docker)
The easiest way to start the database is using Docker Compose:
```bash
docker-compose up -d postgres
```

### 4. Local Development Environment
Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install django djangorestframework python-dotenv psycopg2-binary
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Start the Application
```bash
python manage.py runserver
```

## Docker Deployment
To run the full stack (App + DB) in Docker:
```bash
# Ensure you have a Dockerfile (not currently present in the repo)
docker-compose up --build
```

## Project Structure
```text
├── config/              # Project configuration and settings
├── contracts/           # Contract management module
├── documents/           # Document management module
├── iam/                 # Identity and Access Management
├── notifications/       # Notification services
├── payments/            # Payout processing engine
├── submissions/         # Payout request submissions
├── tasks/               # Workflow and task management
├── manage.py            # Django management script
└── docker-compose.yml   # Docker services definition
```


