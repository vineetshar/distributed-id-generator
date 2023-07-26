#id generation inspired from twitter's snowflake
#runs internally on app servers , not a service 

# [41 - epoc mils, 10 - machine id, 12 - counter]  - id
# example , machine 1 [timestamp1, 1, 1],[timestamp1, 1, 2],[timestamp1, 1, 3]
# example , machine 2 [timestamp1, 2, 1],[timestamp1, 2, 2],[timestamp1, 2, 3]

from operator import concat
import time

def int_to_bits(value, bit_length):
    if not isinstance(value, int) or value < 0:
        raise ValueError("Input value must be a non-negative integer.")
    if not isinstance(bit_length, int) or bit_length <= 0:
        raise ValueError("Bit length must be a positive integer.")

    binary_string = bin(value)[2:]  # Convert value to binary string (remove '0b' prefix)
    binary_string = binary_string.zfill(bit_length)  # Pad with leading zeros to reach the desired bit length

    return binary_string

machineid =1
counter =0

def getCounter():
    global counter
    counter+=1
    return counter

def uidv4(machineid):
    global counter

    current_timestamp = round(time.time() * 1000)
    timestamp_bits = int_to_bits(current_timestamp,42)
    machineid_bits = int_to_bits(machineid,10)
    counter_bits = int_to_bits(getCounter(),12)
    combined =str(timestamp_bits)+str(machineid_bits)+str(counter_bits)
    return int(combined, 2)


for x in range(10):
    time.sleep(0.1)
    #example app server 1 for tweets
    print(uidv4(1))
    #example app server 2 for retweets
    print(uidv4(2))

