from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.keys import Keys
#Initialising the driver
driver = webdriver.Firefox()
driver.get("https://www.linkedin.com")
elem = driver.find_element_by_id("login-email")
elem_pass=driver.find_element_by_id("login-password")
elem_submit=driver.find_element_by_id("login-submit")
elem.clear()
elem_pass.clear()
#Create a file giving username and password in two separate lines with no white spaces in the starting and end and pass its path here.
with open("C:\\Users\\varda\\OneDrive\\Desktop\\selenium.txt",'r') as f:
    uname = f.readline()
    password=f.readline()
elem.send_keys(uname)
elem_pass.send_keys(password)
elem_submit.click()
count=0
#provide any of the link of employee of linkedIn.
company_urls=["https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%2250076%22%5D&page=11"]
company_names_list=["Roku"]
driver.get(company_urls[0])
time.sleep(3)
#Loads all the connect button into an array
connect=driver.find_elements_by_class_name("search-result__wrapper")
toSkip = driver.find_elements_by_class_name("button-secondary-medium.m5.link-without-visited-state")

print(connect)
time.sleep(10)

time.sleep(10)
assert "No results found." not in driver.page_source
driver.close()