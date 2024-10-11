### Algorithm for Ski Jump Distance and Points Calculation

1. Output the purpose and a brief description of the program to the user.

2. Initialize Constants for Hill Types:
    `NORMAL_HILL_HEIGHT = 46`, 
    `LARGE_HILL_HEIGHT = 70`,
    `NORMAL_POINTS_PER_METER = 2`, 
    `LARGE_POINTS_PER_METER = 1.8`,
    `NORMAL_PAR = 90`, 
    `LARGE_PAR = 120`,
    `GRAVITY = 9.8`

3. Ask the user to enter the hill type (`normal` or `large`).
4. Ask the user to enter the speed of the jumper at the end of the ramp.

5. If the hill type is `normal`:
   1. `height = NORMAL_HILL_HEIGHT`
   1. `points_per_meter = NORMAL_POINTS_PER_METER`
   1. `par = NORMAL_PAR`
6. Otherwise, if the hill type is `large`:
   1. `height = LARGE_HILL_HEIGHT`
   1. `points_per_meter = LARGE_POINTS_PER_METER`
   1. `par = LARGE_PAR`

5. Calculate the Time in the Air: `time_in_air = sqrt((2 * height) / GRAVITY)`
6. Calculate the Distance Traveled: `distance = speed * time_in_air`
7. Calculate the Points Earned: `points = 60 + (distance - par) * points_per_meter`

8. Output the calculated `distance`
9. Output the calculated `points` 

1. If `points` is at least 61:
   1. Output "Great job for doing better than par!"
1. Otherwise if `points` is less than 10:
   1. Output "What happened??"
1. Otherwise:
   1. Output "Sorry you didn’t go very far."

1. Output a message indicating the program has ended.