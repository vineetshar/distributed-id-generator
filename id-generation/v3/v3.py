#central-id-generation-service
#AMAZON-ID-GENERATION

#IMAGE SERVICE REQUIRES - 500 ID
#OUR SERVICE WILL BLOCK THOSE 500 IDS IN DB , AND RETURN THEM TO RELEVANT SERVICE TO USE

from operator import concat
import time


def numConcat(num1, num2):
    # Convert both the numbers to
    # strings
    num1 = str(num1)
    num2 = str(num2)
    # Concatenate the strings
    return int(concat(num1,num2))

counter=0

def getCounter():
    global counter
    counter+=1
    return counter


def uidV3(machineId,range_value):
    if range_value <= 0 or range_value > 1000:
        raise ValueError("Range must be between 1 and 1000.")

    # Generate and insert entries into the database
    id_list = []
    for _ in range(range_value):
        generated_id = numConcat(machineId, getCounter())
        id_list.append(generated_id)

    return id_list


# Example usage:
try:
    print(uidV3(1,10))  # Generate and insert 10 entries into the database
    print(uidV3(2,10))  # Generate and insert 10 entries into the database
    print(uidV3(3,5))  # Generate and insert 10 entries into the database
except ValueError as e:
    print(str(e))