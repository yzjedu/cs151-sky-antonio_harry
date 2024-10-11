# Programmers: [Your Name]
# Course: CS151
# Due Date: [Due Date]
# Lab Assignment: Lab 03 
# Problem Statement: Calculate the ski jump distance and points based on hill type and speed.
# Data In: Hill type (normal or large), Jumper's speed
# Data Out: Distance jumped, Points earned, Feedback

import math

# Display program purpose
print("This program calculates the distance traveled and points earned for a ski jumper.")

# Constants
GRAVITY = 9.8
NORMAL_HILL_HEIGHT = 46
LARGE_HILL_HEIGHT = 70
NORMAL_POINTS_PER_METER = 2
LARGE_POINTS_PER_METER = 1.8
NORMAL_PAR = 90
LARGE_PAR = 120

# Input: Hill Type and Speed
hill_type = input("Enter the hill type (normal or large): ").strip().lower()
speed = float(input("Enter the speed of the jumper at the end of the ramp (m/s): "))

# Determine parameters based on hill type
if hill_type == "normal":
    height = NORMAL_HILL_HEIGHT
    points_per_meter = NORMAL_POINTS_PER_METER
    par = NORMAL_PAR
elif hill_type == "large":
    height = LARGE_HILL_HEIGHT
    points_per_meter = LARGE_POINTS_PER_METER
    par = LARGE_PAR
else:
    print("Invalid hill type entered. Please enter either 'normal' or 'large'.")


# Calculate time in air
time_in_air = math.sqrt((2 * height) / GRAVITY)

# Calculate distance traveled
distance = speed * time_in_air

# Calculate points earned
points = 60 + (distance - par) * points_per_meter

# Output: Distance and Points
print(f"Distance traveled: {distance:.2f} meters")
print(f"Points earned: {points:.2f}")

# Determine feedback based on points
if points >= 61:
    print("Great job for doing better than par!")
elif points < 10:
    print("What happened??")
else:
    print("Sorry you didn’t go very far.")