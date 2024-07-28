#####################  break statement ###################
for i in range(1,11):
    if (i==11):
        break
    print("Multiplication of ",5,"x",i,"is : ",5*i)
print("out of the loop")

#####################  continue statement ###################
for i in range(5):
    if(i==3):
        print("skip the itteration")
        continue
    print(" Multiply is ",2,"x",i,"is : ",2*i)