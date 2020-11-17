import os

import requests
from requests.auth import HTTPBasicAuth


class PutAtlassian:
    username = os.environ["WORK_EMAIL"]
    key = os.environ["DEV_JIRA_KEY"]
    auth = HTTPBasicAuth(username, key)
    base_url = os.environ["DEV_JIRA_BASE_URL"]
    url = None
    data = None

    def put_atlassian(self):
        print(f"{self.base_url}{self.url}")
        return requests.put(f"{self.base_url}{self.url}",
                            auth=HTTPBasicAuth(self.username, self.key),
                            headers={"Accept": "application/json", "Content-Type": "application/json"},
                            data=self.data)
