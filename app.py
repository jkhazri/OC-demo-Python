import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    pod_name = os.environ.get("HOSTNAME", "Unknown Pod")
    pod_ip = os.environ.get("POD_IP", "Unknown IP")

    return f"Hello, Kubernetes! I'm running in pod: {pod_name} with IP: {pod_ip}"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
