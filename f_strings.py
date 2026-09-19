age = 21
print(f"{age=}")
# age=21

for i in range(3):
    print(f'{i=}', end=' ')

x = 10
y = 5
print(f"{x=}, {y=}, {x+y=}")
# x=10, y=5, x+y=15


price = 19.956
print(f"{price = :.2f}")
# price=19.96

exit()
name = "Gustav"
print(f"{name!r}")
# meant for debugging 
# 'Gustav'
# ? 

name = "Björelius"
print(f"{name!a}")
# 'Bj\xf6relius'

name = "Gustav"
print(f"{name!s}")
# ? 

print(f"|{'Python':<10}|")
# |Python    |
# so it gives a space of 10 characters to be inside AND Aligns it to the left in that space

print(f"|{'Python':>10}|")
# |Python    |
# so it gives a space of 10 characters to be inside AND Aligns it to the left in that space

print(f"|{'Python':*^10}|")
# Embeds and centers 'Python' inside a space of 10 asterixs 

print(f"|{30:=10}|")
# ? 

print(f"{42:+}")
# +42

print(f"{-42:-}")
# -42 '*' does not work 

print(f"|{42: }|")
#  42 (this prepends a space)

print(f"{3.14159265:.2f}")
# (sets precision with digits)

print(f"{3.14159265:.4f}")

print(f"{1234567890:,}")
# 1,234,567,890

print(f"{1234567890:,}")
# 1,234,567,890

print(f"{1234567890:_}")
# 1_234_567_890

print(f"{1234567890:n}")
# apparently this is 'locale-aware' and i have no idea what that means 

print(f"{'Programming':.7}")
# Program 
# sets the amount of 

# modifiers can be dynamic 
value = 3.14159265
width = 10
precision = 3
print(f"|{value:{width}.{precision}f}|")
#      3.142
# Nested replacement fields are supported inside the format specification. They cannot be nested indefinitely.

number = 1234567.891
print(f"{number:*>+20,.2f}")
# ******+1,234,567.89

print(f"{1234567890:e}")
# 1.234567e+06

print(f"{1234567890:.2e}")
# 1.23e+06