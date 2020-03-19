from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

#chromeOptions = Options()
#chromeOptions.add_experimental_option("pref",{"download.default_directory":"c:\Downloadedfiles"})

driver = webdriver.Chrome() # give executabe_path = "driver_.exe" path
driver.get("http://demo.automationtesting.in/FileDownload.html")
#driver.get("https://b-ok.cc/book/3560761/2f7e48")

driver.maximize_window() # maximze the window

driver.find_element_by_id("textbox").send_keys("testing download file")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()
