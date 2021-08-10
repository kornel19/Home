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

STAGE 2 - Check users position
1. If the user moved outside of the board we are ending the game
2. If users position (x, y) are the same as treasures position (x, y) inform the user that he won and end the game

STAGE 3 - number of tries/steps
1. Define proper variable before the loop
2. After each move we are incrementing this value in this variable
3. If players position and treasure position is the same, then he won the game and we show how many moves he did.

STAGE 4 - hot&cold
https://www.calculatorsoup.com/calculators/geometry-plane/distance-two-points.php
1. Calculate the distance BEFORE players move.
2. Calculate the distance AFTER players move.
3. Based on those two values we show to the user information if he's getting closer or further from the treasure.

STAGE 5 - do not show hint with 1/5 probability
1. use randint(1,5) - if the number we get is different than 5 then we do show the hint.
"""

from math import sqrt

player_x = 4
player_y = 4

treasure_x = 6
treasure_y = 6

moves = 0

while True:
    # calculate distance before the move
    distance_before = sqrt( (treasure_x-player_x) ** 2 + (treasure_y-player_y) ** 2 )

    print(f'Your position is {player_x} {player_y}')

    direction = input('Direction (w,s,a,d): ')

    if direction == 'w':
        player_y += 1
    elif direction == 's':
        player_y -= 1
    elif direction == 'a':
        player_x -= 1
    elif direction == 'd':
        player_x += 1
    else:
        print('Wrong direction. Use w, s, a, d')
        continue

    moves += 1  # counting only valid moves

    # we should check players and treasure position
    if player_x == treasure_x and player_y == treasure_y:
        print(f'Congrats! You have found a treasure in {moves} moves!!! Good job!')
        break

    # check if the user is outside of the board -> game over
    # if player_x < 0 or player_x > 10 or player_y < 0 or player_y > 10:
    if not (0 <= player_x <= 10) or not (0 <= player_y <= 10):
        print('You are outside of the board! Game over!')
        break

    # calculate distance after the move
    distance_after = sqrt( (treasure_x-player_x) ** 2 + (treasure_y-player_y) ** 2 )

    # show to the user if he's getting closer or further from the treasure
    if distance_after < distance_before:
        print('You are getting CLOSER')
    else:
        print('You are getting FURTHER from the treasure')
