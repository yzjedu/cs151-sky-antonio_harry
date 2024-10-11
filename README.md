[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/U4vAwEgA)
# Lab3: Ski Jump
* GRADE: EMRN									
* Due: next Lab class
	
## Problem: 
* Winter is coming! One winter sport is the ski jump, where the score is determined by the distance traveled after skiing down a ramp and into the air.
* What type of speed does a ski jumper need to achieve on the ramp to make a good distance on their jump?
* Let’s make a program to calculate the distance traveled based on speed and determine how many points they’d receive if they went that distance.
* [See an image of ski jump](https://i0.wp.com/i.ytimg.com/vi/nIH01DgMOnI/maxresdefault.jpg), or [watch an intro video](https://www.nbcolympics.com/videos/winter-olympics-101-basics-ski-jumping).

## Purpose: 
This lab gives you practice with:
* Using the math module  
* Using decision making in your code  
* Follow usability rules for your input and output  
* Drawing a flowchart & finding control paths  

## Details:
Given the type of ski jump (normal vs. large) and the jumper’s speed at the end of the ramp, predict how far they will jump using the simplification in the table below. Then output their number of points earned.

|Hill Type	| Height	| Points per meter	| Par (distance)|
|-----------|-----------|-------------------|---------------|
| Normal	| 46	    | 2	                | 90            |
| Large	    | 70	    | 1.8	            | 120           |

 - To simplify the calculation, the time in the air is calculated as `sqrt((2*height)/9.8)`. 
 - The distance traveled is the `jumper’s speed * time in the air`.

* After determining their distance, calculate how many points they would get on the chosen hill. 
  * Their points depend on whether or not their distance is above par (good) or below or equal to par (bad). 
  * Calculate the points earned as `60 + (distance - par)*points_per_meter`.

* Tell the jumper `Great job for doing better than par!` when their points are at least 61, 
* `What happened??` if their points are less than 10, or 
* `Sorry you didn’t go very far` otherwise. 
* Don’t forget to output their distance and points so they know how well they did! 

## Steps:
1. Understand the problem you are trying to solve. 
   1. Do you understand the input, desired output, and when a decision needs to be made?
2. Write your algorithm in `algorithm.docx` to solve this entire problem. 
   1. Remember to write decisions correctly – refer to your notes as necessary. 
   2. This is likely the hardest step of the lab -- be careful about the order of steps so that you aren't doing the same thing more times than necessary. 
   3. The lab instructor must approve your algorithm before you code.
   4. Your `if` statements should *set* the `variables`, but not do the calculations/computations. 
      1. Have the calculations in a different section - so that when debugging, you can easily find where the problem is.
3. Write your code in main.py. Recall that you can compare strings like "normal" and "large" for equality in the same way you can compare numerical types.
4. Make sure you follow the guidelines for well-formatted and readable code with comments.
5. Make sure you add the intro comments.
6. Draw a flowchart of your code on paper/draw.io/whimsical.
7. Create test cases based on the paths through the code (use code or flowchart to find them) in `test_cases.xlsx`. 
   1. You should have test case for each situation that could occur.
   2. Use the test cases to make sure your program works correctly, and fix it if it doesn’t. 
   3. Don’t just assume you did it right, there are many things that could have gone wrong. 
   4. Test EVERY control path. 
   5. You may find it helpful to test with additional inputs as well if you didn’t pick various special cases for your input values.

## Reminder of Intro Comments Style

  ```
  # Programmers:  
  # Course:  
  # Due Date: 
  # Lab Assignment: 
  # Problem Statement:  
  # Data In:
  # Data Out:  
  # Credits: 
  ```

## What to Submit in GitHub:

1. Completed `main.py` file  
2. `algorithm.docx`
3. An Excel file with your test cases.  
    - Edit the `test_cases.xlsx` file with Excel software 
    - If it can open then ok. Otherwise
      - Right click on `test_cases.xlsx` -> Open In -> Associated Application
4. `RD1.docx` -> Reflection for Drive 1
5. `RD2.docx` -> Reflection for Drive 2

**As a reminder, reflections count toward your participation grade.**

Type the Reflection INSIDE the respective Word file and addressing the following questions:

 - Objective:
   - What were you supposed to learn/accomplish?

 - Procedure:
   - What steps were followed and what techniques did you use to solve the problem?
   - What were the Key concepts explored?

 - Results:
   - Did your results match what you expected to get? 
   - Did you try using various test cases, or extreme test cases?
  
 - Reflection:
   - What challenges did you encounter? 
   - How did you follow the first 3 rules of programming?
   - Did you overcome them, and how? 
   - Any key takeaways? 
   - Do you think you learned what you were supposed to learn for this lab? 
   - What was it like working with your partner?

