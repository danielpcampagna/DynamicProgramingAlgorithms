import time
from solution02 import mpc02

for i in range(100, 1000):

    s2 = time.time()
    res2 = mpc02(i)[-1]
    e2 = time.time() 
    
    print(i, res2, format(e2-s2, 'f'))