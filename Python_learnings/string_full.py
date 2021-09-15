# .capitalize() return a capitalized version of a string with the 1st letter capital and rest small
# .casefold() makes all lowercase 
# .center( width , "value to insert in the string") the string will become as the specified width and 
#  make itself centered and place the values ondxccto count the number of occurences of a subtring in the main string 
#  use start and end index to specify where the search for the substring will me considerd 
#   ????encode???
# .endswith("ending" ,  start , end) to check the ending of a string. Returns Boolean type data 
# .exapndtab(tabsize=8)   used if there kjhyis tab \t in string and its size has to be changed the default is 8
# .find("what to find" , start , end) to find the 1st occurence of  something in the range .
# .rfind("what to find" , start ,end) to find the occurence of something in range =returns Highest index
# .index("what to find" , start ,end) to find the occurence of something in range 
# .rindex("what to find" , start ,end) to find the occurence of something in range =returns Highest index
# .isalnum() Returns true if the string is alpha numeric 
# .isalpha() Returns true if all characters are alphabets
# .isdecimal() Returns true if all the characters are decimal(0-9)
# .isascii()  Return true if all characters are A to z and 0-9 and some special characters
# .isdigit()  Returns true if all are digit 
# .isidentifier()  Returns true if the string is any python identifier
# .islower() Returns true if all lowercase
# .isnumric() Returns true if string is numeric
# .isupper() Returns true if all uppercase
# .isprintable() Returns true if all characters in a string is printable
# .isspace() Returns true if the string is just a space
# .istitle() Returns true if the string is title cased . Titled case means if the 1st letter of 
#  every word is capital
# .join(iterable) used to concanetate to a string from all iterable objects
# .ljust(width, fillchar) used to make the string left justified
# .rjust(width, fillchar) used to make the string right justified
# .lower() turns all uppercase into lowercase
# .upper() turns all lowercase into uppercase
# .swapcase() swaps the case
# .strip("char") used to remove character from beginned and end of a string
# .rstrip("char") used to remove character from  end of a string
# .lstirp("char") used to remove character from  end of a string
# .parition("argument") used to split a string by the given argument into a tuple
# .rparition("argument") used to split a string by the given argument from the ending into a tuple
# .replace("old string" , "new string" , count) used to replacement in a string 
# .split("split by what" ,max number of splits) used to split a string into a list
# .rsplit("split by what" ,max number of splits) used to split a string into a list from the right
# .splitlines() used to split by the \n and it True argument is passes then \n,\t these are also shown in the list 
# .startswith("starting" , start end) used to check the starting with the stated range
# .title() returns each word capitalised
# .zfill(width) makes the string to corresponding width and fills the right side with O 
# .format_map(mapping dictionary) used to map with values in the dictionary with the keys in the string

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
text_8 =" acbd\n adb\n xyz"
dict_1 = { "A" : "x" , "G" : "y" }

#print(text_1.capitalize())


#print(text_1.casefold())

#print(text_1.center(50 , "x") )

#print(text_1.endswith("23Aa" , 7 ,14 ))

#print(text_5.expandtabs(tabsize=15))

#print(text_1.find("A" , 7 ,-1))

#print("fine tune the {} {} ".format(a,b))

#print(text_1.index("A" , 2 ,-1))

#print(text_1.isalnum())

#print(text_1.isalpha())

#print(text_6.isdecimal())

#print(text_1.isascii())

#print(text_6.isdigit())

#print(text_7.isidentifier())

#print(text_1.islower())

#print(text_6.isnumeric())

#print(text_1.isupper())

#print(text_5.isprintable())

#print(text_3.isspace())

#print(text_1.istitle())

#print(text_2.join(text_1))

#print(text_3.ljust(20,"Y"))

#print(text_3.rjust(20,"Y"))

#print(text_1.lower())

#print(text_1.upper())

#print(text_1.swapcase())

#print(text_3.strip("ab"))

#print(text_3.rstrip("de"))

#print(text_3.lstrip("ab"))

#print(text_3.partition(" "))

#print(text_3.rpartition(" "))

#print(text_1.replace("A" , "x" , 1))

#print(text_1.rfind("A" , 3 , -1))

#print(text_1.index("A" , 2 , -1))

#print(text_1.rindex("A"))

#print(text_3.split(" " , 1))

#print(text_3.rsplit(" " , 1))

#print(text_8.splitlines(True))

#print(text_3.startswith(" abd" , 3 , -1))

#print(text_3.title())

#print(text_1.zfill(20))

#print(" {A} , {G} ".format_map(dict_1))
