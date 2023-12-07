# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.

stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
vowels = 'уеыаоэяию'
phrases = stroka.split() 
counterList = list()
count = 0
if ( len(phrases) <= 1):
    print('Количество фраз должно быть больше одной!')
else:
    for i in phrases:
        count = 0
        for j in i:
            for k in vowels:
                if (j == k):
                    count += 1
                
        counterList.append(count)
    if (sum(counterList)/len(counterList) == counterList[0]):
        print('Парам пам-пам')
    else: print('Пам парам')
