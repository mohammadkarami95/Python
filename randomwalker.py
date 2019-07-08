import sys
import random

n = int(sys.argv[1])
trials = int(sys.argv[2])
dead_ends = 0
#up : (x, y + 1)
#down: (x, y - 1)
#left : (x - 1, y)
#right : (x + 1, y)
for t in range(trials):
    a = [[False]* n for i in range(n)]
    x, y = n // 2, n // 2
    # shorute barname
    while 0 < x < n - 1 and 0 < y < n - 1 :
        if a[x - 1][y] and a[x + 1][y] and a[x][y + 1] and a[x][y - 1]:
            dead_ends += 1
            break
        a[x][y] = True
        r = random.random()
        if r < 0.25:
            if not a[x + 1][y]: x += 1
        elif r < 0.5:
            if not a[x - 1][y]: x -= 1
        elif r < 0.75:
            if not a[x][y + 1]: y += 1
        else:
            if not a[x][y - 1]: y -= 1
print(str(100 * dead_ends / trials) + '%' + ' dead ended!')
