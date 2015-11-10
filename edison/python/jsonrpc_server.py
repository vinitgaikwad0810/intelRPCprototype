# create a JSON-RPC-server
import jsonrpc
import json
import random
import sys
port = int(sys.argv[1])
server = jsonrpc.Server(jsonrpc.JsonRpc20(), jsonrpc.TransportTcpIp(addr=("0.0.0.0", port), logfunc=jsonrpc.log_file("myrpc.log")))
print "Logger running on Ubilinux port "+ str(port)
print "GPS sensor logs --> /var/log/gpsLog.log"
print "Emergency Detection logs --> /var/log/emergencyLog.log"
# define some example-procedures and register them (so they can be called via RPC)
def echo(s):
    return "VInit"

def gpsLogger(latitude=None,longitude=None):
	data = {}
	data['userId'] = '1234'
	data['securityToken'] = random.random()
	data['latitude'] = latitude
	data['longitude'] = longitude
	with open('/var/log/gpsLog.log', 'a') as outfile:
		json.dump(data, outfile)
		outfile.write("\n")
	return "Successfully Logged"+ str(json.dumps(data)) 


def emergencyDetection(alertType=None,latitude=None,longitude=None):
	data = {}
	data['userId'] = '1234'
	data['securityToken'] = random.random()
	data['alertType'] = alertType
	data['latitude'] = latitude
	data['longitude'] = longitude
	with open('/var/log/emergencyLog.log', 'a') as outfile:
		json.dump(data, outfile)
		outfile.write("\n")
	return "Successfully Logged"+ str(json.dumps(data))
	#print "Logging "+latitude+" and " + longitude
	#return 1

# def search(number=None, last_name=None, first_name=None):
#     sql_where = []
#     sql_vars  = []
#     if number is not None:
#         sql_where.append("number=%s")
#         sql_vars.append(number)
#     if last_name is not None:
#         sql_where.append("last_name=%s")
#         sql_vars.append(last_name)
#     if first_name is not None:
#         sql_where.append("first_name=%s")
#         sql_vars.append(first_name)
#     sql_query = "SELECT id, last_name, first_name, number FROM mytable"
#     if sql_where:
#         sql_query += " WHERE" + " AND ".join(sql_where)
#     cursor = ...
#     cursor.execute(sql_query, *sql_vars)
#     return cursor.fetchall()

server.register_function( echo )
server.register_function( gpsLogger )
server.register_function( emergencyDetection )
#server.register_function( search )

# start server
server.serve()
