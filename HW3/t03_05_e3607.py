def find(array, a, b):
    k = 0
    for num in array:
        if a <= num <= b:
            k += 1
    return k

with open("input.txt") as f:
    while True:
        n = f.readline().strip()  # Читаємо кількість елементів
        if not n:
            break
        n = int(n)
        array = [int(x) for x in f.readline().split()]
        a, b = [int(x) for x in f.readline().split()]
        print(find(array, a, b))
