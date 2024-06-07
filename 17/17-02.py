daily_food = [0, 150, 150]
def count_food(days):
    return sum(daily_food[min(days) - 1: max(days)])


print(count_food([2, 3]))