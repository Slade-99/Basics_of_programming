# These are magic methods/dunder methods . They are built-in . Python calls them automatically
# the def __init__ is called the constructor which is used to takes inputs for the class
# the def __del__ or del __delattr__ is the destructor is used to clean the class and python does it automatically
# the def__iter__ method makes the object an iterator
# the def__next__ method is used to access the next values
# the def __repr__ method is used to print the object


# Making an iterable class like range
# import sys
# class Group:

#     def __init__(self,b):
#         self.b = b
#         self.c = -1


#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.b >=0:
#             if self.c< self.b:
#                 self.c += 1
#                 return self.c
#             else:
#                 raise sys.exit()
#         else:
#             raise StopIteration("Invalid Input")

#     def __repr__(self):
#         return str(self.b)

# myiter = Group(10)
# print(myiter)
# for i in myiter:
#     print(i)

# Making an iterable class like reverse of range
class Group:

    def __init__(self,b):
        self.b = b+1
        


    def __iter__(self):
        return self

    def __next__(self):
        if self.b>0:
            self.b -= 1
            return self.b
        else:
            raise StopIteration

myiter = Group(7) 
# print(myiter.__next__() , myiter.__next__() ) 

for i in myiter:
    print(i)       

# The Generator function can also work like iterator
# yield makes it work like iterable object
# If we use return then value is returned and the function is exitted but using yield returns a value but the function is not exitted

# def itero(x):
    
#     while x>=0:
#         yield x
#         x -= 1


# for i in itero(10):
#     print(i)


