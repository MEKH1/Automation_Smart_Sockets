
Smart Life = Tuya Cloud = Tuya API

You can control your smart sockets using Tuya's cloud API or local API (local API is trickier and needs more setup).

Control Tuya Smart Plugs via Cloud (Using Python)

This is the easiest and most stable method.

Step 1: Create a Tuya Developer Account

Go to https://iot.tuya.com

Sign up or log in.

Create a Cloud Project.

Choose Smart Home industry.

Set Data Center closest to your location.

Enable Device Status Notification.

Link your Tuya Smart app account to this project (under Link Devices > App > QR code).

Copy down:

Access ID (API Key)

Access Secret

Your device IDs (from the Devices tab in the project)

Step 2: Install Tuya Python SDK
pip install tuya-iot-py-sdk



