def name(fname,lname):
    print("Name is :",fname,lname)
name("Alok","Puhan")

####################### Default Argument ###################################
def average(a=6,b=4):
    print("Average is :",(a+b)/2)
average()
average(a=3)
average(b=6)
average(a=2,b=8)

####################### Keyword Argument ###################################
def name1(fname,mname,lname):
    print("Hello My name is ",fname,mname,lname)
name1("Alok","Ranjan","Puhan")
# name1("Alok","Puhan")
####################### Arbitary Argument ###################################
def avg(*numbers):
    print(type(numbers))
    sum=0
    print(len(numbers))
    for i in numbers:
        sum=sum+i
    print("Average is ",sum/len(numbers))
avg(12,32,12)
####################### Keyword Arbitrary Argument ###################################
def df(**nam):
    print(type(nam))
    print("My name is : ",nam["fn"],nam["mn"],nam["ln"])
df(mn="Prasad",fn="Gajendra",ln="Puhan")

####################### return statement ###################################
def ret(*numb):
    sum=0
    for i in numb:
        sum=sum+i
    return sum/len(numb)
c=int(ret(5,4,3))
print(c)