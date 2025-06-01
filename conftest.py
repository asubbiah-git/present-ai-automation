import pytest
import yaml

# Add --data command-line option
def pytest_addoption(parser):
    parser.addoption(
        "--setup", action="store", default="setup/setup_stage.yaml",
          help="Path to the setup YAML data file"
    )
    parser.addoption("--language", action="store", default="english", help="provide the language")

@pytest.fixture(scope="session")
def setup_file(request):
    return request.config.getoption("--setup")

@pytest.fixture(scope="session")
def setup_data(setup_file):
    with open(setup_file, "r") as f:
        return yaml.safe_load(f)
    
@pytest.fixture(scope="session")
def credentials(setup_data):
    return {
        "username": setup_data["username"],
        "password": setup_data["password"],
        "url": setup_data["url"]
    }

@pytest.fixture(scope="class", autouse=True)
def get_language(request):
    request.cls.language = request.config.getoption("--language")
    
@pytest.fixture(scope="class")
def login_credentials(request, credentials):
    request.cls.credentials = credentials    
