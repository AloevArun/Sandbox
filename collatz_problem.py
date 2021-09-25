n = 27
print(n)
while n != 1:
    n = n * 3 + 1 if n % 2 != 0 else n / 2
    print(int(n))
