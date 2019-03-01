from bluetooth.ble import GATTRequester

req = GATTRequester("00:11:22:33:44:55")
req.write_by_handle(0x10, str(bytearray([14, 4, 56])))
