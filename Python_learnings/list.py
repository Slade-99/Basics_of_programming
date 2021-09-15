# list[Start : Upto(excluding) : Step]

#append(self,object,/) -> append object to the end of the list

#insert(self,index,object,/) -> insert object at index

#extend(self,interable,/) -> Extend the list by appending elemnts form the iterable

#remove(self, value,/) -> Remove first occurence of value

#del list[index] ->  Delete the indexed object

#clear(self,/) -> Remove all items from list

#pop(self, index= -1 , /) ->Remove and return item at the end

#count(self,value,/) -> Return the number of occurences of a value

#index(self,value, start=0 , stop = 9223372036854775807 ,/)
#      return the 1st index of a value 
#       raises ValueError if the value is not present

#copy(self,/) -> Return a shallow copy of the list

#reverse(self,/) -> Reverse *IN PLACE*

#sort(self , / , * , key=None , reverse=False) not possible for str and int mixed lists
#   sort the list in ascending order and return None

var_1 = [ "ten" , "twenty" , "thirty" , "forty" , "fifty" , "sixty" , "seventy" , "eighty"]

var_2 = [ 10 , 20 , 30 , 40 ,50 , 60 , 70 , 80]

var_3 = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j"]

var_4 = ["Python" , "C" , "C++" , "Java" , "C#" , "PHP" , "Assembly" , "Ruby" , "C"]

var_5 = [10 , 20 , 30 , 40 , "Python" , "C" , "C++" , "Java" ]

combine_1 = [ var_1 , var_2 , var_3 , var_4 , var_5]


var_5.reverse()
print(var_5)

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





