from selenium.webdriver.common.by import By
from pageObjects.GoogleResults import GoogleResults

class SearchPage:
    search=(By.CLASS_NAME, "gLFyf")
    button = (By.CLASS_NAME, "gNO89b")

    def __init__(self, driver):
        self.driver = driver

    # Google search tab
    def enter_search(self):
        return self.driver.find_element(*SearchPage.search)

    # Google Search button and redirect to google result page
    def enter_click(self):
        self.driver.find_element(*SearchPage.button).click()
        googleresult = GoogleResults(self.driver)
        return googleresult

