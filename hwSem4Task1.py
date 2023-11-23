var1 = '5 4' 
var2 = '1 5 3 7 9' 
var3 = '2 5 4 3'

x = set(var2.split())
y = set(var3.split())
z = list()

for i in x.intersection(y):
    z.append(int(i))
z.sort()

for i in z:
    print(i, end=' ')
