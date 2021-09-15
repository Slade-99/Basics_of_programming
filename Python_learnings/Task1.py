

first_name = open("D:\COURSE\Projects\Class\Extras\First Name.txt", "r")

x = first_name.read()

list_1 = x.split("\n")



last_name = open("D:\COURSE\Projects\Class\Extras\Last Name.txt", "r")

y = last_name.read()

list_2 = y.split("\n")


new = open("final.txt" , "w")


for i,j in zip(list_1,list_2):
    new.write(f"{i} {j} \n")
    


