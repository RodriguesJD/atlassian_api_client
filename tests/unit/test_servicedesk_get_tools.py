import os

from tool_box.servicedesk_get_tools import Organization


class TestOrganization:

    org_api = Organization

    def test_et_first_page_of_orgs(self):
        all_orgs_json = self.org_api().get_first_page_of_orgs().json()
        assert isinstance(all_orgs_json, dict)

        get_request_url = 'https://ripplelabs-dev.atlassian.net/rest/servicedeskapi/organization'
        # Confirm you are using the correct url for the api get call.
        assert all_orgs_json["_links"]["self"] == get_request_url

    def test_find_customers_in_an_org(self):
        org_id = os.environ["DEV_ORG_ID"]
        find_customers_in_org_json = self.org_api().find_customers_in_an_org(org_id=org_id)
        assert isinstance(find_customers_in_org_json, dict)