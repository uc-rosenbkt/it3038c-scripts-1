#This script is meant for a user to input a date and return the leading NBA scorer from that date

# Import requests and BeautifulSoup to scrape and parse web content
import requests, re
from bs4 import BeautifulSoup
# Import time for time.sleep pauses
import time
# Import sys to exit while in loop
import sys

print('NBA leading scorer from any date')

# Defining function that will ask for and return leading scorer
def leadingScorer ():
    # Created while loop to catch errors of bad dates
    while True:
        try:
            # Prompting and returning the desired month variable from the user
            print('Please enter month (1-12):')
            month = input()

            # Prompting and returning the desired day varibale from the user
            print('Please enter day of month:')
            day = input()

            # Prompting and returning the desired year variable from the user
            print('Please enter year:')
            year = input()

            # The site that is being scraped, %s is present to plug in the variable inputs
            data = requests.get("https://www.basketball-reference.com/friv/dailyleaders.fcgi?month=%s&day=%s&year=%s&type=all" % (month, day, year)).content 
            soup = BeautifulSoup(data, 'html.parser')

            # Parsing the HTML to find the player name
            span = soup.find("td", {"data-stat":"player"})
            player = span.text

            # Parsing the HTML to find the amount of points scored
            span = soup.find("td", {"data-stat":"pts"})
            score = span.text

            # Output of the information back to the user
            print('The leading scorer on %s/%s/%s was %s with %s points.' % (month, day, year, player, score))
            break

        # Exception of AttributeError on faulty date
        except AttributeError:
            # Prompting the user to enter a new date with games played
            print('No games played on this date. Please enter a new date.')
            # Delay before asking for the date again
            time.sleep(1)
# End of function
leadingScorer()

# While loop to run the script again
while True:
    time.sleep(1)
    # Prompting the user if they want to enter new date
    print('Would you like to enter another date? (yes/no)')
    answer=input()
    # If answer is yes, the function will run again
    if answer =="yes" or answer =="Yes":
        leadingScorer()
    # If answer is no, the script will stop running
    elif answer =="no" or answer =="No":
        sys.exit()
    # If something other than yes/no, the user is prompted again
    else:
        print('Please answer yes/no')




