import os
from flask import Flask, redirect, request
import requests
import urllib.parse

app = Flask(__name__)

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = os.environ.get("GOOGLE_REDIRECT_URI")

@app.route('/')
def index():
    return "Backend Python + Composio Cloud Run OK!"

@app.route('/auth/google')
def google_auth_start():
    scope = "openid email https://www.googleapis.com/auth/cloud-platform"
    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": scope,
        "access_type": "offline",
        "prompt": "consent"
    }
    url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode(params)
    return redirect(url)

@app.route('/auth/callback')
def google_auth_callback():
    code = request.args.get("code")
    if not code:
        return "Code is missing", 400

    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code"
    }

    resp = requests.post(token_url, data=data)
    if resp.status_code == 200:
        tokens = resp.json()
        return f"Autenticação concluída com sucesso!<br><pre>{tokens}</pre>"
    else:
        return f"Erro ao trocar código: {resp.text}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
