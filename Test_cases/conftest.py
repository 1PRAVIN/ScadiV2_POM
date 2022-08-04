import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    baseurl = "https://test.ecomexpress.in:9013/#/login"
    driver = webdriver.Chrome()
    driver.get(baseurl)
    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.delete_all_cookies()
    return driver

