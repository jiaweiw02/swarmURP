
arr = [i for i in range(0, 100)]
for x in arr:
    if x > 4:
        x = x - 3
    else:
        if x < -4:
            x = x + 3
        else:
            x = x + 1
    print(x)

