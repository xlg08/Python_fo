a = 0
ku = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
for _ in range(1000):
    for i in ku:
        a += 1
        if a > 4:
            break
        else:
            pass
            print(i, end="")
            # print()
            # print(f"{i}:{hash(i)}",end=" ")
    a = 0
    print()

