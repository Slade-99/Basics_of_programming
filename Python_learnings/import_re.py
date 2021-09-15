import re
#message = "awdsfokanmsdokfm  asdfn[asdkfn 01923453390 asdljfnasdojfnaosjdfn 01920709268"

#style = re.compile(r'01\d\d\d\d\d\d\d\d\d')

# x = style.search(message)
# print(x.group())
# x = style.findall(message)

# print(x)


################# To grab a specific part of something we use groups
############### If we are looking for parenthesis then use the escape character \ 
# style = re.compile(r'(01\d)(\d\d\d\d\d\d\d\d)')

# print( style.search(message).group(1))




####### Using pipe | character to find for a specific prefix and some expected suffix
# message = "Batmobile used his batman to chase a villain and used the batclaw and bat rang to catch him"

# style = re.compile(r'Bat(man|mobile|claw|rang)')

# print(style.search(message).group())



##### If something appears once or none

# message = " Adventures of batwoman"
# message_1 = "Adventures of batman"
# style = re.compile(r'bat(wo)?man')
# print(style.search(message).group())
# print(style.search(message_1).group())

###### Using the ()? makes the group optional

################# * is the zero character it means zero or more times
# message = " Adventures of batwowowowoman"
# style = re.compile(r'bat(wo)*man')
# print(style.search(message).group())

################## is we use + then the group must appear one or more times



############## For a specific number of appearance we use {} or also in range {2,5} {3,}
# message = " Adventures of batwowowoman"
# style = re.compile(r'bat(wo){2,5}man')
# print(style.search(message).group())


# message = "My three phone numbers are 01923453390,01303477432,01920709268"
# style  = re.compile(r'(01\d\d\d\d\d\d\d\d\d(,)?){3}')
#print(style.search(message).group())


##########Greedy and non Greedy match this use of ? is different

# style = re.compile(r'(\d){3,5}')
# print(style.search("there is 123456789").group())
# style_1 = re.compile(r'(\d){3,5}?')
# print(style_1.search("there is 123456789").group())




########### When using findall ... If there are no groups so it will return a list of matched strings
########### but if there is are groups... It will return tuples of strings of lists

# message = "My three phone numbers are 01923453390,01303477432,01920709268"
# style  = re.compile(r'((01\d)(\d\d\d\d\d\d\d\d))')
# print(style.findall(message))

# Character classes ... \d for 0-9     \D everything other than 0-9     \w any letter,number,underscore  \W NOT any letter,number,underscore
# \s Any space , tab , newline     \S Not any space ,tab, newline



### Using []

# style = re.compile(r'[aeiouAEIOU]{2}')   ### Same as pipe a|b|c|   {2} impplies to two consequtive vowels

# print(style.findall("Aa brown fox jumped over a lazy dog."))


# the ^ acts like the NOT option

# style = re.compile(r'[^aeiou .]')

# print(style.findall("Aa brown fox jumped over a lazy dog."))  ## using the ^ gives all the consonant

# Not using []  dot star  ^ acts like beginswith and caret dollar $  acts like endswith  if both * and $ used then string has to be exactly same
# style = re.compile(r'^\d+$')
# print(style.search("12312").group())



##### Wildcard dot . means any character but not newline

style = re.compile(r'.at')

print(style.findall("bat mat cat rat brat hat sat tip top"))  ## not showing brat


# style = re.compile(r'.{1,2}at')

# print(style.findall("bat mat cat rat brat hat sat tip top"))

# message = "First Name: Azwad Last Name: Aziz"
# style = re.compile(r'First Name: (.*) Last Name: (.*)')

# print(style.findall(message))

 
# message = " < First to enter the line> will only be accepted>" 
# style = re.compile(r'<(.*?)>')  ### ? means non greedy
# print(style.findall(message)) 

# message = " < First to enter the line> will only be accepted>" 
# style = re.compile(r'<(.*)>') 
# print(style.findall(message))

# message  =  "sadfsdfsdf\nasdfsdfsdf \nasdfsdfsdfsd"
# style = re.compile(r'.*' , re.DOTALL)
# print(style.search(message).group())

# re.I is used to ingnore case changes




#### For find and substitute

# message = "Clash Royale is developed for the tournament of Clash Con."
# style = re.compile(r'Clash \w+')

# print(style.sub("Nice" , message))


##### To partially substitute
# message = "Clash Royale is developed for the tournament of Clash Con."
# style = re.compile(r'Clash (\w)(\w)\w+')
# # print(style.findall(message))
# print(style.sub(r'Clash \1\2*****', message))





### Verbose method allows us to sue new space and new line to make the code more readable

# message = "awdsfokanmsdokfm  asdfn[asdkfn 01923453390 asdljfnasdojfnaosjdfn 01920709268"

# style = re.compile(r'''(01\d)
#                     (\d\d\d\d\d\d\d\d)''' 



#                               , re.VERBOSE)

# print(style.findall(message))

####### if we have to use multiple arguments with the compile function then
####### re.compile(r'sdfsdfsdf' , re.I | re.DOTALL | re.VERBOSE)