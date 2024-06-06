import random

number_of_streaks = 0

for experiment_number in range(10000):
    # code that creates a list of 100 heads or tails values
    coin_value = ""
    for coin_flip in range(100):
        coin_value += str(random.randint(0, 1))
    # code that checks if there is a streak of 6 heads or tails in a row
    for index, coin in enumerate(coin_value):
        if index == 0: current_streak = 0
        elif coin == coin_value[index - 1]: current_streak += 1
        else: current_streak = 0
        if current_streak == 6: number_of_streaks += 1

print("chance of streak: %s%%" % (number_of_streaks / 1000000))