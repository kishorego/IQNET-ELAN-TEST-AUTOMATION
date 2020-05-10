interface_template = '''
interface {{ component.interface }}
 description {{ component.description }}
 mtu {{ component.mtu }}
 service-policy output egr account user-defined 20
 no shutdown
 '''

sub_interface_template = """interface {{ component.sub_interface }} l2transport
 description {{ component.description }}
 encapsulation {{ component.encapsulation }}
 encapsulation_dot1q {{ component.encapsulation_dot1q }}
 service_policy_Input {{component.service_policy_Input}}
 service_policy_Output {{component.service_policy_Output}} account user-defined 26
 """
l2vpn_template = """
l2vpn
 bridge group {{ component.bridge_group }}
 bridge-domain {{component.bridge_domain}}
   mac
    limit
     maximum {{ component.MAC maximum }}
     maximum {{ component.MAC action }}
    exit
 exit  
 mtu {{ component.mtu }} 
 interface {{ component.attch_ckt_intf }}
    storm-control unknown-unicast kbps 20000
    storm-control multicast kbps 20000
    storm-control broadcast kbps 20000
 evi {{component.evi}}
"""

evpn_template = """
  evpn
   evi {{ component.evpn_id }}
    bgp
     route-target import {{ component.rd }}:{{ component.rt_import }}
     route-target export {{ component.rd }}:{{ component.rt_export }}
   advertise-mac
  """
unconfig_evpn_template = """
no evpn evi {{ component.evpn_id }}
"""
unconfig_l2vpn_template = """
no l2vpn bridge group {{ component.bridge_group }}
"""
unconfig_sub_interface_template = """
no interface {{ component.sub_interface }}
"""

unconfig_interface_template = '''
interface {{ component.interface }}
 no description {{ component.description }}
 no mtu {{ component.mtu }}
 no service-policy output egr account user-defined 26
 no load-interval 30
 no ethernet loopback
 shutdown
'''