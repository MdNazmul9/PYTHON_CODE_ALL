from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("C:/Users/User/Desktop/Day1/index.html")


fname = driver.find_element_by_id("firstName")
fname .send_keys("Nazmul")


lname = driver.find_element_by_id("lastName")
lname .send_keys("Hossain")

eml = driver.find_element_by_id("exampleInputEmail1")
eml .send_keys("naz@gmail.com")

phn = driver.find_element_by_id("phone")
phn.send_keys("123444444")

#print(fname .is_displayed())
#print(fname .is_enabled())
#fname .send_keys("Nazmul")







"""
pwd_ele = driver.find_element_by_name("password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

user_ele.send_keys("Nazmul")
pwd_ele.send_keys("nazmul123456")"""

#driver.find_element_by_name("login").click()
