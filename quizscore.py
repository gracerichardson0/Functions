num = int (input ("# quizzes"))
total = 0
for count in range (1, num+1):
    quiz = int (input ("Quiz  "))
    if (quiz < 0 or quiz > 100) :
        print ("INVALID")
    else :
        total += quiz
print ("Average: ", total/num)