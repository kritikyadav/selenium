from selenium import webdriver
f=open('1.txt','r')
lid=f.readline()
p=f.readline()
print(lid)
print(p)

f.close()

driver=webdriver.Chrome(executable_path= "D:\codings\selenium\chromedriver.exe")
driver.maximize_window() 
driver.get("https://www.facebook.com/")
driver.find_element_by_name("email").send_keys(lid)
driver.find_element_by_xpath("//input[@type='password']").send_keys(p)
