from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="D:\codings\selenium\chromedriver.exe")
driver.maximize_window()
driver.get("http://127.0.0.1:5500/KY%20form1.html")

driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[1]/td[2]/input").send_keys("Kritik")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[2]/td[2]/input").send_keys("")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[3]/td[2]/input").send_keys("Yadav")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[4]/td[2]/input").send_keys("Vishnu Kumar Aheer")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[5]/td[2]/select[1]").send_keys("28")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[5]/td[2]/select[2]").send_keys("October")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[5]/td[2]/select[3]").send_keys("1999")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[6]/td[2]/select").send_keys("OBC")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[7]/td[2]/input[1]").click()
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[8]/td[2]/textarea").send_keys("57 Kota Rajasthan")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[9]/td[2]/input").send_keys("Kota")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[10]/td[2]/input").send_keys("Rajasthan")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[11]/td[2]/input").send_keys("324007")
## For click button page 1
time.sleep(3)
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[12]/td/a/input").click()
#####################################    Next Page 2
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[1]/td[2]/input").send_keys("9521201621")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[2]/td[2]/input").send_keys("kritik@abc")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[3]/td[2]/input").send_keys("1000000000001")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[4]/td[2]/input").send_keys("SBI Bank")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[5]/td[2]/input").send_keys("2500000")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[6]/td[2]/select[1]").send_keys("15")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[6]/td[2]/select[2]").send_keys("June")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[6]/td[2]/select[3]").send_keys("2019")
## For Click button page 2
time.sleep(3)
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[7]/td/a/input").click()
######################################  Next Page 3
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[2]/td[2]/input").send_keys("86")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[3]/td[2]/input").send_keys("77")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[4]/td[2]/input").send_keys("70")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[5]/td[2]/input").send_keys("75")
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[6]/td[2]/input[1]").click()
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[6]/td[2]/input[2]").click()
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[6]/td[2]/input[3]").click()
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[7]/td[2]/input[1]").click()
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[7]/td[2]/input[2]").click()


## For click button page 3
time.sleep(3)
driver.find_element_by_xpath("/html/body/center/form/table/tbody/tr[8]/td/a/input").click()

