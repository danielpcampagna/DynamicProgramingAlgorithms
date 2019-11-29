def mpc02(n):
    mat = [0]*(n+1)
    # mat.append(1)

    for i in range(0, n+1):
        mp = 0
        for j in range(0, i):
            mp = max(mp, max(j * mat[i - j], j * (i - j)))
        mat[i] = mp
    return mat

# print(MPC(10))