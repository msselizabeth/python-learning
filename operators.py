#math-operators
print("Math operators(+,-,*,**,/,//,%)")
print("Addition(2 + 2):", 2 + 2)
print("Substraction(2 - 1):", 2 - 1)
print("Multiplication(2 * 2):", 2 * 2)
print("Exponentation(2 ** 3):", 2 ** 3)
print("Division(6 / 2):", 6 / 2)
print("Integer evision(5 // 3):", 5 // 3)
print("Modulo devision(10 % 2):", 10 % 2)

#Bitwise operations
print("#Bitwise operations(<<,>>,&,|,^,~)")
# 2(decimal) --> 10(binary)
# 10(binary) << 2(shift by 2 positions) = 1000(binary)
# 1000(binary) --> 8(decimal)
print("Left shift(2 << 2):", 2 << 2)

# 11(decimal) --> 1011(binary)
# 1011(binary) >> 1(shift by 2 positions) = 101(binary)
# 101(binary) --> 5(decimal)
print("Right shift(11 >> 1):", 11 >> 1)

# 5(decimal) --> 101(binary)
# 3(decimal) --> 11(binary)
# 0b0101 
#   &&&& --> 0b0001
# 0b0011 
# 1(binary) --> 1(decimal)
print("Bitwise AND(5 & 3):", 5 & 3)

# 0b0101 
#   |||| --> 0b0111
# 0b0011 
# 111(binary) --> 7(decimal)
print("Bitwise OR(5 | 3):", 5 | 3)

# 0b0101 
#   ^^^^ --> 0b0110
# 0b0011 
# 110(binary) --> 6(decimal)
print("Bitwise EXCLUSIVE OR(5 ^ 3):", 5 ^ 3)

# ~ 5 -> -(5+1) --> -6
print("Bitwise NOT(~ 5):", ~ 5)

# Comparison
print("#Comparison(<,>,<=,>=,==,!=)")
print("Less(1 < 2):", 1 < 2)
print("Less or equal(2 >= 2):", 2 >= 2)
print("More(1 > 2):", 1 > 2)
print("More or equal(2 >= 2):", 2 >= 2)
print("Equal(1 == 1):", 1 == 1)
print("NOT Equal(1 != 1):", 1 != 1)

#Logical operators(and, or, not)
print("#Logical operators(and, or, not)")
print("Logical AND(False and True):", False and True)
print("Logical OR(False or True):", False or True)
print("Logical NOT(not True):", not True)
