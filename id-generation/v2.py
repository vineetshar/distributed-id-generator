#multi-node-monotonically-increasing-ids

# the goal is to use timestamp in miliseconds (utc) to generate id's that is always greater than previously generated id,
# but with support for multiple servers to avoid generating same ids on multiple nodes at the same time

from operator import concat
import time

def numConcat(num1, num2):
    # Convert both the numbers to
    # strings
    num1 = str(num1)
    num2 = str(num2)
        
    # Concatenate the strings
    return int(concat(num1,num2))


def uidV2(machineId):
    uid = numConcat(machineId, round(time.time() * 1000))
    return uid;

for x in range(100):
    time.sleep(0.1)
    print(uidV2(1))
    print(uidV2(2))
    print(uidV2(3))

