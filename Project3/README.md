# Project 3
This project asks for the user to input a date and then scrapes basketball-reference.com to find the leading scorer on that day.

### Frist, requests and BeautifulSoup need to be imported to scrape the web and display the information. Time and sys is also imported for a time deal and exit.
```
import requests, re
from bs4 import BeautifulSoup
import time
import sys
```
### Inside the leadingScorer function, the user is prompted for the date they want to see. A while loop is created to ask for new dates if there were no games on an entered date.
```
def leadingScorer ():
    while True:
        try:
            print('Please enter month (1-12):')
            month = input()

            print('Please enter day of month:')
            day = input()

            print('Please enter year:')
            year = input()
```

### Next, the site is scraped and the information we want is parsed from HTML
```
            data = requests.get("https://www.basketball-reference.com/friv/dailyleaders.fcgi?month=%s&day=%s&year=%s&type=all" % (month, day, year)).content 
            soup = BeautifulSoup(data, 'html.parser')

            span = soup.find("td", {"data-stat":"player"})
            player = span.text

            span = soup.find("td", {"data-stat":"pts"})
            score = span.text
 ```
 
 ### The leading scorer on that date is sent back to the user
 ```
 print('The leading scorer on %s/%s/%s was %s with %s points.' % (month, day, year, player, score))
            break
 ```
 
 ### If the date had no games played, the user is prompted to neter a new date and restart the function
 ```
 except AttributeError:
            print('No games played on this date. Please enter a new date.')
            time.sleep(1)
leadingScorer()
```

### Finally, a second while loop is created to ask the user if they want to enter a new date and continue running the script
```
while True:
    time.sleep(1)
    print('Would you like to enter another date? (yes/no)')
    answer=input()
    if answer =="yes" or answer =="Yes":
        leadingScorer()
    elif answer =="no" or answer =="No":
        sys.exit()
    else:
        print('Please answer yes/no')
```
## Sample output of the script is as follows:
```
NBA leading scorer from any date
Please enter month (1-12):
10
Please enter day of month:
31
Please enter year:
2019
The leading scorer on 10/31/2019 was Kawhi Leonard with 38 points.
Would you like to enter another date?

```
