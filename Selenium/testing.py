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
driver.get("https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%221231%22%2C%222522622%22%5D")
while True:
    count=0
    time.sleep(3)
    #Loads all the connect button into an array
    connect=driver.find_elements_by_css_selector(".search-result__actions--primary.button-secondary-medium.m5")
    for each in connect:
        count+=1
        if count==4 or count==8:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        if not each.is_enabled():
            continue
        each.click()
        time.sleep(2)
        try:
            popup=driver.find_element_by_css_selector(".button-primary-large.ml1")
            popup.click()
            time.sleep(2)
        except:
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    next_button = driver.find_element_by_css_selector(".next")
    next_button.click()
    time.sleep(5)

print(connect)
time.sleep(10)

time.sleep(10)
assert "No results found." not in driver.page_source
driver.close()