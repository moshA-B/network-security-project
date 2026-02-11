


#returns dict of ip : times interacted with
def count_calls(data):
    times={}
    for log in data:
        times[log[1]] = times.get(log[1], 0) + 1
    return times

