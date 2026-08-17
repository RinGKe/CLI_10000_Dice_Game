Description

This is a simple CLI version of a game my family created and likes to play called 10,000. Originaly played with dice, you take turns rolling to score points. The first to reach 10,000 points wins. Not rolling specific numbers can result in a bust where you lose all of the points gained during that turn. This version is you against a CPU player.

Rules

- Need to roll at least 1,000 points in one turn to get on the board
- Have to roll and keep at least a '1', a '5', or 'combo' to keep rolling
- Not rolling or keeping any scorable dice results in a BUST ending your turn
- Combos only count on single rolls
- Some combos can increase in value with additional rolls (+) during the same cup
- After getting on the board players can stop anytime after their first roll to keep points
- First player to reach 10,000 points starts 'last round' of rolls
- After the 'last round' the player with the most points wins
- 1's count as 10's where die value matters in combos

CLI Game Directions

- When prompted, you can type a response and press ENTER to submit it
- Submitting nothing counts as yes to (Y/N) questions
- Type every die value you want to keep and confirm with ENTER. Spaces don't matter and only numbers that exist in the roll will count.
- Submitting nothing for dice selection auto fills all dice and scores possible combos for you
- CPU opponents play and make choices by themselves

Game Settings Options

- "Use game setting defaults?":
    - ENTERING "y" or nothing will use the default game settings of one player, one cpu, and normal speed
    - ENTERING "n" will lead to additional questions to set the game settings
- "How many players?":
    - ENTER the number of live players you want to play
    - You can enter "0" for this if you want to watch cpus play eachother
- "How man computer opponents?":
    - ENTER the number of CPU opponents you want to play
    - You can enter "0" if you don't want any CPUs playing
- "Game speed?":
    - ENTER one of the four given options this determains how fast the game prints information
    - "Slow": gives plenty of time to read every line as printed
    - "Normal": a balanced speed for reading lines and good pace
    - "Fast": difficult to read each line but makes for quicker games
    - "Hyper": speed is not readable if you only care about the results

Combos and Values

- Spider Eyes (10,000 points)
    - Single roll
    - six ones
    - ex: 1,1,1,1,1,1

- Six of a kind ( x * 800 points) + (100 for each kind in next rolls)
    - Single roll +
    - Dies of same kind in additional rolls add 100 points
    - ex: 4,4,4,4,4,4 = 3200 points + 100 for evey new 4 in next rolls

- Five of a kind ( x * 400 points) + (100 for each kind in next rolls)
    - Single roll +
    - Dies of same kind in additional rolls add 100 points
    - ex: 4,4,4,4,4 = 1600 points + 100 for evey new 4 in next rolls

- Large Straight (1500 points)
    - Single roll
    - ex: 1,2,3,4,5,6

- Small Straight (1000 points)
    - Single roll
    - ex 1,2,3,4,5

- Four of a kind (x * 200 points) + (100 for each kind in next rolls)
    - Single roll +
    - Dies of same kind in additional rolls add 100 points
    - ex: 4,4,4,4 = 800 points + 100 for every new 4 in next rolls

- Double Trips (2500 points)
    - Single roll
    - three of two numbers
    - ex: 4,4,4,6,6,6

- Three Pairs (750 points)
    - single roll
    - ex: 6,6,4,4,3,3

- Three of a Kind (x * 100 points) + (100 for each kind in next rolls)
    - ex: 4,4,4 = 400 points + 100 for every new 4 in next rolls

- 1's Solo (100 points)

- 5's Solo (50 points)
