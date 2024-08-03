letter="Hello My name is {} and I am from {}"
name="Alok"
country="India"
print(letter.format(name,country))
print(letter.format(country,name))
letter1="Hello My name is {1} and I am from {0}"
print(letter1.format(country,name))

################ f Strings ################
print(f" Hello i am {name} and i am from {country}")
print(f"we are using f string {{name}} and from {{country}}")

################ Doc Strings ################
def square(n):
    '''
    This is a methood where it takes a input as n and gives the square of it
    '''
    print(f"square is : {n*n}")
a=square(5)
print(square.__doc__)

