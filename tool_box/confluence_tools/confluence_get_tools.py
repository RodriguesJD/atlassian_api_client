try:
    from tool_box.atlassian_get_tools import GetAtlassian
except ModuleNotFoundError:
    from atlassian_api_client.tool_box.atlassian_get_tools import GetAtlassian


class Content(GetAtlassian):
    url = "/wiki/rest/api/content"

    def get_first_page_content(self):
        self.url = self.url
        response = self.get_atlassian()
        return response

    def get_page_by_id(self, id):
        self.url = f"{self.url}/{id}"
        response = self.get_atlassian()
        return response

    def get_page_body_by_id(self, id):
        self.url = f"{self.url}/{id}?expand=body.storage"
        response = self.get_atlassian()
        return response
