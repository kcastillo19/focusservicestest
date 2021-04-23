from selenium.webdriver.common.by import By


class HomePage:
    nbutton = (By.XPATH, "//span[text()='Now Hiring!']")
    menu = (By.CSS_SELECTOR, "ul[id='avia-menu'] li a")
    menulocation = (By.CSS_SELECTOR, "span[ class='avia-menu-text']")


    def __init__(self, driver):
        self.driver = driver

    # Validate if the Hiring button exists
    def validatebutton(self):
        bhiring= self.driver.find_element(*HomePage.nbutton).text
        assert "Now Hiring!" in bhiring, "The button does not exist"
        print("The button exists: {}".format(bhiring))

    # Location Click
    def text_location(self):
         return self.driver.find_elements(*HomePage.menu)


    def click_location(self):
         return self.driver.find_elements(*HomePage.menulocation)






