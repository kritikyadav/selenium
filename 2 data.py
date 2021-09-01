from selenium import webdriver
driver=webdriver.Chrome(executable_path="D:\codings\selenium\chromedriver.exe")
driver.maximize_window()
driver.get("file:///C:/Users/Kritik%20Yadav/OneDrive/Desktop/forms/login.html")

driver.find_element_by_xpath("/html/body/form/input[1]").send_keys("Kritik Yadav")
driver.find_element_by_xpath("/html/body/form/input[2]").send_keys("Vishnu Kumar Aheer")
driver.find_element_by_xpath("/html/body/form/input[3]").send_keys("kritik@gmail.com")
driver.find_element_by_xpath("/html/body/form/input[4]").send_keys("123 bulding Kota")
driver.find_element_by_xpath("/html/body/form/input[5]").send_keys("12345678abCD@")
driver.find_element_by_xpath("/html/body/form/input[6]").send_keys("Male")
driver.find_element_by_xpath("/html/body/form/button").click()
print("work submited")
driver.get("http://127.0.0.1:5500/page.html")
