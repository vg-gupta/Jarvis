from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

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
    app.run()
