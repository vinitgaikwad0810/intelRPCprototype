# create JSON-RPC client
import jsonrpc
import time
import sys
port = int(sys.argv[1])
server = jsonrpc.ServerProxy(jsonrpc.JsonRpc20(), jsonrpc.TransportTcpIp(addr=("0.0.0.0", port)))
print "GPS sensor is sending data to Logging server running on " + str(port)
# call a remote-procedure (with positional parameters)
result = server.echo("hello world")



print "Result is : " +result

def gpsSensor():
	while (1):	
		time.sleep(5)
		ret=server.gpsLogger(latitude=52.5094982,longitude=13.3765983)
		#print ret

gpsSensor()


# call a remote-procedure (with named/keyword parameters)
#found = server.search(last_name='Python')
