a = [ 55 ,17 , 84, 35 , 2 , 54]
b = a[0]
for fx in a:
    if fx<b:
        b=fx
print(b)        
#Minimum value is printed


c = a[0]
for fx in a:
    if fx>c:
        c=fx
print(c)     
#Maximum value is printed

x=1
while True:
    if x==5: break
    print(x)
    x +=1 
#Prints only 1,2,3,4 ...Infinite loop is stooped due to "break"



while True:
    user_name = input("Please enter the username\n")
    if user_name == "Jason":
        print("Welcome,Jason")
    else:
        print("Username incorrect . Please try again")
        continue    
    while True:
        user_pass = int(input("Please enter your passoword\n"))
        if user_pass == 123:
            print("Access granted")
            break
        else:
            print("Access denied . Please try again")
            continue
    break
        


################ Functions #################################


def fx(name):
    print("Hello" , name)


fx("Mr.X")    


print("Enter the numbers to be added")
function_1 = lambda a , b ,c :  a+b+c
    
a =int(input())
b =int(input())
c =int(input())
print(function_1(a,b,c))
#Addition of 3 numbers





def star(name):
    name_dict = {"Ronaldo":5 , "Messi":4 , "Neymar":9 , "Hazard":3 , "Aguero":6 , "Kane":12 }
    c = name_dict.get(name)
    return print(f"{c} Hours of training left")


c = input("Enter the name of the player")
star(c)



