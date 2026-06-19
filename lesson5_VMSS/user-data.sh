#!/bin/bash

apt-get update -y
apt-get install python3 python3-pip python3-venv python3-flask -y

mkdir -p /app

cd /app

cat<< 'EOF' > app.py

import socket
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    return f""" 
    <html>
        <body>
            <h1>Azure VM scale sets</h1>
            <h2>Instance: <b>{hostname}</b></h2>
        </body>
    </html>
    """

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run('0.0.0.0', port=80)
EOF

# pip3 install flask --break-system-packages

cat << 'EOF' > /etc/systemd/system/pyapp.service
[Unit]
Description=Python Flask Web Application
After=network.target

[Service]
User=root
WorkingDirectory=/app
ExecStart=/usr/bin/python3 app.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable pyapp.service
systemctl start pyapp.service

    
    