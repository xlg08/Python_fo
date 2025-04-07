import random
str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(4): print(str1[random.randint(0, len(str1) - 1)],end="")
