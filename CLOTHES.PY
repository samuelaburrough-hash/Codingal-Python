print ("Hello! How warm or cold it is today? Please tell me the Celsius of today!")
celcius = (int(input("Enter celsius here please...")))
if celcius > 20:
    outfit = "shirt and shorts"
    print ("Its hot today! I its",celcius,"Celsius!! Put on a T-",outfit)
else:
    outfit = "jacket"
    print ("Its cold today! Put on a",outfit,)
israining = input ("Is it raining today? (Yes/No)")
if israining == "yes":
        print ("Then bring an umbrella!")
windy = input ("Is it windy today? (Yes/no)")
if windy == "yes":
 fast = int(input("How fast is the wind? it has to be a number! Average being 10"))
if fast < 30:
 print ("Then you should be ok! Not too much wind!")
else:
  print ("Then watch out! your coat could fly away in the wind! or maybe even your bag!")
