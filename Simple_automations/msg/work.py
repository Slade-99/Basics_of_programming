### Messenger Automation
import os
import sys
import time
import getpass
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class MsgBot:
    
    def __init__(self,username,password):
        # Login info
        self.username = username
        self.password = password
        
        #Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        
        #Driver path
        driver_path = os.path.join(os.getcwd() , 'chromedriver.exe')

        self.driver = webdriver.Chrome(executable_path=driver_path )


    def login(self):
        #go to site
        login_link = 'https://www.messenger.com/'
        self.driver.get(login_link)
        self.wait(5, '//*[@id="loginbutton"]')
        
        
        #username_field
        username_field = self.driver.find_element(By.XPATH,'//*[@placeholder="Email address or phone number"]')
        #password_field
        password_field = self.driver.find_element(By.XPATH,'//*[@placeholder="Password"]')
        #login button
        login_button = self.driver.find_element(By.XPATH,'//*[@id="loginbutton"]')

        #Fill 
        username_field.send_keys(self.username)
        password_field.send_keys(self.password)
        
        #Wait
        time.sleep(3)

        #Click
        login_button.click()


    def find_recepient(self,name):
        self.wait(5, '//*[@placeholder="Search Messenger"]')
        
        #Search bar
        search_bar = self.driver.find_element(By.XPATH,'//*[@placeholder="Search Messenger"]')
        time.sleep(2)
        #Fill
        search_bar.send_keys(name)
        time.sleep(3)
        #select
        search_bar.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        search_bar.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        search_bar.send_keys(Keys.ENTER)
        
        
       
    def send_text(self,text):  
        # text box
        text_box = self.driver.find_element(By.XPATH,'//*[@class="_1mf _1mj"]')
        text_box.send_keys(text)
        text_box.send_keys(Keys.ENTER)



    def wait(self, seconds:int , element:str):
        WebDriverWait(self.driver, seconds).until(lambda x: x.find_element(By.XPATH, element))



def main(username,password,recepient,text):
    My_bot = MsgBot(username,password)
    My_bot.login()
    time.sleep(5)
    My_bot.find_recepient(recepient)
    time.sleep(5)
    My_bot.send_text(text)
    time.sleep(50)

if __name__ == "__main__":
    username = input('Enter username/number')
    password = getpass.getpass('Enter Password')
    recepient = input("Enter the name of the recepient")
    text = input('Enter the text')
    main(username,password,recepient,text)



