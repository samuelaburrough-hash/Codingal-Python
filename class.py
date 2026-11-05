print ("these are the marks the students get")
one = int(input())
two = int(input())
three = int(input())
four = int(input())
five = int(input())
tot = one + two + three + four + five
avg = int(tot /5)
validrange = range (1,101)
if avg not in validrange:
    print ("Invalid input! put it in between 1 and 100")
elif avg in range (91,100):
    print ("A+!!!")
elif avg in range (75,90):
    print ("A")
elif avg in range (69,74):
    print ("A-")
elif avg in range (60,68):
    print ("B")
elif avg in range (56,59):
    print ("B-")
elif avg in range (1,40):
    print ("Not Acceptble")
