from lib.IOBluetooth import *
devices = IOBluetoothDevice.recentDevices_(1)

for d in devices:
	connected = d.isConnected()
	status = "is connected" if connected else "not connected"
	print "%s %s" % (d.getNameOrAddress(), status)

