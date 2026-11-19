print ("Please enter a numirator!")
numirator = int(input())
print ("Okay you have numirator" ,numirator,"!")
print ("Please enter a denomnator")
denomenator = int(input())
if numirator%denomenator == 0:
    print ("/n" +str(numirator) + "is divisible by" +str(denomenator))
else:
    print ("They are not divisible by eachother, so they cannot be used!")