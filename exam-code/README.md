S# Crypto Application

A containerized three-tier application with a frontend, backend service, and MySQL database designed for cryptocurrency data management.

## Project Overview

This project consists of three main components:
- **Frontend**: A Flask web application that serves the user interface
- **Backend**: A Flask API service that handles business logic and database operations
- **Database**: MySQL database for storing cryptocurrency data

The application is containerized using Docker and can be deployed using either Docker Compose or Kubernetes (with Helm support and Istio service mesh integration).

## Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│             │     │             │     │             │
│  Frontend   │────▶│  Backend    │────▶│  MySQL DB   │
│  (Flask)    │     │  (Flask)    │     │             │
│             │     │             │     │             │
└─────────────┘     └─────────────┘     └─────────────┘
```

## Prerequisites

- Docker and Docker Compose (for local development)
- Kubernetes cluster (for production deployment)
- Helm (for Kubernetes package management)
- Istio (for service mesh capabilities)

## Local Development with Docker Compose

### Setup and Run

1. Clone this repository
2. Navigate to the project directory
3. Run Docker Compose:

```bash
docker-compose up -d
```

This will:
- Build and start the frontend service (accessible on port 5002)
- Build and start the backend service (accessible on port 5003)
- Start a MySQL 5.7 database with the crypto_db database

### Environment Variables

The backend service uses the following environment variables:
- `MYSQL_HOST`: MySQL database hostname (default: mysqldb)
- `MYSQL_USER`: MySQL username (default: root)
- `MYSQL_PASSWORD`: MySQL password (default: 123456)

## Kubernetes Deployment

### Using kubectl directly

Apply the Kubernetes manifest files:

```bash
kubectl apply -f fe.yaml
kubectl apply -f be.yaml
kubectl apply -f sql.yaml
```

### Using Helm

The project includes Helm charts for each component:

```bash
# Deploy backend
helm install backend ./charts/be

# Deploy frontend
helm install frontend ./charts/fe

# Deploy MySQL
helm install mysql ./charts/sql
```

### Istio Integration

The project includes Istio configuration for traffic management:

```bash
kubectl apply -f frontend-gateway.yaml
kubectl apply -f frontend-virtualservice.yaml
kubectl apply -f frontend-destination.yaml
```

## Component Details

### Frontend

- Built with Python 3.12 and Flask
- Docker image: `kobi070/fe-exam:latest`
- Exposes port 5002
- Dependencies: Flask, requests

### Backend

- Built with Python 3.12 and Flask
- Docker image: `kobi070/be-exam:latest`
- Exposes port 5001
- Dependencies: Flask, mysql-connector-python, requests, flask-cors

### Database

- MySQL 5.7
- Default database name: crypto_db
- Root password: 123456 (Note: Use secrets in production)

## Helm Charts Configuration

### Backend Chart

```yaml
replicaCount: 2
image:
  repository: kobi070/be-exam
  pullPolicy: Always
  tag: "latest"
service:
  type: ClusterIP
  port: 5001
```

### Frontend Chart

```yaml
replicaCount: 2
image:
  repository: kobi070/fe-exam
  pullPolicy: Always
  tag: "latest"
service:
  type: LoadBalancer
  port: 5002
```

### MySQL Chart

```yaml
replicaCount: 1
image:
  repository: mysql
  tag: "5.7"
  pullPolicy: IfNotPresent
service:
  type: ClusterIP
  port: 3306
mysql:
  rootPassword: "123456"
  database: "crypto_db"
```

## Project Structure

```
.
├── docker/                 # Docker configurations
│   ├── be/                 # Backend service
│   │   ├── Dockerfile          
│   │   ├── requirements.txt    # Backend dependencies
│   │   └── src/                # Backend source code
│   ├── fe/                 # Frontend service
│   │   ├── Dockerfile          
│   │   ├── requirements.txt    # Frontend dependencies
│   │   └── src/                # Frontend source code
│   └── docker-compose.yaml # Docker Compose configuration
├── helm/                   # Helm charts
│   ├── be/                 # Backend chart
│   ├── fe/                 # Frontend chart
│   └── sql/                # MySQL chart
├── istio/                  # Istio configurations
│   ├── frontend-destination.yaml  # Istio destination rule
│   ├── frontend-gateway.yaml      # Istio gateway configuration
│   └── frontend-virtualservice.yaml # Istio virtual service
└── k8s/                    # Kubernetes manifests
    ├── be.yaml             # Backend Kubernetes manifest
    ├── fe.yaml             # Frontend Kubernetes manifest
    └── sql.yaml            # MySQL Kubernetes manifest
```
