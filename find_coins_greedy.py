def find_coins_greedy(coins, amount):
    # Словник для збереження кількості монет кожного номіналу
    result = {}
    
    for coin in coins:
        # Перевіряємо, чи можемо використати поточний номінал для видачі решти
        if amount >= coin:
            # Обчислюємо кількість монет даного номіналу
            num_coins = amount // coin
            # Оновлюємо результат
            result[coin] = num_coins
            # Зменшуємо залишкову суму
            amount -= num_coins * coin
    
    return result