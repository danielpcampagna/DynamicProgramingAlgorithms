import time

from solution02 import mpc02
from solution03 import mpc03

for i in range(100, 500):

    s2 = time.time()
    res2 = mpc02(i)[-1]
    e2 = time.time() 

    s3 = time.time()
    res3 = mpc03(i)
    e3 = time.time()
    
    print(i, res2, format(e2-s2, 'f'), res3, format(e3-s3, 'f'))