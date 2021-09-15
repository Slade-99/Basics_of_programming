# 
# 
# 
#  Open function is used to open a file or also create
# 2.Positional/Required  arguments
# a).As a string the name of the file and location is the 1st argument
#       If the full location of life is not stated then by default python will consider it to be in the same location as the python script
#       If the file is present python will work on it and if not present python will create and then work on it
#  b). The way in which the file will be opened  (also entered as a string) 
#       The various ways are known as open types  
#       i)Read = r
#      ii)Write = w  (Will discard anything written previously and rewrite)
#         w and r and only used for txt files but if the file is in binary format
#     iii)Write = wb
#      iv)Read  = rb
#       
#      vi) Read and Write = r+ / rb+  / w+ / wb+
#      vi) Append = a (It is used to add something to and existing file)    / a+ append and read
# And always after opening the file must be closed with .close() function 
# 
# Optionasl arguments for open() function. encoding type (for example UTF-8)   for newline characters for error handling for external software
#
# open(a,b)
# 
# 
# to write in the file we will use .write() function
# to write txt simply enter the argument as a string and the txt will be written on the file
#
# .writelines() it takes iterable object as input and then writes each of the object.
# .read() is used to read a file
# .writeable() is used to check either a file is writable or not . Returns a Boolean value
# 
#
# Alternative way to open and close is to use " with "
#
#
#
#
#
# Path system of files:
# 1.Relative Path = path of the file relative to the location or folder whete the python script is present
# 2.Absolute Path =  full path of the file starting form the drive to the folders etc etc.
#




#file_1 = open("file_1.txt" , "w+" )

#file_1.write("Azwad")

#print(file_1.read())


#file_1.close()


#with open("file_1.txt" , "w") as f:
    
#    print(f.write("Azwad"))


#file_1 = open("file_1.txt" ,  "a+")


#file_1.write("\n cd")

#print(file_1.read())

#file_1.close()



      # r+ replaces the previous characters with new characters but w+ clears the whole file and then writes


      # r+ initaillly reads and the writes

      # a+ does not read

      # w+ behaves like w and clears all the existing data but does not read 


#with open("file_1.txt", "r+") as f:
#    print(f.read())
    







