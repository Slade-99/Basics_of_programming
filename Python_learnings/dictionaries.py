# Is is an iterable and mutable object with python written with second brackets and colons are used
# Values are not accessed with index . Instead the Keys are used
# 
#
#
#
# .clear() clear e dictionary
# .copy() get a copy 
# .fromkeys(keys taken form the iterable , fixed values of all the keys)
# .get(key) used to get the value of a key . Dont use index method by passing key dict_1[keys] will 
#  give exception error if a key is not present but the get function will not generate any errors
#  x= dict_1.get(key , value) if the key is not value will be assigned to x
# .setdefault( key , value) if a key is not present the value will be key value pair will be updated 
# .items() shows all the pairs of key and values present in a dictionary
# .keys() used to get all the keys
# .pop()  used to remove any desired key value pair 
#  del(dict_1[key])  is another that is used to remove any desired key value pair 
# .popitem() pops the last item of a dictionary
# .update({key : value }) update a dictionary with key and value pairs
# another way to update dict_1[key] = value
# .values() to get all the values

dict_1 = { 1 : "a" , 2 : "b" , 3 : "c" , 4 : "d"}
dict_2 = { 9: "x" , 10 : { 11 : "y" , 12 : "z" } }

list_1 = [ 12 , 13 , 14 , 15]
list_2 = [ "January" , "February" , "March" , "April"]




print(dict_1)

#print(dict_1.keys())

#print(dict_1.values())

#dict_1.clear()
#print(dict_1)

dict_3 = dict_1.copy()
#print(dict_3)

#print(dict_1.items())

dict_3.popitem()
#print(dict_3)

#print(dict_1.get(1))

dict_1.update({ 5 : "e" })
#print(dict_1)

dict_1[6] = "f"
#print(dict_1)

dict_1.pop(5)
#print(dict_1)

del(dict_1[2])
#print(dict_1)

#print(dict_2)
#print(dict_2[10][12])
#print(dict_2.get(10).get(11))

dict_4 = {i:j for i,j in zip(list_1,list_2)}
#print(dict_4)

dict_5= dict_4.fromkeys(list_1 , "rrr")
#print(dict_5)


x = dict_1.get(4 , 10)
#print(x)

y= dict_1.get(9 , "ttt")
#print(y)
#print(dict_1)

z = dict_1.setdefault(3 , "qwr")
#print(z)
#print(dict_1)

m = dict_1.setdefault(2 , "qwr")
#print(m)
#print(dict_1)
