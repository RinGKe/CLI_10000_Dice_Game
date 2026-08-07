Description

This is a simple CLI version of a game my family created and likes to play called 10,000. Originaly played with dice, you take turns rolling to score points. The first to reach 10,000 points wins. Not rolling specific numbers can result in a bust where you lose all of the points gained during that turn. This version is you against a CPU player.

Rules

- Need to roll at least 1,000 points in one turn to get on the board
- Have to roll at least a '1', a '5', or 'combo' to keep rolling
- Combos only count on single rolls some can increase in value with additional rolls (+)
- After getting on the board players can stop anytime after their first roll to keep points
- First player to reach 10,000 points starts 'last round' of rolls
- After the 'last round' the player with the most points wins
- 1's count as 10's where die value matters

Combos and Values

- Six of a kind ( x * 800 points) + (100 for each kind in next rolls)
    - Single roll +
    - Dies of same kind in additional rolls add 100 points
    - ex: 4,4,4,4,4,4 = 3200 points + 100 for evey new 4 in next rolls

- Five of a kind ( x * 400 points) + (100 for each kind in next rolls)
    - Single roll +
    - Dies of same kind in additional rolls add 100 points
    - ex: 4,4,4,4,4 = 1600 points + 100 for evey new 4 in next rolls

- Large Straight (1500 points) - Single roll - ex: 1,2,3,4,5,6

- Four of a kind (x * 200 points) + (100 for each kind in next rolls)
    - Single roll +
    - Dies of same kind in additional rolls add 100 points
    - ex: 4,4,4,4 = 800 points + 100 for every new 4 in next rolls

- Double Trips (2500 points)
    - Single roll
    - three of two numbers
    - ex: 4,4,4,6,6,6

- Three Pairs (500 points)
    - single roll
    - ex: 6,6,4,4,3,3

- Three of a Kind (x * 100 points) + (100 for each kind in next rolls)
    - ex: 4,4,4 = 400 points + 100 for every new 4 in next rolls

- 1's Solo (100 points)

- 5's Solo (50 points)
