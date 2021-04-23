from selenium import webdriver
import time

#Open Browser and avoid popups
option = webdriver.ChromeOptions()
chrome_prefs = {}
option.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"popups": 1}
driver=webdriver.Chrome(executable_path="C:\\Users\\karen.castillo\\PycharmProjects\\focusservicestest\\utilities\\chromedriver.exe", options=option)
driver.maximize_window()
driver.get("https://www.google.com")

# Google search tab and redirect to google result page
time.sleep(5)
driver.find_element_by_class_name("gLFyf").send_keys("Focus Services")
time.sleep(5)
driver.find_element_by_class_name("gNO89b").click()

#validate if the URL exists and click to Focus Home Page
time.sleep(5)
url = driver.find_element_by_css_selector("cite[class*='iUh30 Zu0yb tjvcx']").text
assert "https://www.focusservices.com" in url, "https://www.focusservices.com does not exist"
print("This url exists: {}".format(url))
driver.find_element_by_css_selector("cite[class*='iUh30 Zu0yb tjvcx']").click()

#Validate if the Hiring button exists
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
print(title3)

driver.close()

















