arr = [5, 8, 6, 4, 9, 2, 7, 3]

sum = []
i = 0
while (i < len(arr)):
    sum.append(arr[i-2] + arr[i-1] + arr[i])
    i += 1

print(max(sum))

    