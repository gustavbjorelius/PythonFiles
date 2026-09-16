
"""
Skriv ut True om alla tecken i strängen är siffror, annars False.
Tips! Leta efter en metod som kontrollerar om samtliga tecken är siffertecken.
"""

sentence = "Python is my favorite programming language!"
print(sentence)
print(sentence.upper())
print(sentence.count("o"))
print(sentence.replace("my", "everyone\'s"))

if sentence.isalpha():
    print(True) 
else: 
    print(False)

if sentence.isascii():
    print(True)
else:
    print(False)

if sentence.isdigit():
    print(True)
else:
    print(False)