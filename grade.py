def enter() :
    grade = int(input("Enter grade"))
    while grade < 0 or grade > 100:
        grade = int(input ("Error. Enter grade:"))
    return grade

if enter() >= 90 :
    print ("Congrats on the A")
