from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://www.bcbsil.com/provider/network/join_bcbsil_network.html")
driver.find_element_by_link_text("Provider Onboarding Form").click()
driver.implicitly_wait(10)
