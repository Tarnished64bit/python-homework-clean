import pytest
from projects_API import ProjectsAPI


@pytest.fixture
def projects_api():
    return ProjectsAPI()


@pytest.fixture
def created_project(projects_api):
    response = projects_api.create_project(title="Test Project for API")

    assert response.status_code == 201, (
        "Не удалось создать проект: " + str(response.status_code) +
        " - " + response.text
    )

    project_id = response.json().get("id")
    yield project_id

    projects_api.update_project(project_id, deleted=True)
