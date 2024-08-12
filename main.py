import requests

# Define your OpenHAB server address and port
openhab_url = 'http://localhost:8080'  # Update with the actual URL of your OpenHAB server.

# Define the item name you want to control
item_name = 'SpotifyThing'  # Replace with your actual item name from OpenHAB.

# Define the command you want to send to the item
command = 'ON'  # This could be 'OFF', 'UP', 'DOWN', '1', '0', etc., depending on your setup.

# Construct the full URL to send the command
url = f'{openhab_url}/rest/items/{item_name}'

# Send the command to the item using a PUT request
response = requests.post(url, data=command, headers={'Content-Type': 'text/plain'})

# Check the response from the server
if response.status_code == 200:
    print(f'Successfully sent command {command} to {item_name}')
else:
    print(f'Failed to send command {command} to {item_name}. Status code: {response.status_code}')
    print('Response:', response.text)

