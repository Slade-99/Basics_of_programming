# Operators
#
#  = assignment operator
#  + Add
#  - subtract
#  * multiply
#  / divide 
#  ** exponent
#  % modulus (result will be the same sign as the divisor)
#  // floor division
#
#  INCREMENT AND DECREMENT
# Compound Assigment operators
#  += addition
#  -= subtraction
#  *= multiplication 
#  /= division 
# 
# COMPARISON OPERATORS
#  == equal 
#  ! Not operator 
#  != Not equal
#  >= greater than equal to
#  <= less than equal to
#  
#  LOGICAL OPERATORS
#
#  AND 
#  OR
#  NOT
#
#  MEMBERSHIP OPERATOR
#  in
#  not in
#
#  IDENTITY OPERATOR
#
#  is
#  not is
#
#  Unary - (minus)  used in front of variables to take their negative value
#
#  Unary ~ (invert) used in front of variables to for bitwise inversion
#  In python it evaluates to -( x + 1)
x = - 30
print(~x)


#
# Bitwise operators
#
# & Bitwise AND  (Returns 1 if both the bits are 1 else 0)
a = 10
b = 4 
print(a&b)
#              a = 10 = 1010 (Binary)
#              b = 4 =  0100 (Binary
#
#            a & b = 1010
#                      &
#                    0100
#                    = 0000 #     = 0 (Decimal)
#
# | Bitwise OR (Returns 1 if either of the bit is 1 else 0)
print(a | b)
#              a = 10 = 1010 (Binary)
#               b = 4 =  0100 (Binary
#
#                 a | b = 1010
#                           |
#                         0100
#                        = 1110
#                        = 14 (Decimal)
#
# ^ Bitwise XOR (Returns 1 if one of the bit is 1 and other is 0 else returns false)
x = 7
y = 5
print(x^y)
#
#  
#  7 = 111
#       ^ 
#  5 = 101
#
#    = 010  = 2
#
# ~ Bitwise compliment -(x+1)
print(~x)
#
# << Bitwise left shift (multiply by the power of 2)
print(x<<3)
#             7*(2**3)
#
#
# >> Bitwise right shift (divide by the power of 2)
z= 40
print(z>>3)
#
#    40(2**-3)
#
#
#











#print(42!=42)
#print(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2)



