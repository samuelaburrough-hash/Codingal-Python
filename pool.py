
# Part 1: Sort the swimmer into an age group
age = int(input("How old are you? "))

if age < 12:
    age_group = "Child"
elif age < 18:
    age_group = "Teenager"
else:
    age_group = "Adult"

print("Your age group is:", age_group)


# Part 2: Check that the two answers are yes or no
deep_pool_answer = input("Can you swim? (yes/no): ").lower()
adult_answer = input("Is an adult with you? (yes/no): ").lower()

if (deep_pool_answer != "yes" and deep_pool_answer != "no") or (adult_answer != "yes" and adult_answer != "no"):
    print("Invalid answer! Please enter yes or no.")
    exit()


# Part 3: Allow the deep pool only when two things are both true
if deep_pool_answer == "yes" and age >= 12:
    deep_pool = True
else:
    deep_pool = False


# Part 4: Warn about the shallow end when either condition is true
if age < 12 or deep_pool_answer == "no":
    print("Warning: You should use the shallow end.")


# Part 5: Remind about the lifeguard when no adult is present
if not (adult_answer == "yes"):
    print("Reminder: Make sure a lifeguard is present!")


# Part 6: Give one final verdict
if deep_pool and adult_answer == "yes":
    print("FINAL VERDICT: You are allowed in the deep pool!")
else:
    print("FINAL VERDICT: You must stay in the shallow pool.")
