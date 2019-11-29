
def mpc03(n):
    res = n%3
    if res == 0:
        return 3**(int(n/3))
    elif res == 1:
        return 3**(int(n/3)-1)*4
    else:
        return 3**(int(n/3))*2
