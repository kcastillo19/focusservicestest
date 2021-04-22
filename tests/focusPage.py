from selenium import webdriver
import time

#CSS selector Open Browser and avoid popups
option = webdriver.ChromeOptions()
chrome_prefs = {}
option.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"popups": 1}
driver=webdriver.Chrome(executable_path="C:\\focusservices\\focusservicestest\\utilities\\chromedriver.exe", options=option)
driver.maximize_window()
driver.get("https://www.google.com")


#CSS selector Google's Search
time.sleep(2)
driver.find_element_by_class_name("gLFyf").send_keys("Focus Services")
time.sleep(2)
driver.find_element_by_class_name("gNO89b").click()


#CSS Selector to validate if the URL exists and click
time.sleep(5)
url = driver.find_element_by_css_selector("cite[class*='iUh30 Zu0yb tjvcx']").text
assert "https://www.focusservices.com" in url, "https://www.focusservices.com does not exist"
print("This url exists: {}".format(url))
driver.find_element_by_css_selector("cite[class*='iUh30 Zu0yb tjvcx']").click()

#CSS Selector to validate if the button exists
hbutton = driver.find_element_by_xpath("//span[text()='Now Hiring!']")
be= hbutton.text
assert "Now Hiring!" in be, "The button does not exist"
print("The button exists: {}".format(be))
hbutton.click()

#CSS Selector from Location tab
menu=driver.find_elements_by_css_selector("ul[id='avia-menu'] li a")


i=-1
for menuTab in menu:
    i = i+1
    menus = menuTab.text
    if menus == "Locations":
        driver.find_elements_by_css_selector("span[ class='avia-menu-text']")[i].click()
        break

#CSS Selector •	Locate North America Link
region = driver.find_element_by_css_selector("span[ class='av-inner-tab-title']").text
assert "NORTH AMERICA" in region, "The text was not found"
print(region+" link was found")

#CSS Selector click in Central America
driver.find_element_by_link_text("CENTRAL AMERICA").click()

title1=driver.find_element_by_xpath("//b[contains(text(), 'San Salvador, El Salvador')]").is_displayed()
title2=driver.find_element_by_xpath("//b[contains(text(), 'Managua, Nicaragua')]").is_displayed()
print(title1, title2)

#CSS Selector click in Asia
driver.find_element_by_link_text("ASIA").click()
title3=driver.find_element_by_xpath("//b[contains(text(), 'Bacolod City, Philippines')]").is_displayed()
print(title3)

driver.close()

















