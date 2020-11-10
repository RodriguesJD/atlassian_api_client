import os
from pprint import pprint

import requests
from requests.auth import HTTPBasicAuth

username = os.environ["WORK_EMAIL"]
base_url = os.environ["DEV_JIRA_BASE_URL"]
key = os.environ["DEV_JIRA_KEY"]


def get_all_users():
    """

    Returns:
        list: All users found in jira.

    """
    all_user_data = []
    start_int = 0
    headers = {"Accept": "application/json"}
    auth = HTTPBasicAuth(username, key)
    while isinstance(start_int, int):
        url = f'{base_url}/rest/api/2/users/search?username=.&startAt={start_int}&maxResults=50'
        response = requests.get(url=url, headers=headers, auth=auth)
        if len(response.text) > 2:
            for user in response.json():
                all_user_data.append(user)

            start_int += 50
        else:
            start_int = 'End Loop'  # a str will kill the while loop

    return all_user_data


def find_user_by_account_id(account_id):
    headers = {"Accept": "application/json"}
    auth = HTTPBasicAuth(username, key)
    query = {'accountId': account_id}
    url = f'{base_url}/rest/api/2/user'
    response = requests.get(url=url, headers=headers, params=query, auth=auth).json()
    return response


def find_user_by_email(user_email):
    headers = {"Accept": "application/json"}
    auth = HTTPBasicAuth(username, key)
    url = f'{base_url}/rest/api/2/user/search?username={user_email}'
    response = requests.get(url=url, headers=headers, auth=auth).json()
    return response


def find_users_groups_by_account_id(account_id):
    headers = {"Accept": "application/json"}
    auth = HTTPBasicAuth(username, key)
    query = {'accountId': account_id}
    url = f'{base_url}/rest/api/2/user/groups?accountId={account_id}'
    response = requests.get(url=url, headers=headers, params=query, auth=auth).json()
    return response


def delete_user_by_id(account_id):
    auth = HTTPBasicAuth(username, key)
    url = f'{base_url}/rest/api/2/user'
    query = {'accountId': account_id}
    response = requests.delete(url=url, params=query, auth=auth).status_code
    return response


def get_all_projects():
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
    headers = {"Accept": "application/json"}
    auth = HTTPBasicAuth(username, key)
    url = f'{base_url}/rest/api/2/project/{project_id}'
    response = requests.get(url=url, headers=headers, auth=auth).json()
    return response


def find_issue_by_id(issue_id):
    headers = {"Accept": "application/json"}
    auth = HTTPBasicAuth(username, key)
    url = f'{base_url}/rest/api/2/issue/{issue_id}'
    response = requests.get(url=url, headers=headers, auth=auth).json()
    return response


def get_user_property(account_id):
    headers = {"Accept": "application/json"}
    auth = HTTPBasicAuth(username, key)
    query = {'accountId': account_id}
    url = f'{base_url}/rest/api/2/user/properties'
    response = requests.get(url=url, headers=headers, params=query, auth=auth).json()
    return response


def get_all_groups():
    headers = {"Accept": "application/json"}
    auth = HTTPBasicAuth(username, key)
    url = f'{base_url}/rest/api/2/groups/picker'
    response = requests.get(url=url, headers=headers, auth=auth).json()
    total_group = response["total"]
    url_with_total = f"{url}?maxResults={total_group}"
    response_with_total_groups = requests.get(url=url_with_total, headers=headers, auth=auth).json()

    return response_with_total_groups


def users_in_group_by_group_name(group_name):
    group_users = []
    headers = {"Accept": "application/json"}
    auth = HTTPBasicAuth(username, key)
    url = f'{base_url}/rest/api/2/group/member?groupname={group_name}'
    response = requests.get(url=url, headers=headers, auth=auth).json()

    for user in response['values']:
        group_users.append(user)

    response_keys = response.keys()
    if "nextPage" in response_keys:
        next_page = response["nextPage"]

        need_to_get_more_members = True
        while need_to_get_more_members:
            response = requests.get(url=next_page, headers=headers, auth=auth).json()
            response_keys = response.keys()
            if "nextPage" not in response_keys:
                need_to_get_more_members = False
            else:
                next_page = response["nextPage"]

            for user in response['values']:
                group_users.append(user)

    return group_users


def find_group_by_name(group_name):
    headers = {"Accept": "application/json"}
    auth = HTTPBasicAuth(username, key)
    url = f'{base_url}/rest/api/2/group/member?groupname={group_name}'
    response = requests.get(url=url, headers=headers, auth=auth).json()

    return response


def user_managment(account_id):
    headers = {
        "Accept": "application/json",
        "Authorization": key
    }
    url = f'{base_url}/admin/users/{account_id}/manage/profile'
    response = requests.get(url=url, headers=headers).text
    pprint(response)






