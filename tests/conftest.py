import pytest
import uuid

from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    #global driver
    driver = webdriver.Chrome()

    return driver
