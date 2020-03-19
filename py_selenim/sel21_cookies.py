from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

cookie = {'name':'MyCookie','value':'12346790'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
driver.delete_cookie('MyCookie')

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)