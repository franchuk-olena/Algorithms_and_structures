def max_cyclic_shift(n):
    bin_str = bin(n)[2:]
    max_val = n
    for i in range(len(bin_str)):
        bin_str = bin_str[1:] + bin_str[0]
        max_val = max(max_val, int(bin_str, 2))

    return max_val

n = int(input())
print(max_cyclic_shift(n))