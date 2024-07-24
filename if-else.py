########################### if - else statement##################
applePrice=210
budget=200
if (applePrice<budget):
    print("apple is added to your cart")
else:
    print("Sorry, Your budget is low")

########################### elif statement##################
input=int(input("Enter a Number : "))
if(input>0):
    print("Number is Positive")
elif (input==0):
    print("NUmber is zero")
elif (input == 999):
    print("Number is special number")
else:
    print("Number is negative number")

########################### nested if statement##################
numbers=int(input("Enter a number "))
if(numbers<0):
    print("It is a negative number")
elif(numbers>0):
    if(numbers<=10):
        print("Numbeer is between 1 - 10")
    elif (numbers > 10 and numbers <= 20):
        print("Number is between 11=20")
    else:
        print("Number is greater than 20")
else:
    print("It is a negative number")