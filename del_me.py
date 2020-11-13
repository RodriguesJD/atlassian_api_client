# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json

url = "https://ripplelabs-dev.atlassian.net/rest/servicedeskapi/organization/8/user"

headers = {
   "Content-Type": "application/json"
}

payload = json.dumps({
    "accountIds": [
        "qm:32ecad55-c5c6-48db-b7f6-04bb0e6b712a:ccd62148-e2e7-4ac8-8dbd-a9538dc17ad6"
    ],
    "usernames": []
}
)

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers
)

print(response.text)