#Monte Carlo sims max-central-limit-theoreum

import numpy as np
import random
import math
from datetime import datetime


sampleNo = 10000
stake = 0.2
mu = 200.0
sigma = math.sqrt(mu*(1.0-stake))
n = 7

m=0
k=0
while k < 100:

    i = 0
    avg = 0

    np.random.seed(int(datetime.utcnow().timestamp()))
    s = np.random.normal(mu, sigma, sampleNo )
    while i < sampleNo:
        avg += max(s[i:i+n-1])
        i+=n
        pass

    N=((sampleNo-sampleNo%n)/n)
    #print(N)
    avg = avg/N
    if avg > m:
        m = avg

    k+=1

print(m)