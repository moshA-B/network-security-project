from config import *

#returns dictionary of suspicious ip as key : list of the allegations as value
def suspicious(data):
    sus_dict={}
    for log in data:
        current=[]
        if external_ip(log[1]):
            current.append('EXTERNAL_IP')
        if sensitive_port(log[3]):
            current.append('SENSITIVE_PORT')
        if night_activity(log[0]):
            current.append('NIGHT ACTIVITY')
        if large_packet(log[5]):
            current.append('LARGE_PACKET')
        if len(current)>0:
            sus_dict[log[1]]=sus_dict.get(log[1],current)
    return sus_dict


