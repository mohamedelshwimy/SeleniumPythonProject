import pytest
from selenium import webdriver


url = "https://rahulshettyacademy.com/angularpractice/"


@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome
    driver.get(url)
    driver.maximize_window()