from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
#https://fs2.formsite.com/52x0p8/form1/index.html?fbclid=IwAR2as7_1EZ6iBJ8LzKYKyifnM3MPzpDgl9qxTd51lydm_eHwIxUU3zs_j7o
#https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
element = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(element)

drp.select_by_visible_text("Morning")
#drp.deselect_by_index(2)
#drp.select_by_value("Radio-2")

#count nmber of options
print(len(drp.options))
#capture all options
all_options = drp.options
for option in all_options:
    print(option.text)
