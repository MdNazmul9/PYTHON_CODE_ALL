from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.newtours.demoaut.com/")
driver.save_screenshot("C:/screenshot/homeage.png")