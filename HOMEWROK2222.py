# Step 1: Store Team Points
team1 = 85
team2 = 92
team3 = 78
team4 = 88
team5 = 97

total_points = team1 + team2 + team3 + team4 + team5
average_points = total_points / 5

print("Total team points:", total_points)
print("Average points per team:", average_points)

stars_per_point = 2
total_stars = total_points * stars_per_point

print("Total reward stars:", total_stars)

box_size = 25
full_boxes = total_stars // box_size
leftover_stars = total_stars % box_size

print("Full boxes of stars:", full_boxes)
print("Leftover stars:", leftover_stars)

last_week = 400

print("This week has more points:", total_points > last_week)
print("This week has the same points:", total_points == last_week)
print("This week has at least last week's points:", total_points >= last_week)

total_points += 20  # Bonus points

print("After bonus points:", total_points)

total_points -= 10

print("After missed-task points:", total_points)

print("\n--- Final Results ---")