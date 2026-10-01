import keyword

# Ask for information
name = input("Enter your name: ")
skill = input("Enter a skill: ")
target_month = input("Enter your target month: ")


daily_minutes = 30

print("\nMy Learning Plan\n")


print("Name:", name)
print("Skill:", skill)
print("Target Month:", target_month)
print("Daily Minutes:", daily_minutes)

# Print two lines on the same line
print("I will practise ", end="")
print(skill)

# Print Python's reserved keywords
print("\nPython's reserved keywords:")
print(keyword.kwlist)


