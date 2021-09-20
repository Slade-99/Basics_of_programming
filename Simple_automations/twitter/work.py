import os 
import sys 
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

#### Full Xpath and Xpath are known as absolute xpath
####

class TwitterBot:
    def __init__(self,username,password) -> None:
        
        # Twitter username and password
        self.username =username
        self.password = password
        
        # Driver Location for Selenium
        if sys.platform == "linux":
            driver_path = os.path.join(os.getcwd(), 'chromedriver')
        elif sys.platform == 'win32':
            driver_path = os.path.join(os.getcwd(), 'chromedriver.exe')

        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self) ->None:
        #Login url
        login_url = 'https://twitter.com/login'
       
        # Open login page
        self.driver.get(login_url)

        #Sleep for page to load
        self.wait(5, '//div[@role="button"]')

        # Username field
        username_field = self.driver.find_element(By.NAME,'session[username_or_email]')
        # Password field
        password_field = self.driver.find_element(By.NAME, 'session[password]')
        # Login button
        login_button = self.driver.find_element(By.XPATH,'//div[@role="button"]')

        #Fill in username
        username_field.send_keys(self.username)
        #Fill in password
        password_field.send_keys(self.password)
        #Click login button
        login_button.click()

        #Keyboard Enter Press
        password_field.send_keys(Keys.ENTER)
        


    def wait(self, seconds:int , element:str):
        WebDriverWait(self.driver,seconds).until(lambda driver:driver.find_element(By.XPATH,element))
        
        
def main(username,password):
    bot = TwitterBot(username,password)
    bot.login()
    time.sleep(30)



if __name__=='__main__':
    username = input('Enter your username\n')
    password = getpass.getpass('Enter your password\n')
    main(username,password)
        











    