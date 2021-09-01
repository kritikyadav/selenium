from selenium import webdriver
driver=webdriver.Chrome(executable_path="D:\codings\selenium\chromedriver.exe")
driver.maximize_window()
driver.get("https://en-gb.facebook.com/")
print("Title:",driver.title)
print("Current page url:",driver.current_url)

driver.get("https://google.com/")
print("Title:",driver.title)
print("Current page url:",driver.current_url)
driver.back()
print("Current page url:",driver.current_url)
driver.forward()
print("Current page url:",driver.current_url)
##driver.close()

##Webdriver locator
##driver.find_element_by_name("email").send_keys("kritikyadav2810@gmail.com")
##driver.find_element_by_name("pass").send_keys("123343526")

