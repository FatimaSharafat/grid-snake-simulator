"""


A snake starts at (0,0) and moves right or left (50/50 chance) each step,
consuming 1 energy per move, gaining +5 energy when (row+col)%10==0.
The game ends when the snake reaches the last row or runs out of energy.
"""

import random

i = 0
x = 0
y = 0
energy = 50
moves = 0
game_over = False

while i < 50 and not game_over:
    j = 0
    while j < 50:
        if x == i and y == j and not game_over:
            print("\033[31mO", end="")
            m = random.randint(0, 1)
            # Edge case: at the last column, must move down instead of right
            if y == 49:
                x = x + 1
            elif m == 0:
                y = y + 1
            else:
                x = x + 1
            energy -= 1
            if (x + y) % 10 == 0:
                energy += 5
            moves += 1
            if x == 49 or energy <= 0:
                game_over = True
        elif x == i and y == j:
            print("\033[31mO", end="")
        else:
            print("\033[30mX", end="")
        j = j + 1
    i = i + 1
    print("")

print("\033[32mGame Over!")
print()
if energy <= 0:
    print("\033[32mReason: Out of energy")
else:
    print("\033[32mReason: Reached the Bottom")
print("\033[32mTotal Moves:", moves)
print("\033[32mRemaining Energy:", energy)
print("\033[32mFinal Position:", "(" + str(x) + ", " + str(y) + ")")
