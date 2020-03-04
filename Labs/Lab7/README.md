# Lab 7

This is how to run Python scripts to return various NBA stats from basketballreference.com using a package called basketball-reference-scraper.
##To install the package in Powershell run the following
```
pip install basketball-reference-scraper
```
### Now we are ready to script with Python

The first piece of information we are going to gather is an NBA roster. You need to import get_roster from basketball_reference_scraper.teams and then specify which team and year you want to see. Below I print out the 2016 Cleveland Cavaliers Roster.
```
from basketball_reference_scraper.teams import get_roster
roster = get_roster('CLE', 2016)
print("\nCleveland Cavaliers 2016 Roster:")
print(roster)
```

The next retrieval will be individual players stats, you must import get_stats from the scraper with the extension of .players for this one. The example is the year-by-year stats for Collin Sexton as of the current date.
```
from basketball_reference_scraper.players import get_stats
stats = get_stats('Collin Sexton', stat_type='PER_GAME')
print("\nCollin Sexton Stats:")
print(stats)
```

The final piece of information we will get are the standings. To do this, import get_standings from the scraper with .seasons included. Standings can be returned from any date, however the default is the current date, which is what I do below.
```
from basketball_reference_scraper.seasons import get_standings
standings = get_standings()
print("\nCurrent NBA Standings:")
print(standings)
```

I have added in '\n' in the print statements to be able to easier read the output.
