from pprint import pprint
import json


from tool_box.jira_get_tools import GetAtlassian
from tool_box.atlassian_post_tools import PostAtlassian
from atlassian import ServiceDesk


class Organization(GetAtlassian):
    url = "/rest/servicedeskapi/organization"

    def get_all_organizations_as_a_list(self):
        self.url = f"{self.url}"
        response = self.get_atlassian()
        return response

    def find_customers_in_an_org(self, org_id):
        self.url = f"{self.url}/{org_id}/user"
        response = self.get_atlassian()
        return response

    def get_orgs(self):
        self.url = f"{self.url}"
        response = self.get_atlassian()
        return response


class OrganizationPost(PostAtlassian):
    url = "/rest/servicedeskapi/organization"

    def add_customer_to_org(self, org_id, account_id):
        self.url = f"{self.url}/{org_id}/user"
        self.data = json.dumps({"accountIds": [account_id]})
        response = self.post_atlassian()
        return response


