import time
from solution01 import mpc01
from solution02 import mpc02

for i in range(10, 24):
    s1 = time.time()
    res1 = mpc01(i)
    e1 = time.time()

    s2 = time.time()
    res2 = mpc02(i)[-1]
    e2 = time.time() 

    print(i, res1, format(e1-s1, 'f'), res2, format(e2-s2, 'f'))