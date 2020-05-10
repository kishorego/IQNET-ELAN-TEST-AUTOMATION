R1_interface_data = {
    'description' : 'ABC123IfType[Access] LinkID[LON/LON/LE-500121-LA]',
    'mtu': 9187
}

R2_interface_data = {
    'description' : 'DEF123IfType[Access] LinkID[LON/LON/LE-500121-LB]',
    'mtu': 9187
}
R3_interface_data = {
    'description' : 'DEF123IfType[Access] LinkID[LON/LON/LE-500121-LB]',
    'mtu': 9187
}

R1_sub_interface_data = {
    'description': 'IfType[Access] LinkID[LON/LON/LE-500121-LA]',
    'encapsulation': 'default',
    'encapsulation_dot1q': 4095,
    'service_policy_Input': 'BW-1Gbps-Class-ST',
    'service_policy_Output': 'SHAPE-1000000Kbps-Class-ST-GE'
    }

R2_sub_interface_data = {
    'description': 'IfType[Access] LinkID[LON/LON/LE-500121-LA]',
    'encapsulation': 'default',
    'encapsulation_dot1q': 4095,
    'service_policy_Input': 'BW-1Gbps-Class-ST',
    'service_policy_Output': 'SHAPE-1000000Kbps-Class-ST-GE'
  }
R3_sub_interface_data = {
    'description': 'IfType[Access] LinkID[LON/LON/LE-500121-LA]',
    'encapsulation': 'dot1q',
    'encapsulation_dot1q': 100,
    'service_policy_Input': 'BW-1000000Kbps-Class-B2-GE',
    'service_policy_Output': 'SHAPE-1000000Kbps-Class-ST-GE'
  }

R1_l2vpn_data = {
    'bridge_group': 'EPN-8111111-S1',
    'bridge_domain': 'EPN-8111111-S1',
    'MAC_maximum': 100,
    'MAC_action': 'no-flood',
    'mtu': 9208,
    'evi': 2455
}

R2_l2vpn_data = {
    'bridge_group': 'EPN-8111111-S1',
    'bridge_domain': 'EPN-8111111-S1',
    'MAC_maximum': 100,
    'MAC_action': 'no-flood',
    'mtu': 9208,
    'evi': 2455
}

R3_l2vpn_data = {
    'bridge_group': 'EPN-8111111-S1',
    'bridge_domain': 'EPN-8111111-S1',
    'MAC_maximum': 100,
    'MAC_action': 'no-flood',
    'mtu': 9208,
    'evi': 2455
}

R1_evpn_data = {
    'evi': '2455',
    'rt_import': '8220001:2455',
	'rt_export': '8220001:2455'
}

R2_evpn_data = {
    'evi': '2455',
    'rt_import': '8220001:2455',
	'rt_export': '8220001:2455'
}

R3_evpn_data = {
    'evi': '2455',
    'rt_import': '8220001:2455',
	'rt_export': '8220001:2455'
}
EPN_Result = {'Bridge_Domain_State': 'up', 'EVPN_State': 'up'}

Accedian_CFM_Result = {'Fault_Notifications_State': 'Reset', 'Highest_Defect_Priority': 'None'}

Accedian1_vid_set_data = {
    'nniVidSetName': 'N1_EPN-8111111-S1',
    'Outer_VLAN_Type': 'c-vlan',
    'Outer_VLAN_ID': 100
}
Accedian2_vid_set_data = {
    'nniVidSetName': 'N1_EPN-8111111-S1',
    'Outer_VLAN_Type': 'c-vlan',
    'Outer_VLAN_ID': 100
}
Accedian_NNI_BW_Regulator = {
    'nniRegulatorName': 'N1_EPN-8111111-S1',
    'nniCirValue': 1000000,
    'nniCBSValue': 1000
}

Accedian1_NNI_Policy_set_data = {
    'nniPolicyName': 'N1_EPN-8111111-S1',
    'nniPolicyId': 20
}


Accedian2_NNI_Policy_set_data = {
    'nniPolicyName': 'N1_EPN-8111111-S1',
    'nniPolicyId': 20
}

Accedian1_CFM_set_data = {
    'meg_Name': 'EPN-8111111-S1',
    'ccm_Interval': 1000,
    'index': 1,
    'level': 1,
    'rmep_auto_discovery': 'disable',
    'local_mep_Id':1,
    'remote_mep_Id_list': '2',
    'priority':3
}

Accedian2_CFM_set_data = {
    'meg_Name': 'EPN-8111111-S1',
    'ccm_Interval': 1000,
    'index': 1,
    'level': 1,
    'rmep_auto_discovery': 'disable',
    'local_mep_Id':2,
    'remote_mep_Id_list': '1',
    'priority':3
}

sub_interface_1 = '100'
sub_interface_2 = '100'
sub_interface_3 = '4097'
sub_interface_4 = '4095'

status_up = 'up'
established = 'Established'
zero = '0'
routing_instances = ['LAN1-VRF']
protocols = ['BGP']
indirect = 'Indirect'

local_mep_info = "Local MEPs: 1 total: all operational, no errors"
peer_mep_info = "Peer MEPs: 1 total: all operational, no errors"

cmd1 = 'set interfaces vni-0/1 unit 0 enable false'
cmd2 = 'delete interfaces vni-0/1 unit 0 enable false'
cmd3 = 'set interfaces vni-0/2 unit 0 enable false'
cmd4 = 'delete interfaces vni-0/2 unit 0 enable false'