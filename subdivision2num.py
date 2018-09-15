num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
choice = int(input("Enter choice\n 1: Subtract\n 2: Divide"))
if choice ==1 :
    print (num1-num2)
else:
    if num2==0 :
        print ("Error")
    else :
        print (num1/num2)