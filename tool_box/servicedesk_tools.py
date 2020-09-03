import os
from pprint import pprint

from atlassian import ServiceDesk


base_url = os.environ["JIRA_BASE_URL"]
username = os.environ["WORK_EMAIL"]
key = os.environ["JIRA_KEY"]


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

