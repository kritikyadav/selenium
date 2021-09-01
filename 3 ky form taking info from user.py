from selenium import webdriver
import time

fn=input("First Name: ")
mn=input("middle name: ")
ln=input("Last Name: ")
dad=input("Father's name: ")
dobd=input("enter day of dob: ")
dobm=input("enter month of dob: ")
doby=input("enter year of dob: ")
cast=input("enter genrel/obc/sc/st: ")
gender=input("enter gender male/female: ")
address=input("enter your address: ")
city=input("enter your city: ")
state=input("enter state: ")
pin=input("enter pin code: ")
mno=input("enter mobile no.: ")
email=input("enter email id: ")
dd=input("enter DD: ")
bank=input("enter bank name: ")
amount=input("enter amount: ")
dod=input("enter day of date: ")
dom=input("enter month of date: ")
doy=input("enter year of date(2010-2020): ")
p10=input("enter 10th class percentage: ")
p12=input("enter 12th class percentage: ")
pg=input("enter graduation percentage: ")
ppg=input("enter post graduation percentage: ")




driver=webdriver.Chrome(executable_path="D:\codings\selenium\chromedriver.exe")
driver.maximize_window()
driver.get("http://127.0.0.1:5500/KY%20form1.html")

driver.find_element_by_name("fn").send_keys(fn)
driver.find_element_by_name("mn").send_keys(mn)
driver.find_element_by_name("ln").send_keys(ln)
driver.find_element_by_name("dad").send_keys(dad)
driver.find_element_by_name("date").send_keys(dobd)
driver.find_element_by_name("month").send_keys(dobm)
driver.find_element_by_name("year").send_keys(doby)
driver.find_element_by_name("category").send_keys(cast)
if(gender=="male"):
    driver.find_element_by_id("male").click()
elif(gender=="female"):
    driver.find_element_by_id("female").click()
driver.find_element_by_id("address").send_keys(address)
driver.find_element_by_id("city").send_keys(city)
driver.find_element_by_id("state").send_keys(state)
driver.find_element_by_id("pin").send_keys(pin)
## For click button page 1
time.sleep(3)
driver.find_element_by_xpath("//input[@type='button']").click()
#####################################    Next Page 2
driver.find_element_by_name("mno").send_keys(mno)
driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("dd").send_keys(dd)
driver.find_element_by_name("bank").send_keys(bank)
driver.find_element_by_name("amount").send_keys(amount)
driver.find_element_by_name("date").send_keys(dod)
driver.find_element_by_name("month").send_keys(dom)
driver.find_element_by_name("year").send_keys(doy)
## For Click button page 2
time.sleep(3)
driver.find_element_by_xpath("//input[@type='button']").click()
######################################  Next Page 3
driver.find_element_by_name("p10").send_keys(p10)
driver.find_element_by_name("p12").send_keys(p12)
driver.find_element_by_name("pg").send_keys(pg)
driver.find_element_by_name("ppg").send_keys(ppg)

driver.find_element_by_xpath("//input[@value='c']").click()
driver.find_element_by_xpath("//input[@value='cplus']").click()
driver.find_element_by_xpath("//input[@value='c.']").click()
driver.find_element_by_xpath("//input[@value='cplus.']").click()
driver.find_element_by_xpath("//input[@value='basic.']").click()


## For click button page 3
time.sleep(3)
driver.find_element_by_xpath("//input[@value='Register']").click()

