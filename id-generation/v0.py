import uuid
import time

for x in range(100):
    time.sleep(0.1)
    id = uuid.uuid4()
    print(id,"-",id.bytes.__len__())