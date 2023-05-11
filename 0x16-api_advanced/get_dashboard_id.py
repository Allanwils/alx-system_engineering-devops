#!/usr/bin/python3


"""
Get dashboard ID
"""

import json
import os
import requests

# Set the API and application keys
api_key = '98eaee3dc0dc94c55969c6a54901a8b0'
app_key = '074582b966f5a28d7f893e919e61a177d8e939ba'

# Set the dashboard filter
dashboard_filter = '2-setup_datadog'

# Set the request URL
url = 'https://api.datadoghq.com/api/v1/dashboard'

# Set the curl command
curl_command = f"curl -X GET -H 'Content-type: application/json' \
                -H 'DD-API-KEY: {api_key}' -H 'DD-APPLICATION-KEY: {app_key}' \
                'https://api.datadoghq.com/api/v1/dashboard?filter={dashboard_filter}'"

# Execute the curl command and retrieve the response
response = os.popen(curl_command).read()

# Parse the response as JSON
response_json = json.loads(response)

# Check if at least one dashboard was found
if response_json['total'] > 0:
    # Extract the ID of the first matching dashboard
    dashboard_id = response_json['dashboards'][0]['id']
    print(f"The ID of the dashboard {dashboard_filter} is {dashboard_id}")
else:
    print("Dashboard not found.")
