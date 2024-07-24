# All concepts about string
name = "Alok"
print("your name is "+name)
print('Hello this is m friend "jackson"')

# Multiline String
str=''' Hello my name is alok this is gonna be my first program towards python
this program is about the string concepts
in python program
'''
print(str)

# Accessing characters of a string
name1="Sudarshan"
print(name1[0])
print(name1[4])
print(name1[3])

# looping through string
for character in name1:
    print(character)

# string slicing
# lngth of a string
animal="Elephant"
len=len(animal)
print(animal," is a ",len," letter word.")
# string as an array
print(len)
print(animal[0:4])
print(animal[2:4])
print(animal[3:5])
print(animal[-5:4])  #(length of animal)-5: (length of animal -4)
##############################string methods####################################
mtd ="  !!NewDelhi Bemgaluru Odisha!!  "
print(mtd)
print(mtd.upper())
print(mtd.lower())
print(mtd.strip())
mtd2 ="  !!NewDelhi Bemgaluru Odisha!!"
print(mtd2.rstrip("!"))
print(mtd.replace("NewDelhi","Rajastan"))
print(mtd.split(" "))
mtd3 ="!!NewDelhi Bemgaluru Odisha!!"
print(mtd3.split(" "))
mtd4="Hii there"
print(mtd4.capitalize())
mtd5="hii There"
print(mtd5.capitalize())
str1='Welcome to the console'
print(str1.center(40))
print(str1.center(40,"-"))
str2="alok jitu manisha alok!"
print(str2.count("alok"))
print(str2.endswith("!"))
print(str2.endswith("jit",2,8))
print(str2.find("mani"))
print(str2.find("Mani"))
print(str2.index("mani"))
str3="aloknewdelhI2"
print(str3.isalnum())
str4='newDelhi'
print(str4.isalpha())
str5="hii"
print(str5.isprintable())
str6=" "
print(str6.isspace())
str7="Hello World"
str8="Verry well"
print(str7.istitle(),str8.istitle())
str9="HEALTH IS VERY GOOD"
print(str9.isupper())
print(str9.replace("GOOD","BAD"))
print(str9.startswith("HEALTH"))
print(str9.swapcase())
print(mtd5,"\n",mtd5.swapcase())