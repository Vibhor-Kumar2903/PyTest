import json
import pytest
import os
from datetime import datetime

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    now = datetime.now().strftime("%y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"


@pytest.fixture(scope='session', autouse=True)
def setup_teardown():
    print("\nSetting up resources...")
    yield
    print("\nTearing down resources...")


# @pytest.fixture()
def read_json(file_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # directory where this .py file lives
    file_path = os.path.join(base_dir, "data", file_name)
    with open(file_path, "r", encoding="utf-8") as json_file:
        payload = json.load(json_file)
        print(payload)
    return payload




