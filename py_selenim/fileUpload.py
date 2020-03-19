from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome() # give executabe_path = "driver_.exe" path
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window() # maximze the window
driver.switch_to_frame(0)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("D://41-BCS (1)+CV/Big Bazar-iD-3628.jpg")