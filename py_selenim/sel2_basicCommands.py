from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome() # give executabe_path = "driver_.exe" path
#driver.get("https://www.python.org/") # j website e search korbo sei website
#http://demo.automationtesting.in/Windows.html
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title) # title of the page
print(driver.current_url) # return the current url of the page
#print(driver.page_source) # return the html code of the page

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)
# close --> closed crrently focsed browser
driver.close() # close the browser #close command can close one browser at a time.
#driver.quit() # close all browser at a time