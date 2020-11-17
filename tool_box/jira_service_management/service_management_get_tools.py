from tool_box.jira_tools.jira_get_tools import GetAtlassian


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

    def find_org_by_searching_all_service_desks(self):
        # TODO find out which service desk id we are using. Shoold i look accross all ids?
        pass


