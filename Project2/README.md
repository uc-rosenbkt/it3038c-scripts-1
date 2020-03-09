# Project 2

This project is a script that will ask the user to input two numbers and the prime numbers between those two numbers will be returned.

## In python

First, import the time module which will be used at the end of the script.
```
import time
```

Next, the user will be prompted to input two numbers, the lower one first followed by the higher.
```
print("Please enter your lower number: ")
lower = int(input())

print("Please enter your higher number: ")
higher = int(input())
```

Next is a for loop that will calculate the prime numbers in the range.
Using the range feature, you must add 1 to the higher value because it doesn't count it.
Prime numbers must be greater than one so we test if the numbers in the range are divisible by any number 2 through the rest of the range.
```
for num in range(lower, higher + 1):
    #Prime numbers must be greater than 1
    if num > 1:
        #If a number is divisble by anything between 2 and num, it cannot be prime
        for i in range(2, num):
            if(num % i) == 0:
                break
```

The else section of the loop uses time.sleep to have emulate time for cacluation on the output of the prime numbers.
```
        else:
            #Output of the prime numbers in the range
            time.sleep(1)
            print(num)
```
            
            
            
