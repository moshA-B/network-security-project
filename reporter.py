


#returns dict of ip : times interacted with
def count_calls(data):
    times={}
    for log in data:
        times[log[1]] = times.get(log[1], 0) + 1
    return times


#returns port nums : protocol
def map_port_numbers(data):
    proto_numbers={int(log[3]):log[4] for log in data}
    return proto_numbers