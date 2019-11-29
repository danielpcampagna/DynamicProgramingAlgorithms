
def mpc01(n):
    if n <= 1:
        return 0

    max_p = 0
    for i in range(1, n-1):
        p1 = i * (n-i)
        p2 = i * mpc01(n-i)

        if p1 > max_p:
            max_p = p1

        if p2 > max_p:
            max_p = p2

    return max_p