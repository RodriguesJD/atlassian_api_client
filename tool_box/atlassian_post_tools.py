import os

import requests
from requests.auth import HTTPBasicAuth


class PostAtlassian:
    username = os.environ["WORK_EMAIL"]
    key = os.environ["DEV_JIRA_KEY"]
    auth = HTTPBasicAuth(username, key)
    base_url = os.environ["DEV_JIRA_BASE_URL"]
    url = None
    data = None

    def post_atlassian(self):
        return requests.post(f"{self.base_url}{self.url}",
                             auth=HTTPBasicAuth(self.username, self.key),
                             headers={"Content-Type": "application/json"},
                             data=self.data)