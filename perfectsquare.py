import math

n = int(input("Enter value, at least 10"))
while (n <= 10):
    n = int(input("Error!! Enter a value that is at least 10"))

for value in range (1, n+1) :
    if math.sqrt(value) == int (math.sqrt(value)) :
        print (value)
