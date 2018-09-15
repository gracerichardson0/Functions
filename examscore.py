n = 0
total = 0
exam = int(input("Enter exam (-1 to quit)"))
while exam != -1 :
    total += exam
    n +=1
    exam = int (input ("Enter exam (-1 to quit)"))
if n > 0 :
    print ("Average:   ", total/n)
else :
    print ("No exams entered")