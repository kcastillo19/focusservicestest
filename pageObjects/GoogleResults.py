from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage

class GoogleResults:
    url = (By.CSS_SELECTOR, "cite[class*='iUh30 Zu0yb tjvcx']")
    focuslink = (By.CSS_SELECTOR, "cite[class*='iUh30 Zu0yb tjvcx']")

    def __init__(self, driver):
        self.driver = driver

    #validate if the URL exists and click to Focus Home Page
    def validateurl(self):
        slist = self.driver.find_element(*GoogleResults.url).text
        assert "https://www.focusservices.com" in slist
        return print("This url exists: {}".format(slist))

    def click_url(self):
        self.driver.find_element(*GoogleResults.focuslink).click()
        fhomepage = HomePage(self.driver)
        return fhomepage