richest = "none"
maxBal = 0
for count in range(1,3):
    name = input ("Name: ")
    balance = float (input ("Enter balance: "))
    if balance > maxBal :
        richest = name
        maxBal = balance
    print("Richest guy: {0:s} has balance of ${1: ,.2f}" . format(richest, maxBal))
