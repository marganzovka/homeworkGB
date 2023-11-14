#  На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх, и равно 1, если i-я монетка лежит решкой вверх. Размер списка не превышает 1000 элементов.
coins = [0, 1, 0, 1, 1, 0]
count = 0
for i in coins:
    if (i == 0):
        count += 1
if (count < len(coins)-count):
    print(count)
else: print(len(coins)-count)
