import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head><title>Serverless Python</title></head>
        <body style="font-family:sans-serif; text-align:center; margin-top:100px;">
            <h1>🚀 Deployed on Cloud Run</h1>
            <p>Python running serverless. No server management.</p>
            <button onclick="alert('It works!')">Test JS</button>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))