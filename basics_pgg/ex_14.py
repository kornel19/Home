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
"""

player_x = 4
player_y = 4

treasure_x = 6
treasure_y = 6

while True:
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

    # we should check players and treasure position
    if player_x == treasure_x and player_y == treasure_y:
        print('Congrats! You have found a treasure!!! Good job!')
        break

    # check if the user is outside of the board -> game over
    # if player_x < 0 or player_x > 10 or player_y < 0 or player_y > 10:
    if not (0 <= player_x <= 10) or not (0 <= player_y <= 10):
        print('You are outside of the board! Game over!')
        break


