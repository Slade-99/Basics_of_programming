import requests
import os
def main(name):
  os.chdir("D:\COURSE\Projects\Class")
  with open("./Extras/"+ name + ".py" , "r") as f:
    x = f.read()
  info = {
    'poster' : "Azwad Aziz" ,
    'syntax' : "python3" , 
    'content' : x
  }
  a = requests.post("https://paste.ubuntu.com/" , data = info )
  print (a.url)

main(input("Enter the name of the python file to generate the pastebin link\n"))