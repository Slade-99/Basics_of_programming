# Sets are written in second bracket and items separated with commas and are iterable and can be edited but 
# they cannot one item multiple times and it is mainly used for mathematics
# they are like tuples
# 
# 
# 
# .add() Adds and  element to the set at random position
# .clear() To clear a set
# .copy() return a copy of the set 
# set_1.differnece(set_2)  means set_1  minus set_2
# set_1.differnece_update(set_2)  means set_1  minus set_2 and update the set_1 by the change
# .discard("what to discard") to remove a member of a set
# .intersection() find the intersection of two sets
# .isdisjoint() Returns True if 2 sets do not have any intersection
# .issubset() Returns True if a set is subset of another
# .issupetset() To check if a set contains another predefined set
# .symmetric_difference
# .symmetric_difference_update
# .union() take union of two sets
# .update() take union of two sets and update
# 
# 
# 
# 
#  Can we access each item of a set 
# Can we write a set within a set
# Comparion of differnece and symmetric difference







set_1 = {"a" , "b" , "c" , "d"}

set_2 = {"a" , "b" , "d"}


#print(set_1 , set_2)

set_1.add("xt")
#print(set_1)

set_3 = set_1.copy()
#print(set_3)

set_4 = set_1.difference(set_2)
#print(set_4)

set_1.difference_update(set_2)
#print(set_1)

set_1.discard("xt")
#print(set_1)

set_5 = set_2.intersection(set_1)
#print(set_5)

set_2.intersection_update(set_1)
#print(set_2)

#print(set_2.isdisjoint(set_1))

#print(set_2.issubset(set_1))

#set_2.clear()
#print(set_2)

#print(set_1.issuperset(set_2))

set_3.pop()
#print(set_3)

set_3.remove("a")
#print(set_3)

x = set_4.symmetric_difference(set_1)
#print(x)

set_4.symmetric_difference_update(set_1)
#print(set_4)

set_9 = set_1.union(set_4)
#print(set_9)

set_9.update(set_1)
#print(set_9)

