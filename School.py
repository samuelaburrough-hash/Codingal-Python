print ("Let me plan your day! Awnser these 3 qeustion for me though")
weather = input ("Is the weather rainy sunny or cloudy today? (Please be exact when typing)")
homework = input ("Is your homework done? (Yes/No)")
day = input ("What day is it today? (from monday to sunday ONLY)")
if day in ("Sunday", "Saturday"):
    print ("It's Weekend!!! Enjoy yor free period!")
elif day == ("Monday","Tuseday","Wendsday","Thursday","Friday"):
    print ("Its a normal day of the week, that does mean that you have barely any free time though.")
else: 
    print ("Thats... Not a day?")
if weather == ("Sunny") and homework == ("Yes"):
    print ("Cool! You can go outside and have some fun since you dont have homeworks and the weather is nice")
if weather == ("Rainy") or weather == ("Cloudy"):
    print ("it not nice weather outside, you should stay inside or splash in puddles!")
if not homework == ("Yes"): 
    print ("Maybe you should do your homework first, itll make sure that your less stressed")
if weather == ("raining") and not homework == ("Yes"): 
    print ("Best plan: Stay inside and do your homework, since its raining you could make yourself some hot cocoa")
elif weather == ("Sunny") and homework == ("Yes") and not (day in ("Sunday", "Saturday")) :
    print ("all set and prepared for the great day!")
elif day in ("Saturday","Sunday") and weather == ("Sunny"):
    print ("Perfect weekend weather! hop outside and have fun in this sunny day!")
else: 
    print ("Take the day one step at a time - You got this :D")
print ("Plan complete! Have a nice - welplanned day!")
