#!/usr/bin/env python

answer = 0
numsum = 0

while True:
   answer = input("Enter a number: ")
   if answer == 'done':
      break

   try:
      val = int(answer)   
      numsum += val     
   except ValueError:
        print("Invalid input")
        continue

 
print("Total sum of inputs: " + str(numsum))     
 
