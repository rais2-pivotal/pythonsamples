#!/usr/bin/env python

answer = 0
numarray = []


while True:
   answer = input("Enter a number: ")
   if answer == 'done':
      break

   try:
      val = int(answer)   
      numarray.append(val)
   except ValueError:
        print("Invalid input")
        continue

print("Min from array is: " + str(min(numarray)) + " and Max from array is: " + str(max(numarray)))
