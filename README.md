📌 Flask Frontend & Backend with Item Management

This project is a simple Flask-based frontend and backend for managing a list of items.
It includes:

- A frontend UI that fetches and displays items from a backend.
- A Flask backend that acts as a proxy to another backend API for storing items.
- CORS handling for cross-origin requests.



## Features

- Kubernetes deployment for each tier.
- Service discovery using Kubernetes Services.
- Persistent storage for database components.
- Security best practices (RBAC, Network Policies, etc.).

## Prerequisites

Before deploying the application, ensure you have the following installed:

- Kubernetes cluster (Minikube, EKS, AKS, GKE, etc.)
- kubectl CLI
- Docker (for containerization)

## Deployment Steps

1. **Clone the Repository:**
   ```sh
   git clone git@github.com:esther1Tech/k8s-project-three-tier-application.git
   cd k8s-project-three-tier-application
   ```

2. **Deploy the Database Layer:**
   ```sh
   kubectl apply -f k8s/database/
   ```

3. **Deploy the Backend API:**
   ```sh
   kubectl apply -f k8s/backend/
   ```

4. **Deploy the Frontend Application:**
   ```sh
   kubectl apply -f k8s/frontend/
   ```

5. **Verify Deployments:**
   ```sh
   kubectl get pods,services,deployments
   ```

## Configuration

- Modify environment variables in `k8s/config`.
- Update service configurations in `k8s/` YAML files.

## Cleanup

To remove all deployed resources, run:
```sh
kubectl delete -f k8s/
```
