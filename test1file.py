""" Structured English
This program will create two functions. Each function evaluates a different salary option.
They will calculate the pay for each day. The first function adds $100 per day.
The second function adds $1 the first day, $2 the second day, $4 the third day, and so on, 
with the amount doubling each day. The functions will determine the final pay for each option.
Finally, the final pays of each option will be compared, and the program will display the 
salary option that pays the most, or it will say that they pay the same.
"""

""" Pseudo-code
Option 1: 
  pay = 0 
  day = 0
  pay += 100
  loop 10 times
  return amount

Option 2:
  pay = 1
  day = 0
  total_pay = 0
  pay *= 2
  total_pay += pay
  Loop 10 times
  return amount

Main:
  var1 = option1
  var2 = option2
  if the amounts are the same, output to the user, "Option 1 and Option 2 pay the same"
  if option 1 is better, output to the user, "Option 1 is better."
  if option 2 is better, output to the user, "Option 2 is better."
"""