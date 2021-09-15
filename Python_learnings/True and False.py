'''
Name : Azwad Aziz
Session : 3
Batch : N-212-2
'''
var_1 = 55//3
stack_1 = range(20)
output_1 = var_1 not in stack_1
print(output_1)

print( 43+47<100 and not 23+ 25>50 or not var_1>20 and 44<1 )
#       True     and not  False    or not False    and False
#       True     and   True        or   True       and False
#                         True     or      False
#                                 True
var_2 = 157
var_2 *= 37 
id_var_1 = id(var_1)
id_var_2 = id(var_2)
compare_1 = var_1 is var_2
print(f'''\tID for variable 1= {var_1}
       and ID for variable 2= {var_2}
       so the Identity operator will print {compare_1} ''')
