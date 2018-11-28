# 插入排序

import random
list_date = []

for i in range(10):
    list_date.append(random.randint(0, 20))
print(list_date)

list_len = len(list_date)

for i in range(1, list_len):
    j = 0
    while j < i:
        if list_date[j] > list_date[i]:
            break
        j = j + 1
    tmp = list_date[i]
    k = i
    while k > j:
        list_date[k] = list_date[k - 1]
        k = k - 1
    list_date[k] = tmp
print(list_date)
