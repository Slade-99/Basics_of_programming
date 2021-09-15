# Types of arguments of functions:

# Required/Positional argument = That must be entered and the respective position is followed
# Optional/Deafult argument= Arguemnt that is initially declared in the function but can also be reassigned  (x=10)
# Non-keyworded = Takes unknown number of inputs for a single argument . Takes in a all the inputs as a tuple   *x
# Keyworded = Takes input as  x=5 y=20 z=11 etc . Takes in a dictionary  **x

 




def fx(name):
    print("Hello" , name)


#fx("Mr.X")    


#print("Enter the numbers to be added")
function_1 = lambda a , b ,c :  a+b+c

#print( (lambda a,b : a+b) (2,3))
    
#a =int(input())
#b =int(input())
#c =int(input())
#print(function_1(a,b,c))
#Addition of 3 numbers

def star(name):
    name_dict = {"Ronaldo":5 , "Messi":4 , "Neymar":9 , "Hazard":3 , "Aguero":6 , "Kane":12 }
    c = name_dict.get(name)
    return print(f"{c} Hours of training left")


#c = input("Enter the name of the player\n")
#star(c)

def table(x,y=10):
    print(f"The multiplication table for {x} is given below")
    for g in range(1,y+1):
        print(f"{x} X {g} = {x*g} ")


#table(16,15)

def multi(*x):
    a= 1
    for g in x:
        a *= g
    return a    

a = multi(1,2,3)
#print(a)

def add(a):
    num_1 = 0
    for i in a:
        num_1 += i
    return num_1    

#g = list(map(int,input("Enter numbers to be added").split(",")))
#x= add(g)
#print(x)


#def unk(a,b,c):
#    return a,b,c
#x = unk(b=5 , c=2 , a=7)   
#print(x)


#dict_1 = {}
#def store(name,role):
#   dict_1[name] = role
#for fx in range():
#    name_1 = input("Please enter your name")
#    role_1 = input("Please enter your role")
#    x = store(name_1,role_1)
#print(dict_1)    



#def factorial(number):
#    if number==0:
#        return 1
#    else:
#        return number * factorial(number-1)

#number=int(input('Please input your number: '))
#print(factorial(number))




#  RECRUSION
#def factorial(number):
#    if number==0:
#        return 1
#    else:
#        return number * factorial(number-1)

#number=int(input('Please input your number: '))
#print(factorial(number))


#def sub(abc,num_1,num_2):
#    return abc(num_1,num_2)

#print(sub(lambda x,y:x-y , 50 ,40))    