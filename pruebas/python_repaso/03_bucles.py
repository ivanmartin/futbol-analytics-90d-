#Ejercicio inspirado en apartado Random numbers de Khan Academy
import random

points = 0
games_played = 0
victory = 0
defeat = 0
tie = 0

# The team has a 20% chance of a win, a 30%
# chance of a loss, and a 50% chance of a tie.

#Versión con While ---> """ para comentar todo el bucle
"""while games_played <= 38:

    result = random.randint(1, 10)
    
    if result == 1 or result == 2:
        match_end = "WIN"
        points += 3
        victory +=1
    elif result <= 5:
        match_end = "LOSS"
        defeat += 1
    else:
        match_end = "TIE"
        points += 1
        tie += 1
    games_played += 1"""

#Versión con For ---> """ para comentar todo el bucle
for matches in range(1, 39):
    result = random.randint(1, 10)
        
    if result == 1 or result == 2:
        match_end = "WIN"
        points += 3
        victory +=1
    elif result <= 5:
        match_end = "LOSS"
        defeat += 1
    else:
        match_end = "TIE"
        points += 1
        tie += 1

print("The team has ended the season with: " + str(points)
      + " points which are " + str(victory) + " wins, "+
      str(tie) + " ties and " + str(defeat) + " loses in " + str(matches) + " games played")

#print("The team finished with a " + match_end)