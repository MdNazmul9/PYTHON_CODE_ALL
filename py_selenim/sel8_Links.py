# How many links present in the web page
# capture all links
# click links

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://www.newtours.demoaut.com/")

links = driver.find_elements(By.TAG_NAME,"a")  # obossoi elements dite hobe
print("Number of links present :",len(links))

for link in links:
    print(link.text)

#driver.find_element(By.LINK_TEXT,"REGISTER").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()