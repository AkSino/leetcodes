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
company_urls=["https://www.linkedin.com/search/results/people/v2/?keywords=Bloomberg&origin=FACETED_SEARCH"]
company_names_list=["Bloomberg"]
total_number_of_requests=40
for company in range(len(company_urls)):
    i=0
    company_name=company_names_list[company]
    driver.get(company_urls[company])
    while i<=total_number_of_requests:
        count=0
        time.sleep(3)
        #Loads all the connect button into an array
        connect=driver.find_elements_by_class_name("search-result__wrapper")
        for row in connect:
            if(i>total_number_of_requests):
                break
            each=row.find_element_by_css_selector(".search-result__actions--primary.button-secondary-medium.m5")
            try:
                toSkip=row.find_element_by_class_name("search-result__actions--primary.button-secondary-medium.m5.link-without-visited-state")
                if(toSkip!=None):
                    print("This is a message button")
                    continue
            except:
                print("not a message button")
            name=row.find_element_by_class_name("name.actor-name").text.split(" ")[0]
            count+=1
            if count==4 or count==8:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            if not each.is_enabled():
                continue
            each.click()
            time.sleep(2)
            try:
                #Button for Add a Note
                popup=driver.find_element_by_css_selector(".button-secondary-large.mr1")
                popup.click()
                time.sleep(1)
                textBox=driver.find_element_by_id("custom-message")
                if(len(name)<=15):
                    textBox.send_keys("Hi "+name+",\nHope you are doing great! I am a CS graduate student at Santa Clara University and planning to apply to a full-time position at "+company_name+". It would be great if we could have a quick chat when you are free so I can get some insight on this.  Looking forward to talking with you. \nThanks!")
                else:
                    textBox.send_keys("Hi "+name+",\nHope you are doing great! I am a CS graduate student at Santa Clara University and planning to apply to a full-time positionat "+company_name+". It would be great if we could have a quick chat when you are free so I can get some insight on this.  Looking forward to talking with you.")
                send_invitation=driver.find_element_by_css_selector(".button-primary-large.ml1")
                time.sleep(3)
                send_invitation.click()
                if not send_invitation.is_enabled():
                    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                else:
                    i+=1
                    print(i)
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