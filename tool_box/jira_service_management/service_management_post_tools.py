import json

try:
    from tool_box.atlassian_post_tools import PostAtlassian
except ModuleNotFoundError:
    from atlassian_api_client.tool_box.atlassian_post_tools import PostAtlassian



class CustomerPost(PostAtlassian):
    url = "/rest/servicedeskapi/customer"

    def create_custormer(self, display_name, email):
        self.data = json.dumps({
            "displayName": display_name,
            "email": email
        }
        )
        return self.post_atlassian()


class OrganizationPost(PostAtlassian):
    url = "/rest/servicedeskapi/organization"

    def add_customer_to_org(self, org_id, account_id):
        self.url = f"{self.url}/{org_id}/user"
        self.data = json.dumps({"accountIds": [account_id]})
        response = self.post_atlassian()
        return response

    def create_org(self, org_name):
        self.data = json.dumps({"name": org_name})
        return self.post_atlassian()


class ServiceDeskPost(PostAtlassian):
    url = "/rest/servicedeskapi/servicedesk/"

    def add_org_to_serivedesk_instance(self, service_desk_id, org_id):
        self.url = f"{self.url}/{service_desk_id}/organization"
        self.data = json.dumps({"organizationId": org_id})
        return self.post_atlassian()




