# Programmers: Harry Li, Antonio 
# Course:  CS151 sec 06
# Due Date: 10/2/2024
# Lab Assignment: Ski jump
# Problem Statement:  Let’s make a program to calculate the distance traveled based on speed and determine how many points they’d receive if they went that distance.

import math 

#Output the purpose of the code/ program
print('Winter is coming! Ski season is here! This program would calculate the ski distance traveled based on the speed and ramp size and would calculate how many points you would get for the travelled distance.')

#Prompt the user to input the hill type, large or normal
hill_type = str(input('Please enter the hill type large or normal:' ))
if hill_type.lower() == 'normal':
    hill_height = 46
    points_per_meter = 2
    par = 90
elif hill_type.lower() == 'large':
    hill_height = 70
    points_per_meter = 1.8
    par = 120
else:
    while hill_type != 'large' and hill_type != 'normal':
        hill_type = str(input('Please enter the correct hill type large or normal:' ))

#Using the hill type calculate the air time using the formula
air_time = math.sqrt((2*hill_height)/9.8) 

#Prompt user to input a speed in meters every second above 0 and store it in a variable named 'meters_per_sec'
meters_per_sec = float(input('Enter speed in meters traveled per second:'))
while meters_per_sec <= 0:
    meters_per_sec = float(input('Please enter speed in meters per second above 0:'))

#Calculate distance traveled by multiplying meter_per_sec and air_time
distance_traveled = float(meters_per_sec*air_time)

#Calculate the total amount of points using the formula and store it in a variable named 'total_points'
total_points = float(60 + (distance_traveled - par) * points_per_meter)

#Output the distance the user has traveled 
print(f'You have traveled {distance_traveled:.2f} meters.')

#Output certain response based on the points earned
if total_points > 60:
    print(f'Great job you have earned {total_points:.0f} points. that is more than par')
elif total_points <= 0:
    total_points = 0
    print(f'Oh no! You didnt earn any points. what happened?')
elif total_points < 10:
    print(f'Oh no! you have earned {total_points:.0f} points. what happned?')
else:
    print(f'Unfortunately you have earned {total_points:.0f} points. You did not make it that far.')
