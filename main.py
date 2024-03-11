from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins
from measure_time import measure_time

coins = [50, 25, 10, 5, 2, 1]

# Тестування алгоритмів для суми 113 за умовою завдання
amount = 113

print("Результат для суми 113:")
print("Жадібний алгоритм:", find_coins_greedy(coins, amount))
print("Динамічне програмування:", find_min_coins(coins, amount))

# Тестування алгоритмів на великих сумах
amount = 10058

greedy_result, greedy_time = measure_time(find_coins_greedy, coins, amount)
dp_result, dp_time = measure_time(find_min_coins, coins, amount)

print("Результат для суми 10058:")
print("Жадібний алгоритм:", find_coins_greedy(coins, amount))
print("Динамічне програмування:", find_min_coins(coins, amount))
print("Час для жадібного алгоритму:", greedy_time)
print("Час для динамічного програмування:", dp_time)