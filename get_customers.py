# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json

url = "https://ripplelabs-dev.atlassian.net/rest/servicedeskapi/organization"

headers = {
   "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))