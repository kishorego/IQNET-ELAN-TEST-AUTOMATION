#!/usr/bin/env python
import time
from jinja2 import Template
#import templates as t1
import os
import jinja2
import textfsm

file_path = os.path.dirname(os.path.realpath(__file__))


#
# # cisco
# interface = {
#     'name': 'gigabitethernet0/0',
#     'description': 'Uplink to WAN',
#     'mtu12': '10.10.10.1 255.255.255.0',
# }
#
# template = jinja2.Template(t1.interface_template)
# output = template.render(interface=interface)
# #Print the output
# print(output)
#
# # raw_input("pppp")

def convert_mac_address_from_accedian_to_cisco_format(MAC_Value):
    list = MAC_Value.split(':')
    lower_mac_value = [x.lower() for x in list]
    mac_string=''
    mac_value = mac_string.join(lower_mac_value)
    cisco_mac_format = '.'.join(mac_value[i:i+4] for i in range(0,12,4))
    return(cisco_mac_format)

def show_commands(net_connect, **kwargs):
    print("Now Inside SHOW CMD")
    #if kwargs is not None:
    for key, value in kwargs.items():
       print ("%s == %s" %(key,value))
    #    template = Template(kwargs['template_name'])
    #tempalte_data = kwargs['template_data']
    #p=kwargs['template_data']
    #print(p.bridge_domain)
    #show_cmd = template.render(component=kwargs['template_data'])
    #output1 = net_connect.send_command_expect(show_cmd, strip_prompt=False, strip_command=False)
    template1 = Template(kwargs['template_name'])
    print("OUT of SHOW CMD of template1")
    show_cmds = template1.render(component=kwargs['template_data'])
    print("OUT of SHOW CMD after rendering")
    print(show_cmds)
    output1 = net_connect.send_command_expect(show_cmds, strip_prompt=False, strip_command=False)
    print("Show Command Output")
    print(output1)
    template_fsm = open(file_path + "/TEXTFSM/" + kwargs['textfsm_template'])
    out_table = textfsm.TextFSM(template_fsm)
    fsm_results = out_table.ParseText(output1)
    print("FSM_RESULTS")
    print(fsm_results)
    header_row = out_table.header
    for row in fsm_results:
        key_row = row
    fsm_results_str = dict(zip(header_row, key_row))
    print("GOT IT")
    print(fsm_results_str)
    return fsm_results_str

def configure_commands(net_connect, **kwargs):
    # if kwargs is not None:
    #     for key, value in kwargs.iteritems():
    #         print ("%s == %s" %(key,value))
    template = Template(kwargs['template_name'])
    template_data = kwargs['template_data']
    # if  'interface' in kwargs.keys():
    #     tempalte_data['interface'] = kwargs['interface']
    # if  'sub_interface' in kwargs.keys():
    #     tempalte_data['sub_interface'] = kwargs['sub_interface']
    cmds = template.render(component=kwargs['template_data'])
    device_type = template_data.get('device_type')
    config_commands = [cmds]
    print(cmds)
    print(device_type)
    output2 = net_connect.send_config_set(config_commands,cmd_verify=False)
    if (device_type != 'Accedian'):
     output2 = net_connect.commit()
     print("Inside Commit")
     output3 = net_connect.exit_config_mode()
    return output2


def get_interface_status(net_connect, intf_name):
    """Get interface status. Return LAN VRF name and subnet"""
    cmd = 'show interfaces brief ' + str(intf_name) + ' | tab'
    print(cmd)
    output = net_connect.send_command_expect(cmd)
    output_string = str(output)
    print(output_string)
    output_list = output_string.split("\n")
    intf_dict = {}
    keys = output_list[0].split()
    values = output_list[2].split()
    for i in xrange(len(keys)):
        intf_dict[keys[i]] = values[i]
    return intf_dict


def get_bgp_neighbor(net_connect, org):
    cmd = 'show bgp neighbor org ' + org + " brief | match ^[0-9]+"
    output = net_connect.send_command_expect(cmd)
    output_string = str(output)
    dict1 = {}
    for i in output_string.split("\n"):
        k = i.split()
        dict1[k[0]] = k[1:]
    return dict1


def get_ipsec_sa(net_connect, org, vpn_profile):
    cmd = 'show orgs org-services ' + org + ' ipsec vpn-profile ' + \
          vpn_profile + ' security-associations brief'
    output = net_connect.send_command_expect(cmd)
    output_string = str(output)
    print(output_string)
    dict1 = {}
    for i in output_string.split("\n"):
        k = i.split()
        dict1[k[0]] = k[1:]
    return dict1


def get_route(net_connect, routing_instance, protocol):
    cmd = "show route routing-instance " + routing_instance
    output = net_connect.send_command(cmd)
    # print  output
    routes = []
    for route in output.split("\n"):
        if protocol in route:
            routes.append(route)
    return routes


def check_route(routes_list, dest_address, next_hop, intf_name):
    """check_route(routes_list, '192.168.111.0/24', '10.60.68.31', 'Indirect')
    """
    for route in routes_list:
        list1 = route.split()
        if '+' + dest_address in list1:
            if next_hop in list1:
                if intf_name in list1:
                    print("-" * 20)
                    print(route)
                    print("-" * 20)
                    return True
    return False


def ping(net_connect, dest_ip, **kwargs):
    cmd = "ping " + str(dest_ip)
    paramlist = ['count', 'df_bit', 'interface', 'packet_size', 'rapid', 'record-route', 'routing_instance', 'source']
    for element in paramlist:
        if element in kwargs.keys():
            cmd = cmd + " " + element.replace('_', '-') + " " + str(kwargs[element])
    print(cmd)
    output = net_connect.send_command_expect(cmd)
    print(output)
    return str(" 0% packet loss" in output)
