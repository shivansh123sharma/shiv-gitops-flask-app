# shiv-gitops-flask-app
production grade flask microservice ci-cd pipeline

This repository demonstrates a modern DevOps approach to deploying a Flask application. It utilizes Docker for containerization and GitHub Actions for continuous integration, ensuring a seamless flow from code to deployment.

---

## 🛠️ Tech Stack
* **Framework:** Flask (Python)
* **WSGI Server:** Gunicorn
* **Containerization:** Docker
* **CI/CD:** GitHub Actions
* **GitOps Workflow:** Automated builds and deployment triggers

---

## 📂 Project Structure
* `app.py`: Core application logic and API routes.
* `Dockerfile`: Multi-stage build for optimized production images.
* `.github/workflows/ci.yml`: Automated testing and container build pipeline.
* `templates/`: UI components for the web interface.
* `requirements.txt`: Managed dependencies (pinned versions for stability).

---

## 🚀 Quick Start

### 1. Local Environment
```bash
# Clone the repo
git clone [https://github.com/shivansh123sharma/shiv-gitops-flask-app.git](https://github.com/shivansh123sharma/shiv-gitops-flask-app.git)
cd shiv-gitops-flask-app

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py


2. Docker Setup (Production Mode)
Bash
# Build the image
docker build -t flask-microservice:latest .

# Run the container
docker run -p 5000:5000 flask-microservice:latest


 CI/CD Pipeline
The integrated GitHub Actions workflow performs the following on every push to main:

Linting: Checks Python code for PEP 8 compliance.

Dependency Check: Scans requirements.txt for security vulnerabilities.

Build: Validates the Docker build process.

Test: Executes unit tests to ensure application stability.

