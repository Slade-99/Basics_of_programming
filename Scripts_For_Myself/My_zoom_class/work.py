######    Script For My Own Zoom Classes   ######


from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import pyperclip
import time
import os
# __link = 'https://us04web.zoom.us/j/4534726949?pwd=YzhHYmNRT0ZVT3hjdEViQ29WTmVVdz09'
# __meetingID = '453 472 6949'
# __passcode = '00001111'
# __messenger = 'https://www.messenger.com/'



class Zoom:


    def __init__(self):
        
        #Login info
#        self.username = username
#        self.password = password


        #Driver
        driver_path = os.path.join(os.getcwd() , 'chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path=driver_path)




    def start_zoom(self):
        self.driver.get('https://us04web.zoom.us/j/4534726949?pwd=YzhHYmNRT0ZVT3hjdEViQ29WTmVVdz09')
        time.sleep(5)
        Alert(self.driver).accept()
        time.sleep(5)






















def main():
    jarvis = Zoom()
    jarvis.start_zoom()







if __name__ == "__main__":
    
    main()


