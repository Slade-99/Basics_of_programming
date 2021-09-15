print("Enter any number")

user_i= input()

user_i = int(user_i)
x= user_i*100

a=float(x)

print("The number you entered x 100 equals to  " +  str(x) )
print(" The number you entered in decimal places is" + str(a))
 


## If the user enters a floating point number then it will be stored as a string but the int() function
## in line 5 cannot evaluate it    