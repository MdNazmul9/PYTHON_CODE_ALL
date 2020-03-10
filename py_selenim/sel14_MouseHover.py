from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome() # give executabe_path = "driver_.exe" path
driver.get("https://opensorce-demo.orangehrmlive.com")

driver.find_element_by_xpath("//*[@id='txtUsername']").clear()
driver.find_element_by_xpath("//*[@id='txtPassword']").clear()

driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()

admin = driver.find_element_by_xpath("//*[@id='menu_admin_ViewAdminModle']/b")
usermgnt = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
users = driver.find_element_by_xpath("//*[@id='menu_admin_ViewSystemUsers']")

actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(usermgnt).move_to_element(users).click().perform()