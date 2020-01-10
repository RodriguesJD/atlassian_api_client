from tool_box import jira_tools


def test_get_all_users():
    all_users = jira_tools.get_all_users()
    assert isinstance(all_users, list)