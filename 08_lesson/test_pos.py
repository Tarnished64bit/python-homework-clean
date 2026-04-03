class TestProjectsAPI:

    def test_create_project_positive(self, projects_api):
        title = "My New Project"
        response = projects_api.create_project(title=title)

        assert response.status_code == 201
        data = response.json()
        assert "id" in data
        assert isinstance(data["id"], str)

        projects_api.delete_project(data["id"])

    def test_get_project_positive(self, projects_api, created_project):
        response = projects_api.get_project(created_project)

        assert response.status_code == 200
        data = response.json()
        assert data.get("id") == created_project
        assert "title" in data

    def test_update_project_positive(self, projects_api, created_project):
        new_title = "Updated Project Name"
        response = projects_api.update_project(
            project_id=created_project,
            title=new_title
        )

        assert response.status_code == 200

        get_response = projects_api.get_project(created_project)
        assert get_response.json().get("title") == new_title

    def test_delete_project_positive(self, projects_api):
        create_response = projects_api.create_project(
            title="Project to Delete"
        )
        assert create_response.status_code == 201
        project_id = create_response.json().get("id")

        delete_response = projects_api.delete_project(project_id)
        assert delete_response.status_code == 200

        get_response = projects_api.get_project(project_id)
        assert get_response.status_code == 404
