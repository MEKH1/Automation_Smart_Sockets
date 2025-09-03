#Make sure to install pip install tuya-iot-py-sdk 
# Check the ReadMe FILE 

from tuya_connector import TuyaOpenAPI, TUYA_LOGGER

# Your Tuya credentials
ACCESS_ID = "your-access-id"
ACCESS_KEY = "your-access-key"
API_ENDPOINT = "https://openapi.tuyaus.com"  # Change to your region
USERNAME = "your-smartlife-email"
PASSWORD = "your-password"
DEVICE_ID_1 = "your-device-id-1"
DEVICE_ID_2 = "your-device-id-2"

# Initialize API
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

# Function to control a device
def switch_device(device_id, turn_on=True):
    commands = {"commands": [{"code": "switch_1", "value": turn_on}]}
    response = openapi.post(f"/v1.0/iot-03/devices/{device_id}/commands", commands)
    print("Response:", response)

# Example usage:
switch_device(DEVICE_ID_1, True)   # Turn ON socket 1
switch_device(DEVICE_ID_2, False)  # Turn OFF socket 2
