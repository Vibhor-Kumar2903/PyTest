import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pytest import fixture


@pytest.fixture
def driver_setup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver


