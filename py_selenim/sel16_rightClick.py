from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome() # give executabe_path = "driver_.exe" path
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window() # maximze the window
button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
actions = ActionChains(driver)
actions.context_click(button).perform() #Double click on the button