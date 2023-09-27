def pow(x, n):
    hasil = 1
    if n < 0:
        x = 1 / x
        n = -n
    while n > 0:
        if n % 2 == 1:
            hasil *= x
        x *= x
        n //= 2
    return hasil

if __name__ == '__main__':
    print(pow(2, 3)) # 8
    print(pow(7, 2)) # 49
    print(pow(10, 5)) # 100000
    print(pow(17, 6)) # 24137569
    print(pow(5, 3)) # 125
