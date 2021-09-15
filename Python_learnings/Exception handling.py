import time

# Exception handling


#prevent crashing

#First the try block is executed and it any error is found then the except block is used and the upcoming lines of codes are executed
#try
#except
#finally

# ZeroDivisionError

#try:
#    print(55/0)
#except:
#    print("There is a problem")

# You can only catch SyntaxError if it's thrown out of an eval, exec, or import operation.
# try:
#     print(eval("5===5"))
# except Exception as x:
#     print(x)    

# print(xyz)
# except ZeroDivisionError:
# print("Zero Division Error")
# except NameError:
#  print("Name Error")        

# try:
# while True:
#     print("HI")
#     time.sleep(1)
# except KeyboardInterrupt:
# print("User used keyboard")        


# To handle an error and also check its type

# try:
#     print(2/0)
# except Exception as x:
#     print(x)        
# finally:                       # code in the finally block will run even if there is or there is not any error
#     print("Error handled")     


# To intentionally use the built-in errors

# def main(a,b):
#     if a == 0 or b == 0:
#         raise NameError("Azwad")
#     return a
# print(main(5,0))




# To create custom errors
# class CustomError(Exception):

#     def __init__(self, text="Number is greater than 10"):
        
#         self.text = text
#         super().__init__(self.text)

        

    

# x = int(input("Enter a number"))

# if x>10:
#     raise CustomError()

# else:
#     print("Hi")    
