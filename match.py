x= int(input("Enter a number :"))
match x:
    case 0:
        print("x is zero")
    case 4 if(x%2==0):
        print("x%2==0 case is in ")
    case _ if(x>10):
        print("x>10")
    case _ :
        print(x)