from pageObjects.LocationPage import LocationPage
from pageObjects.LocationTab2 import LocationTab2
from pageObjects.LocationTab3 import LocationTab3
from pageObjects.SearchPage import SearchPage
from pageObjects.GoogleResults import GoogleResults
from pageObjects.HomePage import HomePage
import time
from utilities.BaseClass import BaseClass
import pytest

class TestGoogleSearch(BaseClass):

    def test_search(self):

        time.sleep(5)
        # Google search tab
        spage = SearchPage(self.driver)
        spage.enter_search().clear()
        spage.enter_search().send_keys("Focus Services")
        # Google Search button and redirect to google result page
        time.sleep(5)
        spage.enter_click()
        # validate if the URL exists and click to Focus Home Page
        homepages = GoogleResults(self.driver)
        homepages.validateurl()
        homepages.click_url()
        # Validate if the Hiring button exists
        homePage = HomePage(self.driver)
        homePage.validatebutton()
        # Location Click
        menus=homePage.text_location()

        i = -1
        for menuTab in menus:
            i = i + 1
            m = menuTab.text
            if m == "Locations":
                homePage.click_location()[i].click()
                break

        # Locate North America Link
        validates= LocationPage(self.driver)
        validates.validate_na()
        # Validate Central America
        validates.click_ca()
        catittles=LocationTab2(self.driver)
        catittles.validate_title1()
        catittles.validate_title2()
        # Validate Asia
        catittles.click_asia()
        asiatab= LocationTab3(self.driver)
        asiatab.validate_asia()

















