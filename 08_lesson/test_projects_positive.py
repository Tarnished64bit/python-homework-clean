class TestProjectsAPI:

    def test_create_project_positive(self, projects_api):
        title = "My New Project"
        response = projects_api.create_project(title=title)

        assert response.status_code == 201, (
            "Статус код" + str(response.status_code) +
            "\nОтвет: " + response.text
        )

        data = response.json()
        assert "id" in data, "В ответе отсутствует поле id"
        assert isinstance(data["id"], str), "id должен быть строкой"

        projects_api.update_project(data["id"], deleted=True)

    def test_get_project_positive(self, projects_api, created_project):
        response = projects_api.get_project(created_project)

        assert response.status_code == 200, (
            "Статус код" + str(response.status_code)
        )

        data = response.json()
        assert data.get("id") == created_project, "ID проекта не совпадает"
        assert "title" in data, "Отсутствует поле title"
        assert "timestamp" in data, "Отсутствует поле timestamp"

    def test_update_project_title_positive(self, projects_api, created_project):
        new_title = "Updated Project Name"
        response = projects_api.update_project(
            project_id=created_project,
            title=new_title
        )

        assert response.status_code == 200, (
            "Статус код" + str(response.status_code)
        )

        get_response = projects_api.get_project(created_project)
        assert get_response.json().get("title") == new_title
