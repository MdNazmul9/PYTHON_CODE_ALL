from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.implicitly_wait(5)
assert "Facebook – log in or sign up" in driver.title
driver.find_element_by_name("email").send_keys("01986231962")
driver.find_element_by_name("pass").send_keys("19191919")
driver.find_element_by_id("u_0_b").click()
#print(driver.title) 