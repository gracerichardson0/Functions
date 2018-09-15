day = int (input ("Enter day 1 - 7"))
if day == 1:
    name = "Sunday"
elif day == 2 :
    name = "Monday"
elif day == 3 :
    name = "Tuesday"
elif day == 4 :
    name = "Wednesday"
elif day == 5 :
    name = "Thursday"
elif day == 6 :
    name = "Friday"
elif day == 7 :
    name = "Saturday"
else :
    name = "INVALID"
if day >= 2 and day <= 6 :
    name += " Time for Work"
elif day == 1 or day == 7
    name += " Enjoy the weekend!"

print (name)