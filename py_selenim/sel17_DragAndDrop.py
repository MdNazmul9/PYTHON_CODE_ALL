from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome() # give executabe_path = "driver_.exe" path
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window() # maximze the window

source_element = driver.find_element_by_xpath("//*[@id='box3']")
target_element = driver.find_element_by_xpath("//*[@id='box106']")
actions = ActionChains(driver)
actions.drag_and_drop(source_element, target_element).perform() #Double click on the button
