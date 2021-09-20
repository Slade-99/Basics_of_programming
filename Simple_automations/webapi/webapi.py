import os 
import subprocess
import requests
import pprint
import json
import time
import base64

#os.system('.\chromedriver.exe --port=1234')
class WebAPI:
    subprocess.Popen(['.\chromedriver.exe', '--port=1234'])
    ## IP for local host
    def __init__(self):
        self.ip = 'http://127.0.0.1'
        self.port = "1234"
        self.sessionID =" "
        self.url = self.ip + ":" + self.port + "/session"
        self.headers = {

            "Content-Type" : "application/json"
        }
        
    

        


        data = {
            "capabilities" : {
                "acceptInsecureCerts" : True
                }
        }

        res = requests.post(self.url  , headers=self.headers , json=data)

        # pprint.pprint(res.json())

        self.sessionID = res.json().get('value').get('sessionId')
        # print(sessionID)

        time.sleep(3)

        return None




    ## Going to goolge .com


    def get(self,link):
        data = {'url' : link}

        res_2 = requests.post(self.url + "/" +self.sessionID +"/url", headers=self.headers , json=data)

        # pprint.pprint(res_2.json())


        time.sleep(3)
    ### Take screenshot

    def screenshot(self,name):
        res_3 = requests.get(self.url + "/" +self.sessionID +"/screenshot", headers=self.headers)

        # pprint.pprint(res_3.json())


        ##saving in a file

        with open(name+".jpg" , "wb") as f:
            
            f.write(base64.urlsafe_b64decode(res_3.json().get('value')))