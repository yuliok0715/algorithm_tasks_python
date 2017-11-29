n = int(input("input your number"))


def sum_dig(n):
    return n % 10 + sum_dig(n // 10) if n > 0 else 0


print(sum_dig(n))
