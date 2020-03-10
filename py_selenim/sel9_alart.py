from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
#http://testautomationpractice.blogspot.com/
driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)
#driver.switch_to_alert().accept() #closes window by OK button
driver.switch_to_alert().dismiss() #closes window by cancel button