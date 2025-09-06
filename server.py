from flask import Flask, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Jarvis is running!"

@app.route("/run")
def run_jarvis():
    # Run your script
    result = subprocess.run(
        ["python", "main2.py"], capture_output=True, text=True
    )
    return jsonify({
        "stdout": result.stdout,
        "stderr": result.stderr
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
