import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("C:/Users/User/Desktop/Day1/index_OutPut.html")
url = r'file:///C:/Users/User/Desktop/Day1/index.html'
for i, df in enumerate(pd.read_html(url)):
    df.to_csv('HTML_to_CSV.csv')


df = pd.read_csv('HTML_to_CSV.csv')
df = df[~df.Name.str.contains("an")]
df.to_csv(r'without_an_inName.csv', index = False)
df = pd.read_csv('without_an_inName.csv')
ls = df.Name.str.split(',')

fName = []
lName = []

for i in range(len(ls)):
    fName.append(ls[i][0])
    lName.append(ls[i][-1])

df["FastName"] = fName
df["LastName"] = lName
df = pd.DataFrame({'First_Name': df.FastName, 'Last_Name': df.LastName, 'Email': df.Email, 'Phone': df.Phone})


for i in range(len(df)):
    fname = driver.find_element_by_id("firstName")
    fname.send_keys(df.First_Name[i])

    lname = driver.find_element_by_id("lastName")
    lname.send_keys(df.Last_Name[i])

    eml = driver.find_element_by_id("exampleInputEmail1")
    eml.send_keys(df.Email[i])

    phn = driver.find_element_by_id("phone")
    phn.send_keys(df.Phone[i])
    time.sleep(1)
    fname.clear()
    lname.clear()
    eml.clear()
    phn.clear()

driver.close()


