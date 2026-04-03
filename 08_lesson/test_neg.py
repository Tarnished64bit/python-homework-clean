class TestProjectsAPI:

    def test_create_project_without_title_negative(self, projects_api):
        response = projects_api.create_project(title="")

        assert response.status_code == 400

    def test_get_nonexistent_project_negative(self, projects_api):
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = projects_api.get_project(fake_id)

        assert response.status_code == 404

    def test_update_nonexistent_project_negative(self, projects_api):
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = projects_api.update_project(
            project_id=fake_id,
            title="New Title"
        )

        assert response.status_code == 404

    def test_delete_nonexistent_project_negative(self, projects_api):
        fake_id = "00000000-0000-0000-0000-000000000000"
        response = projects_api.delete_project(fake_id)

        assert response.status_code == 404
