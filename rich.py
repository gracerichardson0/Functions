amt = float (input ("Enter amount of bill: "))
sat = int(input ("1: Very satisfied\n2: Satisfied\n3. Dissatisfied"))
if sat == 1 :
    tipPerc = .2
    info = "Very Satisfied"
elif sat == 2 :
    tipPerc = .15
    info = "Satisfied"
elif sat == 3 :
    tipPerc = .1
    info = "Dissatisfied"
else :
    tipPerc = 0
    info = "Invalid"

print ("Bill: $", amt, "\n",info, "\nTip: $",tipPerc*amt)