try:
    from tool_box.atlassian_post_tools import PostAtlassian
except ModuleNotFoundError:
    from atlassian_api_client.

class OrganizationPost(PostAtlassian):
    url = "/rest/servicedeskapi/organization"

    def add_customer_to_org(self, org_id, account_id):
        self.url = f"{self.url}/{org_id}/user"
        self.data = json.dumps({"accountIds": [account_id]})
        response = self.post_atlassian()
        return response