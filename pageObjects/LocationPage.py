from selenium.webdriver.common.by import By
from pageObjects.LocationTab2 import LocationTab2

class LocationPage:
    region = (By.CSS_SELECTOR, "span[ class='av-inner-tab-title']")
    ca= (By.LINK_TEXT, "CENTRAL AMERICA")

    def __init__(self, driver):
        self.driver = driver

    #Locate North America Link
    def validate_na(self):
        regions=self.driver.find_element(*LocationPage.region).text
        assert "NORTH AMERICA" in regions, "The text was not found"
        return print(regions + " link was found")

    #Validate Central America
    def click_ca(self):
        self.driver.find_element(*LocationPage.ca).click()
        tab2=LocationTab2(self.driver)
        return tab2