'''
Written by: Azwad Aziz
-------------------------

This program is only used to detect whether a file is malicious or not.
The program uses the VirusTotal V3 REST API
Note that the file must be less than 32MB
Please keep this script in the same directory as the file which is to be tested.
Must have internet connection

'''

import time
import requests
import re
import sys

class Viruscheck:

    def __init__(self,headers,file_name):
        self.headers=headers
        self.file_name=file_name


   
    def post_file(self):
    
        #Post the file in VirusTotal

        try:
            file= {'file' : open(f'{self.file_name}' , 'rb')}

            id_response = requests.post('https://www.virustotal.com/api/v3/files', headers=self.headers , files=file)
            self.id_response = id_response
        
        except FileNotFoundError:
            print('File not found. \n Please enter your filename correctly and try again')
            time.sleep(1)
            sys.exit()

    def retrieve_id(self):
        
        # Retrieve the id of the posted file
        
        style = re.compile(r'".+?"')

        result = style.findall(self.id_response.text)
        self.id = result[-1][1:-1]


        

    def retrieve_sha256(self):
        
        #Retrieve the sha256 id of the posted file
        
        res_2 = requests.get(f'https://www.virustotal.com/api/v3/analyses/{self.id}' , headers=self.headers)

        

        style_2 = re.compile(r'"sha256": ".+?"')
        self.id_sha256 = style_2.findall(res_2.text)[0][11:-1]

    def final_outcome(self):


        # Evaluate whether the posted file is malcious or not

        res_3 = requests.get(f'https://www.virustotal.com/api/v3/files/{self.id_sha256}' , headers=self.headers)

        style_3 = re.compile(r'"malicious": \d{1,2}')


        result_3=style_3.findall(res_3.text)[1]


        if result_3 == '"malicious": 0':
            print('The file is free from virus')
        else:
            print("The file is malicious")


if __name__ == "__main__":
    file_name = input('Enter the name of the file and also the extension\n')
    api_key = input('Enter your x-api key\n')
    
    
    headers = {
        'x-apikey': api_key ,
    }
    
    
    attempt = Viruscheck(headers,file_name)

    attempt.post_file()
    attempt.retrieve_id()
    attempt.retrieve_sha256()
    attempt.final_outcome()
