#Script to get NBA roster from a certain year
from basketball_reference_scraper.teams import get_roster
roster = get_roster('CLE', 2016)
print("\nCleveland Cavaliers 2016 Roster:")
print(roster)


#Script to retrieve an indiviual player's stats by year
from basketball_reference_scraper.players import get_stats
stats = get_stats('Collin Sexton', stat_type='PER_GAME')
print("\nCollin Sexton Stats:")
print(stats)


#Script to get NBA standing on a certain date
from basketball_reference_scraper.seasons import get_standings
standings = get_standings()
print("\nCurrent NBA Standings:")
print(standings)