'''
Name : Azwad Aziz
Session : 3
Batch : N-212-2
'''
#########LISTS#############################
var_1 = [ "ten" , "twenty" , "thirty" , "forty" , "fifty" , "sixty" , "seventy" , "eighty"]

var_2 = [ 10 , 20 , 30 , 40 ,50 , 60 , 70 , 80]

var_3 = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j"]

var_4 = ["Python" , "C" , "C++" , "Java" , "C#" , "PHP" , "Assembly" , "Ruby" , "C"]

var_5 = [10 , 20 , 30 , 40 , "Python" , "C" , "C++" , "Java" ]

combine_1 = [ var_1 , var_2 , var_3 , var_4 , var_5]

var_5.reverse()
print(var_5)
print()
x = var_1.copy()
var_1.sort(reverse=True)
print(var_1)
print(x)

print( combine_1[0][3::2])

var_2.append(90)
print(var_2)

var_3.insert( 3 , 20 )
print(var_3)

var_2.extend(var_3)
print(var_2)

var_4.remove("C")
print(var_4)

print(var_4.index("C",2))

del var_4[7]
print(var_4)

var_4.pop()
print(var_4)

print(var_4.count("C"))




#########STRING##########################

text_1 = "ABcdER GFR23Aa"
text_5 = "stqea\tasdasd"
text_3 = "abc abd cde"
text_4 = text_3[0:2]
text_2 = text_1[0]
text_6 = "1231357"
group_1 = [ "a" , "b" , "c"]
a=10
b=20
text_7 = "in"

print(text_1.capitalize())


print(text_1.casefold())

print(text_1.center(50 , "x") )

print(text_3.count(text_4 , 0 , 9 ))

print(text_1.endswith("23Aa" , 7 ,14 ))

print(text_5.expandtabs(tabsize=15))

print(text_1.find("A" , 7 ,-1))

print("fine tune the {} {} ".format(a,b))

print(text_1.index("A" , 2 ,-1))

print(text_1.isalnum())

print(text_1.isalpha())

print(text_6.isdecimal())

print(text_1.isascii())

print(text_6.isdigit())

print(text_7.isidentifier())

print(text_1.islower())

print(text_6.isnumeric())

print(text_1.isupper())

print(text_5.isprintable())

print(text_3.isspace())

print(text_1.istitle())

print(text_2.join(text_1))

print(text_3.ljust(20,"Y"))

print(text_3.rjust(20,"Y"))

print(text_1.lower())

print(text_1.upper())

print(text_1.swapcase())

print(text_3.strip("ab"))

print(text_3.rstrip("de"))

print(text_3.lstrip("ab"))

print(text_3.partition(" "))

print(text_3.rpartition(" "))