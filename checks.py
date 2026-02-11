from config import *

def get_external_ip(data):
    external_list=[log[1] for log in data if external_ip(log[1])]
    return external_list

def get_sensitive_port(data):
    sensitive_list=[log for log in data if sensitive_port(log[3])]
    return sensitive_list

def get_large_data(data):
    lage_list=[log for log in data if large_packet(log[5])]
    return lage_list

def tag_data_size(data):
    tag_list=[log + ["LARGE"]  if large_packet(log[5]) else log +["NORMAL"] for log in data]
    return tag_list
