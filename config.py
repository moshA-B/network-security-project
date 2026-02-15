#defining suspicious activity
#all return True if suspicious

#checks if ip is local
def external_ip(ip):
    return ip[0:7]!="192.168" and ip[0:2]!="10"

#checks for sensitive ports
def sensitive_port(port):
    sens_list=["23","3389","22"]
    return port in sens_list

##checks packet size
def large_packet(pack):
    return int(pack) > 5000

#checks sus activity time
def night_activity(time):
    a,b=time.split()
    return int(b[0:2]) < 6

