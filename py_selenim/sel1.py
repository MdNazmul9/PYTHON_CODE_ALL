from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome() # give executabe_path = "driver_.exe" path
driver.get("https://www.python.org/") # j website e search korbo sei website
print(driver.title) # title of the page
print(driver.current_url) # return the current url of the page
#print(driver.page_source) # return the html code of the page
driver.close() # close the browser
