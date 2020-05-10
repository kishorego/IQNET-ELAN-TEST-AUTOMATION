import json
import os
import sys
import yaml
import sth
import time
from pprint import pprint
# file_path =  os.path.pardir()
# print file_path
# file_path =  os.path.dirname(os.path.basename(__file__))
file_path = os.path.dirname(os.path.realpath(__file__))
def get_data():
    with open( file_path + '\..\Topology\Spirent_Test_Topology.yaml') as data_file:
        data = yaml.load(data_file,Loader=yaml.FullLoader)
    interface_config = data['sth_interface_config']
    Booked_ports = data['Spirent_Port_Booking']
    Stream_config = data['Spirent_stream_config']
    Spirent_Test_Infra = data['Spirent_Test_Infrastructure']
    Stream_Name = data['Stream_Names']
    return (Booked_ports, interface_config, Stream_config, Spirent_Test_Infra, Stream_Name)

Booked_ports, Interface_config, Stream_config, Spirent_Test_Infra,Stream_Name = get_data()
Number_of_ports = Spirent_Test_Infra['Number_of_ports']
Number_of_streams_per_Port = Spirent_Test_Infra['Number_of_streams_per_Port']
Total_Number_of_stream = Spirent_Test_Infra['Total_Number_of_stream']
Initial_MAC_address = Spirent_Test_Infra['Initial_MAC_address']

##############################################################
#Creation of Spirent Test config with log file
##############################################################

test_sta = sth.test_config (
		log                                              = '1',
		logfile                                          = 'SteamConfig-WithPercentageTraffic_logfile',
		vendorlogfile                                    = 'SteamConfig-WithPercentageTraffic_stcExport',
		vendorlog                                        = '1',
		hltlog                                           = '1',
		hltlogfile                                       = 'SteamConfig-WithPercentageTraffic_hltExport',
		hlt2stcmappingfile                               = 'SteamConfig-WithPercentageTraffic_hlt2StcMapping',
		hlt2stcmapping                                   = '1',
		log_level                                        = '7');

status = test_sta['status']
if (status == '0') :
	print("run sth.test_config failed")
	print(test_sta)

##############################################################
#config the parameters for optimization and parsing
##############################################################

test_ctrl_sta = sth.test_control (
		action                                           = 'enable');

status = test_ctrl_sta['status']
if (status == '0') :
	print("run sth.test_control failed")
	print(test_ctrl_sta)

##############################################################
#connect to chassis and reserve port list
##############################################################
i = 0
device = "10.91.113.124"
port_list = list(Booked_ports.values())
Streams = list(Stream_Name.values())
port_handle = []
intStatus = sth.connect (
		device                                           = device,
		port_list                                        = port_list,
		break_locks                                      = 1,
		offline                                          = 0 )

status = intStatus['status']

if (status == '1') :
	for port in port_list :
		port_handle.append(intStatus['port_handle'][device][port])
		i += 1
else :
	print("\nFailed to retrieve port handle!\n")
	print(port_handle)

##############################################################
#Spirent Ports configuration
##############################################################
for i in range(len(port_list)) :
	Interface_config['port_handle'] = port_handle[i]
	int_ret0 = sth.interface_config (**Interface_config)
	status = int_ret0['status']
	if (status == '0') :
		print("run sth.interface_config failed")
		print(int_ret0)

##############################################################
#stream config
##############################################################
for i in range(len(port_list)) :
	Stream_config['port_handle'] = port_handle[i]
	if(i == 0) :
		Stream_config['dest_port_list'] = port_handle[i+1]
	else :
		Stream_config['dest_port_list'] = port_handle[i - 1]
	Stream_config['name'] = Streams[i]
	streamblock_ret1 = sth.traffic_config(**Stream_config)
	status = streamblock_ret1['status']
	if (status == '0') :
		print("run sth.traffic_config failed")
		print(streamblock_ret1)

#############################################################
#start traffic
##############################################################
print("Traffic Started")
traffic_ctrl_ret = sth.traffic_control (
		port_handle                                      = [port_handle[0],port_handle[1]],
		action                                           = 'run',
        duration                                         = '30');

status = traffic_ctrl_ret['status']
if (status == '0') :
	print("run sth.traffic_control failed")
	print(traffic_ctrl_ret)
print("Test Traffic Stopped now adding delay before collecting stats")
time.sleep(30)
print("Traffic collection started")

##############################################################
#start to get the traffic results
##############################################################
traffic_results_ret = sth.traffic_stats (
		port_handle                                      = [port_handle[0],port_handle[1]],
		mode                                             = 'all');

status = traffic_results_ret['status']
if (status == '0') :
	print("run sth.traffic_stats failed")
	print(traffic_results_ret)
##############################################################
#Get required values from Stats
##############################################################
Streams_rx_stat = []
Streams_tx_stat = []
for i in range(1,Number_of_ports+1):
	Port_Index = 'port'+ str(i)
	Stream_Index = 'streamblock' + str(i)
	Streams_rx_stats = traffic_results_ret[Port_Index]['stream'][Stream_Index]['rx']
	Streams_tx_stats = traffic_results_ret[Port_Index]['stream'][Stream_Index]['tx']
	Streams_rx_stat.append(int(Streams_rx_stats['total_pkt_bytes']))
	Streams_tx_stat.append(int(Streams_tx_stats['total_pkt_bytes']))

if((Streams_tx_stat[0] == Streams_rx_stat[1]) and (Streams_tx_stat[1] == Streams_rx_stat[0])):
	print("Great Test Case is passed")
	print("streamblock1 TX = ", Streams_tx_stat[0], "streamblock1 RX = ", Streams_rx_stat[0], "streamblock2 TX = ",
		  Streams_tx_stat[1], "streamblock2 RX = ", Streams_rx_stat[1])
else:
	print("Oops Tst Case Failed")
	print("streamblock1 TX = ", Streams_tx_stat[0], "streamblock1 RX = ", Streams_rx_stat[0], "streamblock2 TX = ",
		  Streams_tx_stat[1], "streamblock2 RX = ", Streams_rx_stat[1])
	Stream1_packet_loss_in_msec = ((Streams_tx_stat[0] - Streams_rx_stat[1]) / 1000)
	Stream2_packet_loss_in_msec = ((Streams_tx_stat[1] - Streams_rx_stat[0]) / 1000)
