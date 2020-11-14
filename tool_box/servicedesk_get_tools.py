import os
from pprint import pprint
import json
import requests
from requests.auth import HTTPBasicAuth
from tool_box.jira_get_tools import GetAtlassian
from atlassian import ServiceDesk
import requests
from requests.auth import HTTPBasicAuth

base_url = os.environ["DEV_JIRA_BASE_URL"]
username = os.environ["WORK_EMAIL"]
key = os.environ["DEV_JIRA_KEY"]


class ServiceDeskPost:
    username = os.environ["WORK_EMAIL"]
    key = os.environ["DEV_JIRA_KEY"]
    auth = HTTPBasicAuth(username, key)
    base_url = os.environ["DEV_JIRA_BASE_URL"]
    url = None
    data = None

    def post_atlassian(self):
        return requests.post(f"{self.base_url}{self.url}",
                             auth=HTTPBasicAuth(self.username, self.key),
                             headers={"Content-Type": "application/json"},
                             data=self.data)

def service_desk_request():
    sd = ServiceDesk(
            url=base_url,
            username=username,
            password=key)

    return sd


def list_all_sd_projects():
    return service_desk_request().get_service_desks()


def list_request_types(service_desk_id):
    return service_desk_request().get_request_types(service_desk_id)["values"]


def create_ticket(service_desk_id, request_type_id, dict_values):
    return service_desk_request().create_customer_request(service_desk_id=service_desk_id, request_type_id=request_type_id, values_dict=dict_values)


def list_tickets(service_desk_id, queue_id):
    return service_desk_request().get_issues_in_queue(service_desk_id=service_desk_id, queue_id=queue_id)


def does_org_exist(org_name):
    url = f"{base_url}/rest/servicedeskapi/organization/search?query={org_name}"

    headers = {
        "Accept": "application/json"
    }

    response = requests.request(
        "GET",
        url,
        headers=headers
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


def add_customer_to_org(account_id, org_id):
    url = f"{base_url}/rest/servicedeskapi/organization/{org_id}/user"
    print(account_id)
    print(org_id)
    print(url)

    headers = {
        "Accept": "application/json"
    }

    payload = json.dumps({
        "accountIds": [
            account_id
        ],
        "usernames": []

    })
    pprint(payload)
    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))


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


class OrganizationPost(ServiceDeskPost):
    url = "/rest/servicedeskapi/organization"

    def add_customer_to_org(self, org_id, account_id):
        self.url = f"{self.url}/{org_id}/user"
        self.data = json.dumps({"accountIds": [account_id]})
        response = self.post_atlassian()
        return response



# class ServiceDesk(GetAtlassian):
#     url = "/rest/servicedeskapi/servicedesk"

