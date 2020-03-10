from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome() # give executabe_path = "driver_.exe" path
driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
print(driver.current_window_handle) #CDwindow-1D5CBD254F3D05E0856EC69B43A6B361 --> parent window
handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close() #close only parent browser

driver.quit()
