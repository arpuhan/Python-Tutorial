letter="Hello My name is {} and I am from {}"
name="Alok"
country="India"
print(letter.format(name,country))
print(letter.format(country,name))
letter1="Hello My name is {1} and I am from {0}"
print(letter1.format(country,name))