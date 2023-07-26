# monotonically-increasing-single-server
# the goal is to use timestamp in miliseconds (utc) to generate id's that is always greater than previously generated id
import time

def uidV1():
    uid = round(time.time() * 1000)
    return uid;

for x in range(100):
    time.sleep(0.1)
    uid = uidV1()
    print(uid,"-",uid.to_bytes((uid.bit_length() + 7) // 8, 'big').__len__())


#note : instead of timestamp, we can use a static counter too