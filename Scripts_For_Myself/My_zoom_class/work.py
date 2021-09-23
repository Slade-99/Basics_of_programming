######    Script For My Own Zoom Classes   ######


from selenium import webdriver

import pyperclip
import time
import os
# __link = 'https://us04web.zoom.us/j/4534726949?pwd=YzhHYmNRT0ZVT3hjdEViQ29WTmVVdz09'
# __meetingID = '453 472 6949'
# __passcode = '00001111'
# __messenger = 'https://www.messenger.com/'



class Zoom:


    def __init__(self,username,password):
        
        #Login info
        self.username = username
        self.password = password


        #Driver
        driver_path = os.path.join(os.getcwd() , 'chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path=driver_path)




    def start_zoom(self):
        pass






















def main(username,password):
    jarvis = Zoom(username,password)
    jarvis.login()







if __name__ == "__main__":
    username = input("Enter your usename\n")
    password = input("Enter your password\n")
    main(username,password)


