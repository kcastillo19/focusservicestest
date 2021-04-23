from selenium.webdriver.common.by import By
from pageObjects.LocationTab3 import LocationTab3

class LocationTab2:
    title1 = (By.XPATH, "//b[contains(text(), 'San Salvador, El Salvador')]")
    title2 = (By.XPATH, "//b[contains(text(), 'Managua, Nicaragua')]")
    asia = (By.LINK_TEXT, "ASIA")

    def __init__(self, driver):
        self.driver = driver

    # Validate Central America
    def validate_title1(self):
        tit1=self.driver.find_element(*LocationTab2.title1).is_displayed()
        return print(tit1)

    def validate_title2(self):
        tit2=self.driver.find_element(*LocationTab2.title2).is_displayed()
        return print(tit2)

    # Click Asia
    def click_asia(self):
        self.driver.find_element(*LocationTab2.asia).click()
        tab3 = LocationTab3(self.driver)
        return tab3