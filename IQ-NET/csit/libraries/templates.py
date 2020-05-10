interface_template = '''
interface {{ component.interface }}
 description {{ component.description }}
 mtu {{ component.mtu }}
 negotiation auto
 service-policy output egr account user-defined 26
 lldp
  receive disable
  transmit disable
 load-interval 30
 '''

sub_interface_template = '''
interface {{ component.sub_interface }} l2transport
 description {{ component.description }}
 encapsulation {{ component.encapsulation }} {{ component.encapsulation_dot1q }}
 service-policy input {{ component.service_policy_Input }}
 service-policy output {{ component.service_policy_Output}} account user-defined 26
'''

Default_encap_sub_interface_template = '''
interface {{ component.sub_interface }} l2transport
 description {{ component.description }}
 encapsulation default
 '''
l2vpn_Witn_One_SubInterface_template = """
l2vpn
 bridge group {{ component.bridge_group }}
  bridge-domain {{component.bridge_domain}}
   mac 
    limit
     maximum {{component.MAC_maximum}}
     action {{component.MAC_action}}
    !
   !
   mtu {{component.mtu}}  
    interface {{component.sub_interface}}
    storm-control broadcast kbps 20000
    storm-control multicast kbps 20000  
    storm-control unknown-unicast kbps 20000
   !
   evi {{component.evi}}
   !
  !
 !
!
"""
l2vpn_main_Intf_template = """
l2vpn
 bridge group {{ component.bridge_group }}
  bridge-domain {{component.bridge_domain}}
   mac 
    limit
     maximum {{component.MAC_maximum}}
     action {{component.MAC_action}}
    !
   !
   mtu {{component.mtu}}  
   interface {{ component.main_interface }}
    storm-control broadcast kbps 20000
    storm-control multicast kbps 20000  
    storm-control unknown-unicast kbps 20000
   !
   evi {{component.evi}}
   !
  !
 !
!
"""
evpn_template = """
evpn
 evi {{ component.evi }}
  bgp
   route-target import {{ component.rt_import }}
   route-target export {{ component.rt_export }}
  !
  advertise-mac
 !
"""
eth_cfm_template = """
ethernet cfm
 domain {{ component.domain_name }} level {{ component.domain_level }} id null
  service {{ component.service_name }} xconnect group {{ component.xc_group }} p2p {{ component.p2p_xc_name }} id icc-based {{ component.ICC }} {{ component.UMC }}
   continuity-check interval 1s
   mep crosscheck
    mep-id {{ component.mep_id }}
   !
   log continuity-check errors
   log crosscheck errors
   log continuity-check mep changes
"""

unconfig_eth_cfm_template = """
ethernet cfm
 domain {{ component.domain_name }} level {{ component.domain_level }} id null
  no service {{ component.service_name }}
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
 no service-policy output {{ component.output_policy }} account user-defined {{ component.acc_value }}
 no load-interval 30
 no ethernet loopback
'''
show_l2vpn_BD_template = """show l2vpn bridge-domain bd-name {{ component.bridge_domain }}"""

show_evpn_evi_mac_filter_with_specific_mac = """sh evpn evi mac | inc {{ component.Accedian_NNI_Port_MAC_In_Cisco_Format }}"""

extract_Accedian_Port_MAC_address = """port show configuration PORT-{{ component.NNI_Interface }}"""

show_eth_cfm_template = """show ethernet cfm services domain {{ component.domain_name }} service {{ component.service_name }}"""

config_vid_set = """vid-set add {{ component.nniVidSetName }} policy-list Traffic-{{ component.NNI_Port_Number }} vlan-type {{ component.Outer_VLAN_Type }} vid-list {{component.Outer_VLAN_ID }}"""

config_NNI_BW_Regulator = """bandwidth-regulator add regulator {{ component.nniRegulatorName }} cir {{ component.nniCirValue }} cir-max {{ component.nniCirValue }} cbs {{ component.nniCBSValue }} eir 0 eir-max  {{ component.nniCirValue }} ebs 10 color-mode blind coupling-flag false"""

config_NNI_Policy = """policy edit Traffic-{{ component.NNI_Port_Number }} {{ component.nniPolicyId }} state enable action permit pre-marking green regulator enable {{ component.nniPolicyName }} filter vlan {{ component.nniPolicyName }} evc-encapsulation pop cos-mapping direct green-cfi 0 green-pcp 3 yellow-cfi 0 yellow-pcp 0 out-port PORT-{{ component.UNI_Port_Number }}"""

config_Single_Tagged_CFM = """cfm add meg name {{ component.meg_Name }} name-format icc-based ccm-interval {{ component.ccm_Interval }} index {{ component.index }} mhf-creation none sndr-id-perm none  level {{ component.level }} rmep-auto-discovery {{ component.rmep_auto_discovery }} mepid-list {{ component.local_mep_Id }},{{ component.remote_mep_Id_list }}  vid-list {{ component.vid }} vlan-type {{ component.vlan_type }}"""

config_Single_Tagged_CFM_MEP = """cfm add mep name {{ component.meg_Name }}|{{ component.level }}|{{ component.local_mep_Id }} active yes index {{ component.index }} direction down cci-enable yes ccm-seq-number enable meg-idx {{ component.index }} lowest-alarm-pri macRemErrXconAis mep-id {{ component.local_mep_Id }} port PORT-{{ component.NNI_Port_Number }} priority {{ component.priority }} pvid {{ component.vid }}"""

show_accedian_cfm_status = """cfm show mep status {{ component.index }}"""