'''
Name : Azwad Aziz
Session : 3
Batch : N-212-2
'''

##############  TUPLE #########################

abc = ( "meteor" , "comets")

xyz = ("star" , "planet" , "asteroids" , "moon" , "planet")

print(xyz)
#output = ('star', 'planet', 'asteroids', 'moon', 'planet')

print(xyz.count("planet"))
#output = 2

print(xyz.index("planet" , 2 , ) )
#output = 4

xyz += ("meteor", )
print(xyz)
#output =  ('star', 'planet', 'asteroids', 'moon', 'planet', 'meteor')

xyz += abc
print(xyz)
#output = ('star', 'planet', 'asteroids', 'moon', 'planet', 'meteor', 'meteor', 'comets')




#######################   SETS  ##################################

set_1 = {"a" , "b" , "c" , "d"}

set_2 = {"a" , "b" , "d"}

set_10 = {"y", "x" , "z"}

set_11 = {"x" ,"z" }

print(set_1 , set_2)
#output = {'b', 'c', 'a', 'd'} {'b', 'a', 'd'}

set_1.add("xt")
print(set_1)
#output = {'c', 'd', 'xt', 'b', 'a'}

set_3 = set_1.copy()
print(set_3)
#output = {'xt', 'c', 'b', 'a', 'd'}

set_4 = set_1.difference(set_2)
print(set_4)
#output = {'xt', 'c'}

set_1.difference_update(set_2)
print(set_1)
#output = {'c', 'xt'}

set_1.discard("xt")
print(set_1)
#output =  {'c'}

set_5 = set_2.intersection(set_1)
print(set_5)
#output = set()

set_2.intersection_update(set_1)
print(set_2)
#output = set()

print(set_10.isdisjoint(set_11))
#Output = Flase

print(set_11.issubset(set_10))
#Output = True

set_2.clear()
print(set_2)
#Output = set()

print(set_1.issuperset(set_2))
#Output = True

set_3.pop()
print(set_3)
#output = {'a', 'b', 'xt', 'c'}

set_3.remove("a")
print(set_3)
#output = {'b', 'xt', 'c'}

x = set_4.symmetric_difference(set_1)
print(x)
#output = {'xt'}

set_4.symmetric_difference_update(set_1)
print(set_4)
#output = {'xt'}

set_9 = set_1.union(set_4)
print(set_9)
#output = {'c', 'xt'}

set_9.update(set_1)
print(set_9)
#output = {'c', 'xt'}



############### Dictionaries ##########################################

dict_1 = { 1 : "a" , 2 : "b" , 3 : "c" , 4 : "d"}
dict_2 = { 9: "x" , 10 : { 11 : "y" , 12 : "z" } }

list_1 = [ 12 , 13 , 14 , 15]
list_2 = [ "January" , "February" , "March" , "April"]




print(dict_1)
#output = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

print(dict_1.keys())
#output = dict_keys([1, 2, 3, 4])

print(dict_1.values())
#output = dict_values(['a', 'b', 'c', 'd'])


dict_3 = dict_1.copy()
print(dict_3)
#output = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

print(dict_1.items())
#output = dict_items([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')])

dict_3.popitem()
print(dict_3)
#output = {1: 'a', 2: 'b', 3: 'c'}

print(dict_1.get(1))
#output = a

dict_1.update({ 5 : "e" })
print(dict_1)
#output = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

dict_1[6] = "f"
print(dict_1)
#output = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}

dict_1.pop(5)
print(dict_1)
#output = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 6: 'f'}

del(dict_1[2])
print(dict_1)
#output = {1: 'a', 3: 'c', 4: 'd', 6: 'f'}

print(dict_2)
#output = {9: 'x', 10: {11: 'y', 12: 'z'}}

print(dict_2[10][12])
#output = z

print(dict_2.get(10).get(11))
#output = y

dict_4 = {i:j for i,j in zip(list_1,list_2)}
print(dict_4)
#output =  {12: 'January', 13: 'February', 14: 'March', 15: 'April'}

dict_5= dict_4.fromkeys(list_1 , "rrr")
print(dict_5)
#output = {12: 'rrr', 13: 'rrr', 14: 'rrr', 15: 'rrr'}


x = dict_1.get(4 , 10)
print(x)
#output = d

y= dict_1.get(9 , "ttt")
print(y)
#output =ttt

print(dict_1)
#output = {1: 'a', 3: 'c', 4: 'd', 6: 'f'}

z = dict_1.setdefault(3 , "qwr")
print(z)
#output = c
print(dict_1)
#output = {1: 'a', 3: 'c', 4: 'd', 6: 'f'}

m = dict_1.setdefault(2 , "qwr")
print(m)
#output = qwr

print(dict_1)
#output = {1: 'a', 3: 'c', 4: 'd', 6: 'f', 2: 'qwr'}

dict_1.clear()
print(dict_1)
#output = {}