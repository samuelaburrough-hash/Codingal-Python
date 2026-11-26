print ("==WELCOME TO THE RIDE BUILDER==")
print ("xX PLease choose honestly! Xx")
print ("           !ENJOY!")
print ("Please choose if you want a car or bike")
choice = input ("INPUT YOUR CHOICE HERE ----->    ")
if choice == "bike" :

    print ("Okay! What type of bike though???")
    print ("1 for Scooty, 2 for mountain bike!!!")
    type = int(input("PUT NUMBER HERE! ---->       "))
    if type == 1:
        print ("YOU CHOSE SCOOTY BIKE")
        print ("Definitely the faster choice!")
        print ("Its good for city roads!")
        print ("Not for big open moantains and paths")
    else:
        print ("You chose the Mountain Bike!")
        print ("Slower but easier and funner to use!")
        print ("Great for open paths! and of course... Mounatains!")
        print ("Not bad for city roads, but a scooter is better for them")
elif choice == "car":
    print ("You chose Car! What brand car?")
    print ("1 for a lambo 2 for a volvo!")
    type2 = int(input("INPUT 1/2 HERE ------->    "))
    if type2 == 2:
        print ("You chose volvo!")
        print ("Great for transporting stuff!")
        print ("Very easy to use!")
        print ("Doesnt go too fast but has some good speed!")
    else:
        print ("You chose the lamborgini!")
        print ("MEGA STYLISH!")
        print ("Very fast!")
        print ("HARD TO CARRY STUFF ): ")
else:
    print ("THATS NOT WHAT I ASKED OR YOU TYPED IT WRONG!!! remember, only type car or bike")
print ("+THIS WAS THE AMAZING... RIDE BUILDER! I HOPE YOU ENJOYED AND BYE. ")
