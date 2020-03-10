from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome() # give executabe_path = "driver_.exe" path
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window() # maximze the window
element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
actions = ActionChains(driver)
actions.double_click(element).perform() #Double click on the button