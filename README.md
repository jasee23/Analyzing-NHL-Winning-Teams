# Analyzing-NHL-Winning-Teams

## Dataset Info
- Datasets used are in-depth stats on each NHL team for the last 3 regular seasons (82 game span)
- The datasets were downloaded here: https://moneypuck.com/data.htm

## Important Notes
xGoalsPercentage:
The xGoalsPercentage stat is used to measure the quality of a team's scoring chances. Simply put, the higher the number is, the greater chance that a scoring opportunity will result in a goal.

corsiPercentage:
The corsiPercentage stat is a measure of the quantity of shots. It is calculated by taking the number of shot attempts a team has and dividing that by the sum of shot attempts for and against. This includes blocked shots. A corsi percentage over 50% implies that a team creates more chances than it gives up.

fenwickPercentage:
The fenwickPercentage stat quantifies how much a team controls the play. It is calculated with the same formula as corsi, though fenwick disregards blocked shots. Just like corsi, a percentage of over 50% shows that a team is controlling the play. 
