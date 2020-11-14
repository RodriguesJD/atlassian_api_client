import os

import requests
from requests.auth import HTTPBasicAuth


class GetAtlassian:
    username = os.environ["WORK_EMAIL"]
    key = os.environ["DEV_JIRA_KEY"]
    auth = HTTPBasicAuth(username, key)
    base_url = os.environ["DEV_JIRA_BASE_URL"]
    url = None
    query = None

    def get_atlassian(self):
        return requests.get(f"{self.base_url}{self.url}",
                            auth=HTTPBasicAuth(self.username, self.key),
                            headers={"Accept": "application/json"},
                            params=self.query)