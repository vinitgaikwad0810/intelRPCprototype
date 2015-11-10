# create JSON-RPC client
import jsonrpc
import time
import sys
port = int(sys.argv[1])
server = jsonrpc.ServerProxy(jsonrpc.JsonRpc20(), jsonrpc.TransportTcpIp(addr=("0.0.0.0", port)))
print "Accelerometer is sending data to Logging server running on " + str(port)
# call a remote-procedure (with positional parameters)


def accelerometerProcessing():
	while (1):	
		time.sleep(5)
		ret=server.emergencyDetection(alertType="Fall",latitude=52.5094982,longitude=13.3765983)
		#print ret

accelerometerProcessing()


# call a remote-procedure (with named/keyword parameters)
#found = server.search(last_name='Python')
