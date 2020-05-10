#!/usr/bin/env python

from datetime import datetime
from netmiko import ConnectHandler
import time
import json
import os
import sys

# file_path =  os.path.pardir()
# print file_path
# file_path =  os.path.dirname(os.path.basename(__file__))
file_path = os.path.dirname(os.path.realpath(__file__))
def get_data():
    with open( file_path + '/../Topology/EPN_Topology_file.json') as data_file:
       data = json.load(data_file)
    return data


# devices_dict = get_data()
# devicename = 'R1'
# a_device = devices_dict['Device_Details'][devicename]
# print a_device
# print type(a_device)
# raw_input("prrrr")

def make_connection(a_device):
    #devices_dict = get_data()
    #a_device = devices_dict['Device_Details']['R1']
    net_connect = ConnectHandler(**a_device)
    #net_connect.enable()
    print (net_connect)
    time.sleep(5)
    print ("{}: {}".format(net_connect.device_type, net_connect.find_prompt()))
    return net_connect

def close_connection(net_connect):
    net_connect.disconnect()
    print (str(net_connect) + " connection closed")


def main():
    # device_list = [cpe19]
    start_time = datetime.now()
    # for a_device in device_list:
    #     #print type(a_device)
    #     net_connect = make_connection(a_device)
    #     Commands.ping(net_connect, dest_ip='127.0.0.1', source='127.0.0.1')
    #     close_connection(net_connect)

if __name__ == "__main__":
    main()