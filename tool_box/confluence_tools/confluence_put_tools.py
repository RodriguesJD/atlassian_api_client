import json
try
    from tool_box.atlassian_put_tools import PutAtlassian
except ModuleNotFoundError:
    from atlassian_api_client.tool_box.atlassian_put_tools import PutAtlassian

class UpdateContent(PutAtlassian):
    url = "/wiki/rest/api/content"

    def update_body_by_id(self, page_id, body):
        self.url = f"{self.url}/{page_id}"
        self.data = body
        response = self.put_atlassian()
        return response

