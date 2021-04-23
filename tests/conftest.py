import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    # CSS Open Browser and driver path
    driver = webdriver.Chrome(executable_path="C:\\Users\\karen.castillo\\PycharmProjects\\focusservicestest\\utilities\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.google.com")
    request.cls.driver = driver
    yield
    driver.close()