from bluetooth.ble import GATTRequester
import time

req = GATTRequester("B8:27:EB:B4:34:F1", False)

check = 0
while(check == 1):
	try:
		req.write_by_handle(0x10, str(bytearray([14, 4, 56])))
	    check = 0
	except Exception as e:
		check = 1
		time.sleep(1)

