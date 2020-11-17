# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os
# todo refactor page

username = os.environ["WORK_EMAIL"]
base_url = os.environ["DEV_JIRA_BASE_URL"]
key = os.environ["DEV_JIRA_KEY"]


def create_user():
    url = f"{base_url}/rest/api/3/user"

    auth = HTTPBasicAuth(username, key)

    headers = {
       "Accept": "application/json",
       "Content-Type": "application/json"
    }

    payload = json.dumps( {
      "password": "abracadabra",
      "emailAddress": "fakeUser@fake.com",
      "displayName": "fake user",
      "name": ""
    } )

    response = requests.request(
       "POST",
       url,
       data=payload,
       headers=headers,
       auth=auth
    )
    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))


def create_group(group_name_to_create):
    url = f"{base_url}/rest/api/3/group"

    auth = HTTPBasicAuth(username, key)

    headers = {
       "Accept": "application/json",
       "Content-Type": "application/json"
    }

    payload = json.dumps({
        "name": f"{group_name_to_create}"
    })

    response = requests.request(
       "POST",
       url,
       data=payload,
       headers=headers,
       auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

