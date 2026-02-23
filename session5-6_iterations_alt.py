# ITERATIONS
from random import randint
money = 1000000
it = 0
while money > 0:
    spend = randint(a=1, b=10000)
    it = it + 1
    print(f"Iteration {it}: I am spending {spend}")
    money = money - spend

# infinite loop with escape clause
money = 100
it = 0
while True:
    if money < 0:
        break
    it = it + 1
    spend = randint(-1, b=1)
    print(f"Iteration {it}: I am spending {spend}")
    money = money - spend

# break = get out of the while