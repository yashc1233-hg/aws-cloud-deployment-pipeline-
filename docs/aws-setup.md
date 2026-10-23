# AWS EC2 setup and deployment

## Architecture

Developer -> GitHub repository -> GitHub Actions (tests + Docker build) -> Docker Hub image registry -> SSH deployment -> AWS EC2 instance -> Flask app on port 5000.

## AWS setup (manual, verify in your own account)

1. In AWS Console, choose EC2 and launch an Amazon Linux 2023 instance.
2. Create/download a key pair and store the private key safely. Never commit it.
3. Configure the security group:
   - SSH (TCP 22): restrict source to your own IP wherever possible.
   - Custom TCP 5000: allow only the audience that needs to view the demo; remove this rule after the presentation or use a reverse proxy/TLS for a longer-lived deployment.
4. Use `infra/ec2-user-data.sh` as user data, or SSH into the instance and install Docker:
   `sudo dnf update -y && sudo dnf install -y docker && sudo systemctl enable --now docker && sudo usermod -aG docker ec2-user`
   Reconnect after changing group membership.
5. Test SSH and Docker on the instance before configuring GitHub Actions.

## GitHub Actions repository secrets

Add these in GitHub repository -> Settings -> Secrets and variables -> Actions -> New repository secret:

- `DOCKERHUB_USERNAME`: your Docker Hub username
- `DOCKERHUB_TOKEN`: a Docker Hub access token (not your account password)
- `EC2_HOST`: public IPv4 address or DNS of the EC2 instance
- `EC2_USER`: normally `ec2-user` for Amazon Linux
- `EC2_SSH_KEY`: entire private key file content (keep it secret; never commit it)

Then run the `Deploy to AWS EC2` workflow from the Actions tab. It runs tests, builds and pushes an image to Docker Hub, connects to EC2 by SSH, and replaces the running container.

## Validation

Open `http://EC2_PUBLIC_IP:5000/` and `http://EC2_PUBLIC_IP:5000/health`. The EC2 security group must allow TCP 5000 for your source IP. Do not say the cloud deployment is complete until you see the app working from the browser and the workflow has succeeded.

## Cost and security cautions

- EC2 can incur charges depending on instance type, region, and account eligibility. Check current AWS pricing and Free Tier eligibility before launching; stop or terminate resources after the demo if no longer needed.
- Restrict SSH to your IP. Avoid opening port 5000 to the whole internet unless necessary for a short demo.
- This SSH-based learning setup is not a hardened production architecture. For a more secure production pipeline, consider GitHub Actions OIDC with AWS IAM, Amazon ECR, and ECS/App Runner, plus HTTPS and monitoring.
