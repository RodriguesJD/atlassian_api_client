import os
from pprint import pprint
from tool_box.atlassian_get_tools import GetAtlassian


class Users(GetAtlassian):
    url = "/rest/api/3/user"

    def get_all_users_as_a_list(self):
        """

        Returns:
            list: All users found in jira.

        """
        all_user_data = []
        start_int = 0

        while isinstance(start_int, int):
            self.url = f'{self.url}s/search?username=.&startAt={start_int}&maxResults=50'
            response = self.get_atlassian()
            if len(response.text) > 2:
                for user in response.json():
                    all_user_data.append(user)

                start_int += 50
            else:
                start_int = 'End Loop'  # a str will kill the while loop

        return all_user_data

    def find_user_by_account_id(self, account_id):
        self.query = {'accountId': account_id}
        self.url = f'{self.url}'
        response = self.get_atlassian()
        return response

    def find_user_by_email(self, user_email):
        self.url = f"{self.url}/search?query={user_email}"
        response = self.get_atlassian()
        return response

    def find_users_groups_by_account_id(self, account_id):
        self.query = {'accountId': account_id}
        self.url = f'{self.url}/groups'
        response = self.get_atlassian()
        return response

    def get_user_property(self, account_id):
        self.query = {'accountId': account_id}
        self.url = f'{self.url}/properties'
        response = self.get_atlassian()
        return response


class Groups(GetAtlassian):
    url = "/rest/api/3/group"

    def get_all_groups(self):
        self.url = f'{self.url}s/picker'
        response = self.get_atlassian().json()
        total_group = response["total"]
        self.url = f"{self.url}?maxResults={total_group}"
        response_with_total_groups = self.get_atlassian()

        return response_with_total_groups

    def users_in_group_by_group_name(self, group_name):
        group_users = []
        self.url = f'{self.url}/member?groupname={group_name}'
        response = self.get_atlassian().json()

        for user in response['values']:
            group_users.append(user)

        response_keys = response.keys()
        if "nextPage" in response_keys:
            next_page = response["nextPage"]

            need_to_get_more_members = True
            while need_to_get_more_members:
                self.url = next_page
                response = self.get_atlassian().json()
                response_keys = response.keys()
                if "nextPage" not in response_keys:
                    need_to_get_more_members = False
                else:
                    next_page = response["nextPage"]

                for user in response['values']:
                    group_users.append(user)

        return group_users

    def find_group_by_name(self, group_name):
        self.url = f'{self.url}/member?groupname={group_name}'
        response = self.get_atlassian()
        return response


def get_all_projects():
    username = os.environ["WORK_EMAIL"]
    key = os.environ["DEV_JIRA_KEY"]
    base_url = os.environ["DEV_JIRA_BASE_URL"]

    all_projects = []
    is_last = False
    headers = {"Accept": "application/json"}
    auth = HTTPBasicAuth(username, key)
    url = f'{base_url}/rest/api/2/project/search?project'
    while not is_last:
        response = requests.get(url=url, headers=headers, auth=auth).json()
        if not response['isLast']:
            url = response['nextPage']
            for project in response['values']:
                all_projects.append(project)
        else:
            for project in response['values']:
                all_projects.append(project)

            is_last = True  # If this is true then its the last page so stop the while loop.

    return all_projects


def find_project_by_id(project_id):
    username = os.environ["WORK_EMAIL"]
    key = os.environ["DEV_JIRA_KEY"]
    base_url = os.environ["DEV_JIRA_BASE_URL"]
    headers = {"Accept": "application/json"}
    auth = HTTPBasicAuth(username, key)
    url = f'{base_url}/rest/api/2/project/{project_id}'
    response = requests.get(url=url, headers=headers, auth=auth).json()
    return response


def find_issue_by_id(issue_id):
    username = os.environ["WORK_EMAIL"]
    key = os.environ["DEV_JIRA_KEY"]
    base_url = os.environ["DEV_JIRA_BASE_URL"]
    headers = {"Accept": "application/json"}
    auth = HTTPBasicAuth(username, key)
    url = f'{base_url}/rest/api/2/issue/{issue_id}'
    response = requests.get(url=url, headers=headers, auth=auth).json()
    return response


# TODO move this to its own module jira_delete_tools
def delete_user_by_id(account_id):
    username = os.environ["WORK_EMAIL"]
    key = os.environ["DEV_JIRA_KEY"]
    base_url = os.environ["DEV_JIRA_BASE_URL"]
    auth = HTTPBasicAuth(username, key)
    url = f'{base_url}/rest/api/2/user'
    query = {'accountId': account_id}
    response = requests.delete(url=url, params=query, auth=auth).status_code
    return response


