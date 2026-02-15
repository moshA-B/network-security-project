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
            current.append('NIGHT_ACTIVITY')
        if large_packet(log[5]):
            current.append('LARGE_PACKET')
        if log[1] in sus_dict:
            for i in sus_dict[log[1]]:
              if i not in current:
                  current.append(i)
        if len(current)>0:
            sus_dict[log[1]]=sus_dict.get(log[1],current)
    return sus_dict


#returns dictionary of ip's with multiple suspicions ot of a "sus" dict
def very_suspicious(data):
    more_sus={k:v for k,v in data.items() if len(v) > 1}
    return more_sus

#function to save only the time
timstamps=["2024-01-15 11:02:30","2024-01-15 08:02:30"]
time_list=map(lambda x: int(x[11:13]),timstamps )
