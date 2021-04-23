from pageObjects.SearchPage import SearchPage
from pageObjects.GoogleResults import GoogleResults
import time
from utilities.BaseClass import BaseClass

class GoogleSearch(BaseClass):

    def test_search(self):

        time.sleep(5)
        # Google search tab
        spage = SearchPage(self.driver)
        spage.enter_search().clear()
        spage.enter_search().send_keys("Focus Services")
        # Google Search button and redirect to google result page
        time.sleep(5)
        SearchPage.enter_click()
        # validate if the URL exists and click to Focus Home Page
        homepages = GoogleResults(self.driver)
        homepages.validateurl()



""""#Validate if the button exists
hbutton = driver.find_element_by_xpath("//span[text()='Now Hiring!']")
be= hbutton.text
assert "Now Hiring!" in be, "The button does not exist"
print("The button exists: {}".format(be))
hbutton.click()

#Location tab interactions
menu=driver.find_elements_by_css_selector("ul[id='avia-menu'] li a")

i=-1
for menuTab in menu:
    i = i+1
    menus = menuTab.text
    if menus == "Locations":
        driver.find_elements_by_css_selector("span[ class='avia-menu-text']")[i].click()
        break

#Locate North America Link
region = driver.find_element_by_css_selector("span[ class='av-inner-tab-title']").text
assert "NORTH AMERICA" in region, "The text was not found"
print(region+" link was found")

#Validate Central America
driver.find_element_by_link_text("CENTRAL AMERICA").click()

title1=driver.find_element_by_xpath("//b[contains(text(), 'San Salvador, El Salvador')]").is_displayed()
title2=driver.find_element_by_xpath("//b[contains(text(), 'Managua, Nicaragua')]").is_displayed()
print(title1, title2)

#Validate Asia
driver.find_element_by_link_text("ASIA").click()
title3=driver.find_element_by_xpath("//b[contains(text(), 'Bacolod City, Philippines')]").is_displayed()
print(title3)"""

















