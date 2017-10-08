def generator(n):
    while n >= 0:
        yield n
        n -= 1

finalcountdown = generator(int(input("Please input the first number here:")))
for x in finalcountdown:
    print(x)
print(type(finalcountdown))
