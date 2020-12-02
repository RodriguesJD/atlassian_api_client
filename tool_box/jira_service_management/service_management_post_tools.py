import json

try:
    from tool_box.atlassian_post_tools import PostAtlassian
except ModuleNotFoundError:
    from atlassian_api_client.tool_box.atlassian_post_tools import PostAtlassian




class CustomerPost(PostAtlassian):
    url = "/rest/servicedeskapi/customer"

    def create_custormer(self, display_name, email):
        self.data = json.dumps({
            "displayName": "Fred F. User",
            "email": "fred@example.com"
        }
        )



class OrganizationPost(PostAtlassian):
    url = "/rest/servicedeskapi/organization"

    def add_customer_to_org(self, org_id, account_id):
        self.url = f"{self.url}/{org_id}/user"
        self.data = json.dumps({"accountIds": [account_id]})
        response = self.post_atlassian()
        return response


CustomerPost().create_custormer("disp", "em")