#file:///C:/Users/User/Desktop/Day1/index.html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome() # give executabe_path = "driver_.exe" path
driver.get("file:///C:/Users/User/Desktop/Day1/index.html")
rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
#/html/body/table/tbody/tr[1]/th
cols = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))
print("rows:", rows)
print("column:",cols)

print("Name"+"      "+"Phone"+"      "+"Email"+"      "+"Date")
#/html/body/table/tbody/tr[2]/td[1]
for r in range(2, rows+1):
    for c in range(1,cols+1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end="      ")
    print()