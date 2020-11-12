import os
from pprint import pprint
import json
import requests
from requests.auth import HTTPBasicAuth

from atlassian import ServiceDesk


base_url = os.environ["DEV_JIRA_BASE_URL"]
username = os.environ["WORK_EMAIL"]
key = os.environ["DEV_JIRA_KEY"]



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


def add_user_to_org(account_id, org_id):
    url = f"{base_url}/rest/servicedeskapi/organization/{org_id}/user"

    headers = {
        "Accept": "application/json"
    }

    payload = json.dumps({
        "accountIds": [
            account_id
        ],
        "usernames": []
    })

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
