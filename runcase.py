import assignment2, time, os


if not os.path.exists("./result"):
        os.mkdir("./result")
file = open("./result_time.txt","w")
for i in range(0,25):
    print("case " + str(i+1) + "================================================")
    start = time.time()
    N, M = assignment2.assign("./testcase/case"+str(i+1)+".txt","./result/case"+str(i+1)+".txt")
    file.write("case " + str(i+1) + "( N = " + str(N) + ", M = " + str(M) + " ): " + str(time.time() - start) + "\n")
    print("Complete !!!!!")
file.close()