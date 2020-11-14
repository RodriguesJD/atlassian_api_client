import os
import sys
sys.path.insert(0, os.getcwd())

try:
    from tool_box import jira_get_tools
except ModuleNotFoundError:
    from atlassian_api_client.tool_box import jira_get_tools


def test_get_all_users():
    all_users = jira_get_tools.Users().get_all_users_as_a_list()
    assert isinstance(all_users, list)


def test_find_user_by_account_id():
    pass


def test_find_user_by_email():
    pass

# todo break theese tests into get and post tests
def test_find_users_groups_by_account_id():
    account_id = os.environ["DEV_MY_JIRA_ACCOUNT_ID"]
    users_groups = jira_get_tools.Users().find_users_groups_by_account_id(account_id).json()
    isinstance(users_groups, list)
    for group in users_groups:
        isinstance(group, dict)
        isinstance(group["name"], str)
        isinstance(group['self'], str)


def test_delete_user_by_id():
    pass


def test_get_all_projects():
    pass

def test_find_project_by_id():
    pass

def test_find_issue_by_id():
    pass


def test_get_user_property():
    pass


def test_get_all_groups():
    all_groups = jira_get_tools.Groups().get_all_groups().json()
    groups = all_groups['groups']
    isinstance(all_groups, dict)
    isinstance(groups, list)
    for group in groups:
        group_id = group['groupId']
        isinstance(group_id, str)
        group_html = group['html']
        isinstance(group_html, str)
        group_labels = group['labels']
        isinstance(group_labels, list)
        group_name = group['name']
        isinstance(group_name, str)


def test_users_in_group_by_group_name():
    group_name = 'itsupport'
    group_members = jira_get_tools.Groups().users_in_group_by_group_name(group_name)
    isinstance(group_members, list)
    for member in group_members:
        isinstance(member, dict)


def test_user_managment():
    pass