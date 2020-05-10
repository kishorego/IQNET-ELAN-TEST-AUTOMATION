*** Settings ***
Documentation     Resource file containing all the PYTHON API implementations.
Library           String
Library           Collections
Resource          ${CURDIR}//Resource.robot    #Resource    Resource.robot
Library           Connect_devices.py
Library           Commands.py
Variables         templates.py

*** Variables ***

*** Keywords ***
Setup Actions
    Log To Console    Setup Actions done here
    #    log to console    ${CURDIR}
    ${Topo_data}    get data
    log to console    ${Topo_data}
    ${DEV_DICT}    get from dictionary    ${Topo_data}    Device_Details
    ${INTERFACE_DICT}    get from dictionary    ${Topo_data}    Interface_Details
    ${R1_INTERFACES}    get from dictionary    ${INTERFACE_DICT}    R1_Interfaces
    ${MAIN_INTERFACE_R1}    get from dictionary    ${R1_INTERFACES}    R1_Main_Interface
    ${SUB_INTERFACE_R1}    get from dictionary    ${R1_INTERFACES}    R1_Sub_Interface
    ${R2_INTERFACES}    get from dictionary    ${INTERFACE_DICT}    R2_Interfaces
    ${MAIN_INTERFACE_R2}    get from dictionary    ${R2_INTERFACES}    R2_Main_Interface
    ${SUB_INTERFACE_R2}    get from dictionary    ${R2_INTERFACES}    R2_Sub_Interface
    ${R3_INTERFACES}    get from dictionary    ${INTERFACE_DICT}    R3_Interfaces
    ${MAIN_INTERFACE_R3}    get from dictionary    ${R3_INTERFACES}    R3_Main_Interface
    ${SUB_INTERFACE_R3}    get from dictionary    ${R3_INTERFACES}    R3_Sub_Interface
    #${ACCEDIAN1_INTERFACES}    get from dictionary    ${INTERFACE_DICT}    Accedian1_Interfaces
    #${NNI_INTERFACE_ACCEDIAN1}    get from dictionary    ${ACCEDIAN1_INTERFACES}    NNI_Interface
    #${UNI_INTERFACE_ACCEDIAN1}    get from dictionary    ${ACCEDIAN1_INTERFACES}    UNI_Interface
    #${ACCEDIAN2_INTERFACES}    get from dictionary    ${INTERFACE_DICT}    Accedian2_Interfaces
    #${NNI_INTERFACE_ACCEDIAN2}    get from dictionary    ${ACCEDIAN2_INTERFACES}    NNI_Interface
    #${UNI_INTERFACE_ACCEDIAN2}    get from dictionary    ${ACCEDIAN2_INTERFACES}    UNI_Interface
    #Builtin.Set_Suite_Variable    ${ACCEDIAN1_INTERFACES}
    #Builtin.Set_Suite_Variable    ${ACCEDIAN2_INTERFACES}
    Builtin.Set_Suite_Variable    ${MAIN_INTERFACE_R1}
    Builtin.Set_Suite_Variable    ${SUB_INTERFACE_R1}
    Builtin.Set_Suite_Variable    ${MAIN_INTERFACE_R2}
    Builtin.Set_Suite_Variable    ${SUB_INTERFACE_R2}
    #Builtin.Set_Suite_Variable    ${MAIN_INTERFACE_R3}
    #Builtin.Set_Suite_Variable    ${SUB_INTERFACE_R3}
    #Builtin.Set_Suite_Variable    ${NNI_INTERFACE_ACCEDIAN1}
    #Builtin.Set_Suite_Variable    ${UNI_INTERFACE_ACCEDIAN1}
    #Builtin.Set_Suite_Variable    ${NNI_INTERFACE_ACCEDIAN2}
    #Builtin.Set_Suite_Variable    ${UNI_INTERFACE_ACCEDIAN2}
    ${R1_DICT}    get from dictionary    ${DEV_DICT}    R1
    ${R1_net_connect}    Make Connection    ${R1_DICT}
    Builtin.Set_Suite_Variable    ${R1_net_connect}
    Log To Console    Connection Establihed to RTR1
    ${R2_DICT}    get from dictionary    ${DEV_DICT}    R2
    ${R2_net_connect}    Make Connection    ${R2_DICT}
    Builtin.Set_Suite_Variable    ${R2_net_connect}
    Log To Console    Connection Establihed to RTR2
    #${R3_DICT}    get from dictionary    ${DEV_DICT}    R3
    #${R3_net_connect}    Make Connection    ${R3_DICT}
    #Builtin.Set_Suite_Variable    ${R3_net_connect}
    #Log To Console    Connection Establihed to RTR3
    # ${Accedian1_DICT}    get from dictionary    ${DEV_DICT}    Accedian1
    # ${Accedian1_net_connect}    Make Connection    ${Accedian1_DICT}
    # Builtin.Set_Suite_Variable    ${Accedian1_net_connect}
    #Log To Console    Connection Establihed to Accedian1
    # ${Accedian2_DICT}    get from dictionary    ${DEV_DICT}    Accedian2
    # ${Accedian2_net_connect}    Make Connection    ${Accedian2_DICT}
    # Builtin.Set_Suite_Variable    ${Accedian2_net_connect}
    #Log To Console    Connection Establihed to Accedian2

Teardown Actions
    Log To Console    Teardown Actions done here
    #Close Connection    ${R1_net_connect}
    #Close Connection    ${R2_net_connect}
    #Close Connection    ${R3_net_connect}
    #Close Connection    ${Accedian1_net_connect}
    #Close Connection    ${Accedian2_net_connect}

CONFIGURE INTERFACE
    [Arguments]    ${connect_id}    ${intf_name}    ${template_name}    ${template_data}
    Log To Console    Configuring Main Interface
    set to dictionary    ${template_data}    interface=${intf_name}
    set to dictionary    ${template_data}    device_type=Cisco
    ${commit_result}    Configure Commands    ${connect_id}    template_name=${template_name}    template_data=${template_data}
    log to console    ${commit_result}
    should not contain    ${commit_result}    fail
    #log to console    Interfce Config Complete

CONFIGURE SUB-INTERFACE
    [Arguments]    ${connect_id}    ${sub_intf_name}    ${template_name}    ${template_data}
    Log To Console    Configuring Sub Interface
    set to dictionary    ${template_data}    sub_interface=${sub_intf_name}
    set to dictionary    ${template_data}    device_type=Cisco
    log to console    ${template_data}
    log to console    Subinterface commit started
    ${commit_result}    Configure Commands    ${connect_id}    template_name=${template_name}    template_data=${template_data}
    should not contain    ${commit_result}    fail

CONFIGURE l2vpn-With-MainInterface-Only
    [Arguments]    ${connect_id}    ${main_intf}    ${template_name}    ${template_data}
    Log To Console    Configuring l2vpn
    set to dictionary    ${template_data}    main_interface=${main_intf}
    set to dictionary    ${template_data}    device_type=Cisco
    ${commit_result}    Configure Commands    ${connect_id}    template_name=${template_name}    template_data=${template_data}
    should not contain    ${commit_result}    fail

CONFIGURE l2vpn-With-SubIntf-Encap-Default
    [Arguments]    ${connect_id}    ${sub_intf}    ${template_name}    ${template_data}
    Log To Console    Configuring l2vpn
    set to dictionary    ${template_data}    sub_interface=${sub_intf}
    set to dictionary    ${template_data}    device_type=Cisco
    ${commit_result}    Configure Commands    ${connect_id}    template_name=${template_name}    template_data=${template_data}
    should not contain    ${commit_result}    fail

CONFIGURE l2vpn
    [Arguments]    ${connect_id}    ${sub_intf}    ${template_name}    ${template_data}
    Log To Console    Configuring l2vpn
    set to dictionary    ${template_data}    sub_interface=${sub_intf}
    set to dictionary    ${template_data}    device_type=Cisco
    ${commit_result}    Configure Commands    ${connect_id}    template_name=${template_name}    template_data=${template_data}
    should not contain    ${commit_result}    fail

CONFIGURE evpn
    [Arguments]    ${connect_id}    ${template_name}    ${template_data}
    Log To Console    Configuring evpn
    set to dictionary    ${template_data}    device_type=Cisco
    ${commit_result}    Configure Commands    ${connect_id}    template_name=${template_name}    template_data=${template_data}
    should not contain    ${commit_result}    fail

ADD VIDSET TO ACCEDIAN
    [Arguments]    ${connect_id}    ${template_name}    ${template_data}    ${nni_intf}
    set to dictionary    ${template_data}    NNI_Port_Number=${nni_intf}
    set to dictionary    ${template_data}    device_type=Accedian
    Log To Console    ${template_name}
    Log To Console    ${template_data}
    Log To Console    Now Configuring
    ${commit_result}    Configure Commands    ${connect_id}    template_name=${template_name}    template_data=${template_data}
    should not contain    ${commit_result}    Error

CONFIGURE ACCEDIAN REGULATOR
    [Arguments]    ${connect_id}    ${template_name}    ${template_data}
    set to dictionary    ${template_data}    device_type=Accedian
    ${commit_result}    Configure Commands    ${connect_id}    template_name=${template_name}    template_data=${template_data}
    should not contain    ${commit_result}    Error

CONFIGURE ACCEDIAN POLICY
    [Arguments]    ${connect_id}    ${template_name}    ${template_data}    ${nni_intf}    ${uni_intf}
    set to dictionary    ${template_data}    NNI_Port_Number=${nni_intf}
    set to dictionary    ${template_data}    UNI_Port_Number=${uni_intf}
    set to dictionary    ${template_data}    device_type=Accedian
    ${commit_result}    Configure Commands    ${connect_id}    template_name=${template_name}    template_data=${template_data}
    should not contain    ${commit_result}    Error

CONFIGURE ethernet cfm
    [Arguments]    ${connect_id}    ${template_name}    ${template_data}
    ${commit_result}    Configure Commands    ${connect_id}    template_name=${${template_name}}    template_data=${template_data}
    should not contain    ${commit_result}    fail

CONFIGURE ACCEDIAN EPN-CFM
    [Arguments]    ${connect_id}    ${template_name}    ${template_data}    ${vid_set_data}
    ${vlan_type}    get from dictionary    ${vid_set_data}    Outer_VLAN_Type
    ${vid}    get from dictionary    ${vid_set_data}    Outer_VLAN_ID
    Log To Console    Printing EPN CFM Data
    set to dictionary    ${template_data}    vid=${vid}
    set to dictionary    ${template_data}    vlan_type=${vlan_type}
    set to dictionary    ${template_data}    device_type=Accedian
    Log To Console    ${template_data}
    #Log To Console    ${${template_name}}
    ${commit_result}    Configure Commands    ${connect_id}    template_name=${template_name}    template_data=${template_data}

CONFIGURE ACCEDIAN EPN-SingleTagged-MEP
    [Arguments]    ${connect_id}    ${template_name}    ${template_data}    ${vid_set_data}    ${nni_intf}
    ${vid}    get from dictionary    ${vid_set_data}    Outer_VLAN_ID
    set to dictionary    ${template_data}    vid=${vid}
    set to dictionary    ${template_data}    NNI_Port_Number=${nni_intf}
    set to dictionary    ${template_data}    device_type=Accedian
    ${commit_result}    Configure Commands    ${connect_id}    template_name=${template_name}    template_data=${template_data}

SHOW COMMAND
    [Arguments]    ${connect_id}    ${template_name}    ${template_data}
    ${show_cmd_result}    Show Commands    ${connect_id}    template_name=${${template_name}}    template_data=${template_data}    textfsm_template=${template_name}
    [Return]    ${show_cmd_result}

UNCONFIGURE ethernet cfm
    [Arguments]    ${connect_id}    ${template_name}    ${template_data}
    ${commit_result}    Configure Commands    ${connect_id}    template_name=${template_name}    template_data=${template_data}
    should not contain any    ${commit_result}    fail

UNCONFIGURE evpn
    [Arguments]    ${connect_id}    ${template_name}    ${template_data}
    ${commit_result}    Configure Commands    ${connect_id}    template_name=${template_name}    template_data=${template_data}
    should not contain    ${commit_result}    fail

UNCONFIGURE l2vpn
    [Arguments]    ${connect_id}    ${sub_intf_name}    ${template_name}    ${template_data}
    set to dictionary    ${template_data}    attch_ckt_intf=${sub_intf_name}
    ${commit_result}    Configure Commands    ${connect_id}    template_name=${template_name}    template_data=${template_data}
    should not contain    ${commit_result}    fail

UNCONFIGURE SUB-INTERFACE
    [Arguments]    ${connect_id}    ${sub_intf_name}    ${template_name}    ${template_data}
    set to dictionary    ${template_data}    sub_interface=${sub_intf_name}
    ${commit_result}    Configure Commands    ${connect_id}    template_name=${template_name}    template_data=${template_data}
    should not contain    ${commit_result}    fail

UNCONFIGURE INTERFACE
    [Arguments]    ${connect_id}    ${intf_name}    ${template_name}    ${template_data}
    set to dictionary    ${template_data}    interface=${intf_name}
    ${commit_result}    Configure Commands    ${connect_id}    template_name=${template_name}    template_data=${template_data}
    should not contain    ${commit_result}    fail
