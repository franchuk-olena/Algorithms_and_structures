def a(n):
    s = 0
    for x in range(1, n+1):
        s += x
    return s

def b(n):
    s = 0
    for x in range(1, n+1):
        s += x * x
    return s

def c(n, a):
    s = 0
    for i in range(n + 1):
        s += a ** i
    return s

def d(n):
    s = 0
    for i in range(n + 1):
        s += i ** i
    return s

def e(n):
    s = 1
    for i in range(1, n + 1):
        s *= 1 / (1 + i)
    return s

def f(n):
    s = 1
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        s *= 1 / (1 + fact)
    return s

def g(n, a):
    s = 1
    for i in range(1, n + 1):
        power = 1
        for j in range(i):
            power *= a
        s *= power / (1 + i)
    return s

def h(n, m):
    s = 1
    for i in range(1, n + 1):
        power = 1
        for j in range(m):
            power *= i
        s *= 1 / (1 + power)
    return s

def i(n):
    s = 1
    for i in range(1, n + 1):
        s *= 1 / (1 + i * i)
    return s