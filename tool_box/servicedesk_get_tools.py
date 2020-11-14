from pprint import pprint
import json


from tool_box.jira_get_tools import GetAtlassian

from atlassian import ServiceDesk


class Organization(GetAtlassian):
    url = "/rest/servicedeskapi/organization"

    def get_first_page_of_orgs(self):
        # Todo add pagination to this func and then change the name to get_all_orgs_as_list
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





