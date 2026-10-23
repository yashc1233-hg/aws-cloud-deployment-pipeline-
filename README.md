# AWS DevOps Internship Project: Automated CI/CD to EC2

This beginner project demonstrates automated tests, Docker image packaging, and an optional GitHub Actions deployment to an AWS EC2 virtual machine.

## Folder structure

```text
aws-devops-cicd-internship-project/
├── app.py
├── requirements.txt
├── Dockerfile
├── compose.yaml
├── tests/test_app.py
├── .github/workflows/ci.yml
├── .github/workflows/deploy-ec2.yml
├── infra/ec2-user-data.sh
└── docs/aws-setup.md
```

## Run locally (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe app.py
```

Open http://127.0.0.1:5000 and http://127.0.0.1:5000/health.

## Run with Docker

```powershell
docker compose up --build
```

## Enable AWS deployment

Read `docs/aws-setup.md` before creating resources. You need an AWS account, an EC2 instance with Docker, a Docker Hub account/token, and the GitHub repository secrets listed in the guide. The AWS workflow is a template and will not deploy until you configure and test these prerequisites.

## Workflow

- `ci.yml`: tests the Flask app and verifies a Docker image can build.
- `deploy-ec2.yml`: tests, builds/pushes the image to Docker Hub, and deploys it to EC2 over SSH when secrets are configured.

## Security and cost

Do not commit cloud credentials or private keys. Restrict SSH access, review AWS charges, and stop/terminate resources after the demo if they are no longer needed. This is a learning project, not a production-hardened deployment.
