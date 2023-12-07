# индексы

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

index = list()
count = 0

for i in list_1:
    if (i >= min_number and i <= max_number):
        index.append(count)
    count += 1

for i in index:
    print(i)