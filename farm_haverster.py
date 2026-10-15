field1 = 20
field2 = 11
field3 = 32
field4 = 51
field5 = 5
#smallgap
total = field1 + field2 + field3 + field4 + field5
average = total /5
print ("The total harvest is",total,"apples")
print ("But the average is",average,"apples!")
print ("in field 1 lies 20 apples, in field 2 11!In field 3 were 32 whole apples, in field 4 were the most, rounding up to a whopping 51 apples! field five had 5.")
price_per_apple = 2.50
earnings = price_per_apple * total 
print ("One apple is 2.50$, you sold",total,"apples, you earned",earnings,"$")
bags = total // 25
leftover= total %25
print ("You made",bags,"bags")
print ("You have",leftover,"leftover apples")
lastyear = 500
print ("Better than last year? :",total>lastyear)
print ("Worse than last year?  :",total<lastyear)
total += 30
print ("After a bonus check we got 30 extra apples! you total is now",total,"apples")
total -= 15
print ("You actually only have",total,"apples after we took 15 for seeds so that we could make more next year!")
bags = total // 25
print ("Now finally you can check the amount of bags, in today, you made",bags,"bags!!!!WHOOO!")