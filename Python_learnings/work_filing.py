import os
import sys

os.chdir("D:\Regular\Course\Projects\Class")
with open("num1.csv" , "r") as f:

    x = f.read()
   
    each_row = x.split("\n")
    labels = each_row[0]
    each_user = each_row[1:]
    user_names = []
    
    def find_user_details():
        for i in each_user:
            m = i.split(",")
            user_names.append(m[0])

        name_dict = {a:b for a,b in zip(user_names,each_user)}    

        user_input = input("Enter your username to retrieve all the informations\n")
        
        if user_input not in user_names:
            sys.stderr.write("User not found")
        else: 
            print(labels)
            print((name_dict[user_input]).replace("," , "-"))


    find_user_details()    
    
sys.exit()     