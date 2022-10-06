a = [int(x) for x in input("Введите элементы через строчку: ").split()]
delta = int(input("Дельта = "))
minim = 100000000000000
count = 0
n = len(a)
for i in range(n):
    if a[i] < minim:
        minim = a[i]

for i in range(n):
    if a[i] - delta == minim:
        count += 1

print(count)