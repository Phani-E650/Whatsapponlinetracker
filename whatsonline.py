from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from playsound import playsound
import time
import os

# XPath selectors
#Xpath is not unique inspect the element and change it with the one you get
NEW_CHAT_BTN = '/html/body/div/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[2]/div/span'
INPUT_TXT_BOX = '/html/body/div/div[1]/div[1]/div[2]/div[1]/span/div[1]/span/div[1]/div[1]/div/label/div/div[2]'
ONLINE_STATUS_LABEL = '/html/body/div/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[2]/span'

# Replace below path with the absolute path
browser = webdriver.Chrome('chromedriver.exe')

#enter the person you want to track
person="delete sanple"

# Load Whatsapp Web page
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser, 600)

#wait until new chat button is visible
new_chat_title = wait.until(EC.presence_of_element_located((By.XPATH, NEW_CHAT_BTN)))

new_chat_title.click()
#wait until input text box is visible

input_box = wait.until(EC.presence_of_element_located((By.XPATH, INPUT_TXT_BOX)))
time.sleep(0.5)

#searching for the person
input_box.send_keys(person)
time.sleep(1)
input_box.send_keys(Keys.ENTER)
time.sleep(5)


os.system("cls")
while(True):
    try:
        browser.find_element_by_xpath(ONLINE_STATUS_LABEL)
        print("classmate is online")
        playsound('audio.mp3')
        time.sleep(10)
    except:
        print("classmate is offline")
        time.sleep(10)




