from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://www.bcbsil.com/provider/network/join_bcbsil_network.html")
##driver.implicitly_wait(15)
driver.find_element_by_link_text("Provider Onboarding Form").click()
time.sleep(10)
pw = driver.window_handles[02]
childwindow = driver.window_handles[1]

driver.switch_to.window(childwindow)
driver.find_element_by_css_selector("div[role='dialog']")
driver.find_element_by_css_selector("svg.wm-ignore-css-reset").click()

logo = driver.find_element_by_class_name("sr-only").text
assert logo == "Blue Cross and Blue Shield of Illinois"
print(logo)
driver.close()
driver.switch_to_window(pw)
driver.close()

##driver.find_element_by_id("488bfe6a-64a7-f480-4f66-27ea42a687a5").click()
