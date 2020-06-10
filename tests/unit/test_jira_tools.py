import os

from tool_box import jira_tools


def test_get_all_users():
    all_users = jira_tools.get_all_users()
    assert isinstance(all_users, list)


def test_find_user_by_account_id():
    pass


def test_find_user_by_email():
    pass


def test_find_users_groups_by_account_id():
    account_id = os.environ["MY_JIRA_ACCOUNT_ID"]
    users_groups = jira_tools.find_users_groups_by_account_id(account_id)
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
    pass


def test_user_managment():
    pass