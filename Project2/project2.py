#This script is meant for the user to input two numbers and they will be returned the prime numbers between them.


#Import the time module for the pause in calculation
import time

#Prompting the user to enter their lower int value
print("Please enter your lower number: ")
lower = int(input())

#Prompting the user to enter their higher int value
print("Please enter your higher number: ")
higher = int(input())

#Output message before the prime numbers are listed
print("Prime numbers bewteen %s and %s are: " % (lower, higher))

#For loop to determine prime numbers in the range input
for num in range(lower, higher + 1):
    #Prime numbers must be greater than 1
    if num > 1:
        #If a number is divisble by anything between 2 and num, it cannot be prime
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            #Output of the prime numbers in the range
            time.sleep(1)
            print(num)

