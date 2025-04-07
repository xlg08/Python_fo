# 求 1~100之间，所有奇数的和

i = 1
sum = 0
while i <= 100:
    if i % 2 != 0:
        sum += i
    i += 1
print(sum)

a = 1
num = 0
while a <= 100:
    if a % 2 == 0:
        num += a
    a += 1

print(num)

print(sum + num)