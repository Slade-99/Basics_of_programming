## https://pastebin.ubuntu.com/p/QBWJt23zjf/


import requests
import string #module to get all the characters
from bs4 import BeautifulSoup  # allows us to retrieve data from html tags
import random

def gen():
    chars = string.ascii_lowercase + "1234567890"
    mixup = "".join(random.choice(chars) for i in range(6))
    return mixup


# we send headers to expplain that the request is sent from a browser
def main(x):
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
    }
    n = 0
    
    while n<x: 
        genrator = gen()
        link = "https://prnt.sc/" + genrator
        print(link)
        received = requests.get(link  ,headers = headers)
        data = BeautifulSoup(received.text , "html.parser")
        #image = data.findAll("img") # returns all the img tags
        image = data.find("img")["src"] #returns the image source

        if image.startswith("https"):
            download = requests.get(image)   #it is in binary format
            n+=1
            with open(genrator + ".jpg" , "wb") as f:
                f.write(download.content)

main(int(input("Enter the number of random images to be downloaded\n")))




#print(received)
#print(received.status_code)
#print(received.text) to get the html response the the browser receives