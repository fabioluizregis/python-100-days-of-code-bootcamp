# Day 2 - Understanding data types and how to manipulate strings

# Subscripting
print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])

# String
print("")
print("123" + "456")

# Integer = Whole number
print("")
print(123 + 456)

# Large Integers
print("")
print(123_456_789)

# Float = Floating point numbers
print(3.14159)

# Boolean
print("")
print(True)
print(False)

# Showing the type of a data
print()
print(type("Text"))
print(type(1234))
print(type(True))
print(type(3.14))

# Type conversion ( works with int() , float(), str(), bool() )
print()
print(int("100")+int("100"))

print()
print("Number of letters in your name: " + str(len(input("Enter your name: "))))

# Mathematical Operations
print()
print(123 + 456)
print(7 - 5)
print(3 * 2)
print(5 / 3)
print(5 // 3) # Eliminates the values after .
print(2 ** 3) # Potenciation

# Rounding numbers
print()
bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi, 2))

# f-Strings
print()
age = 50
print(f"The wine has {age} years!")
