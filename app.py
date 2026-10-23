from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return """
    <!doctype html><html lang="en"><head><meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>AWS DevOps CI/CD Demo</title>
    <style>
      body{font-family:Arial,sans-serif;background:#0f172a;color:#f8fafc;margin:0}
      main{max-width:760px;margin:10vh auto;padding:24px}
      section{background:#1e293b;border:1px solid #334155;border-radius:18px;padding:28px}
      h1{color:#38bdf8}.pill{background:#064e3b;color:#a7f3d0;padding:7px 12px;border-radius:20px}
      a{color:#67e8f9}
    </style></head><body><main><section>
    <span class="pill">Demo application</span><h1>AWS DevOps CI/CD Pipeline</h1>
    <p>This sample app is containerized with Docker and can be deployed to an AWS EC2 instance by GitHub Actions.</p>
    <p>Health endpoint: <a href="/health">/health</a></p>
    <p>Cloud deployment must be configured and tested in your own AWS account.</p>
    </section></main></body></html>
    """

@app.get("/health")
def health():
    return jsonify(status="ok", service="aws-devops-cicd-demo"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
