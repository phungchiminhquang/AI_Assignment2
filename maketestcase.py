import numpy
import copy
import math
import random
import os

def makecase(step,numcase,a):
    if not os.path.exists("./testcase"):
        os.mkdir("./testcase")
    for j in range(a, a + numcase):
        file = open("./testcase/case"+str(j+1)+".txt","w")
        if (step == 1):
            low = 2
        else:
            low = 10**(step-1)
        high = 10**step - 1
        file.write(str(random.randint(0,high)) + " " + str(random.randint(0,high)) + "\n")
        N = random.randint(low,high)
        M = random.randint(1,N-1)
        file.write(str(N) + " " + str(M) + "\n")
        for i in range(0,N):
            file.write(str(random.randint(0,high)) + " " + str(random.randint(0,high)) + " " + str(random.randint(1,high)) + " " + str(random.randint(1,high)) )
            if (i!=N-1):
                file.write("\n")
        file.close()
    

#Main
a = 0
for i in range(1,4):
    makecase(i,9,a)
    a = a + 9




