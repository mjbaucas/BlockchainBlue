from gattlib import GATTRequester
import time

req = GATTRequester("B8:27:EB:F1:GC:F3", False)
#name = req.read_by_uuid("00002a00-0000-1000-8000-00805f9b34fb")[0]

import time

check = 1
while(check == 1):
	try:
        steps = req.read_by_handle(0x10)[0]
        print(steps)
        check = 1
    except Exception as e:
        check = 0
        time.sleep(0.5)
