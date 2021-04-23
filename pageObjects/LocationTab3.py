from selenium.webdriver.common.by import By

class LocationTab3:
    title3 = (By.XPATH, "//b[contains(text(), 'Bacolod City, Philippines')]")

    def __init__(self, driver):
        self.driver = driver

    # Validate Asia
    def validate_asia(self):
        tit3 = self.driver.find_element(*LocationTab3.title3).is_displayed()
        return print(tit3)