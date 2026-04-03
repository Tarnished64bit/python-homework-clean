from api_client import ApiClient


class ProjectsAPI:
    def __init__(self):
        self.client = ApiClient()

    def create_project(self, title, users=None):
        data = {"title": title}
        if users is not None:
            data["users"] = users
        return self.client.post("/projects", data)

    def update_project(self, project_id, title=None, users=None, deleted=None):
        data = {}
        if title is not None:
            data["title"] = title
        if users is not None:
            data["users"] = users
        if deleted is not None:
            data["deleted"] = deleted

        if not data:
            raise ValueError("Не передано ни одного поля")

        return self.client.put("/projects/" + project_id, data)

    def get_project(self, project_id):
        return self.client.get("/projects/" + project_id)
