from gattlib import GATTRequester

req = GATTRequester("00:11:22:33:44:55", False)
name = req.read_by_uuid("00002a00-0000-1000-8000-00805f9b34fb")[0]
steps = req.read_by_handle(0x15)[0]
