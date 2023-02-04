import sys,os
#if not os.environ.get("ONLINE_JUDGE"):
#    sys.stdin=open('../in.txt', 'r')
#    sys.stdout=open('../myout.txt', 'w')
import time
start_time = time.time()

x = [2,3,4]*5
print(x)



print("--- %s seconds ---" % (time.time() - start_time))