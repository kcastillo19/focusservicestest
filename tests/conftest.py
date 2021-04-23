import pytest
from selenium import webdriver


"""def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )"""

@pytest.fixture(scope="class")
def setup(request):
    # CSS Open Browser and avoid popups
    #chrome_options=webdriver.ChromeOptions()
    #chrome_prefs = {}
    #option.experimental_options["prefs"] = chrome_prefs
    #chrome_prefs["profile.default_content_settings"] = {"popups": 1}
    #chrome_options.add_argument("headless")
    #chrome_options.add_argument("window-size=1500,1200")
    #browser_name=request.config.getoption("browser_name")
    #if browser_name == "chrome":
    driver = webdriver.Chrome(executable_path="C:\\work\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.google.com")
    request.cls.driver = driver
    yield
    driver.close()