"""
Write a game of treasure hunting on a two-dimensional board 10 x 10.
The user can enter commands to change the position of the character.
After each move, the user should be notified if he is heading in the right direction.
Going beyond the board means the end of the game.
After finding the treasure, write down the number of moves used by the user to reach the goal.

Additionally:
- after taking more steps than twice the minimum number of steps, put the treasure in a new place
- with 1/5 probability, don’t give the player a clue after completing the step

STAGE 1 - moving around the board
1. Define variables with user and treasure position on a board (start with hardcoding the position)
2. Crete infinite while loop, where:
- we show the users position
- asking the user about move direction (w, s, a, d)
- change the direction or inform the user that the direction is incorrect

"""

# define treasure x and y coordinates in separate variables
# define user x and y coordinates in separate variables
player_x = 4
player_y = 4

treasure_x = 6
treasure_y = 6

# while True loop where the whole game will happen
while True:
    # display where the user is

    # ask where he wants to go