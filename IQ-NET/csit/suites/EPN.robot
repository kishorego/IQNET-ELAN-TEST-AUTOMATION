*** Settings ***
Documentation     A test suite with tests for EPN conenctivity.
...               Topology:-
...               ____________________________
...
...
...               Testplan Goals:-
...               1. CHECK EPN service.
Suite Setup       Setup Actions
Suite Teardown    Teardown Actions
Metadata          Version    1.0\nMore Info For more information about Robot Framework see http://robotframework.org\nAuthor Sathishkumar murugesan\nDate 12 Dec 2017\nExecuted At HOST\nTest Framework Robot Framework Python
Library           Collections
Library           String
Library           OperatingSystem
Resource          ${CURDIR}/../libraries/Resource.robot
Variables         ../Variables/EPN/Variables.py
Library           ../libraries/Commands.py
Library           ../libraries/Connect_devices.py
Library           ../libraries/Spirent_Test_Suit.py
Variables         ../libraries/templates.py
Variables         ../libraries/templates.py

*** Test Cases ***
Test Creation of Two Site Main Interface Based EVPN service
    [Documentation]    TEST To Create Two Site EVPN service with Direct NCS Termination
    [Tags]    EVPN-Creation
    CONFIGURE INTERFACE    ${R1_net_connect}    ${MAIN_INTERFACE_R1}    ${interface_template}    ${R1_interface_data}
    CONFIGURE INTERFACE    ${R2_net_connect}    ${MAIN_INTERFACE_R2}    ${interface_template}    ${R2_interface_data}
    CONFIGURE SUB-INTERFACE    ${R1_net_connect}    ${SUB_INTERFACE_R1}    ${Default_encap_sub_interface_template}    ${R1_sub_interface_data}
    CONFIGURE SUB-INTERFACE    ${R2_net_connect}    ${SUB_INTERFACE_R2}    ${Default_encap_sub_interface_template}    ${R2_sub_interface_data}
    CONFIGURE l2vpn-With-SubIntf-Encap-Default    ${R1_net_connect}    ${SUB_INTERFACE_R1}    ${l2vpn_Witn_One_SubInterface_template}    ${R1_l2vpn_data}
    CONFIGURE l2vpn-With-SubIntf-Encap-Default    ${R2_net_connect}    ${SUB_INTERFACE_R1}    ${l2vpn_Witn_One_SubInterface_template}    ${R2_l2vpn_data}
    CONFIGURE evpn    ${R1_net_connect}    ${evpn_template}    ${R1_evpn_data}
    CONFIGURE evpn    ${R2_net_connect}    ${evpn_template}    ${R2_evpn_data}
    Log To Console    entering Spirent Testing
    ${Spirent_Test_Result}=    Spirent EPN Unicast Traffic Testing
    Log To Console    Out Of Spirent Testing
    Log To Console    ${Spirent_Test_Result}
    should be equal    ${Spirent_Test_Result}    Spirent Test Result Passed
    #UNCONFIGURE evpn    ${R1_net_connect}    ${unconfig_evpn_template}    ${R1_l2vpn_data}
    #UNCONFIGURE evpn    ${R2_net_connect}    ${unconfig_evpn_template}    ${R2_l2vpn_data}
    #UNCONFIGURE l2vpn    ${R1_net_connect}    ${unconfig_l2vpn_template}    ${R1_l2vpn_data}
    #UNCONFIGURE l2vpn    ${R2_net_connect}    ${unconfig_l2vpn_template}    ${R2_l2vpn_data}
    # UNCONFIGURE SUB-INTERFACE    ${R1_net_connect}    ${PORT_R1_to_R2_1}.${sub_interface_1}    ${unconfig_sub_interface_template}    ${R1_sub_interface_data}
    # UNCONFIGURE SUB-INTERFACE    ${R2_net_connect}    ${PORT_R2_to_R1_1}.${sub_interface_1}    ${unconfig_sub_interface_template}    ${R2_sub_interface_data}
    # UNCONFIGURE INTERFACE    ${R1_net_connect}    ${PORT_R1_to_R2_1}    ${unconfig_interface_template}    ${R1_interface_data}
    # UNCONFIGURE INTERFACE    ${R2_net_connect}    ${PORT_R2_to_R1_1}    ${unconfig_interface_template}    ${R2_interface_data}

TEST to Verify VLAN transperancy
    [Documentation]    TEST to Verify VLAN transperancy
    [Tags]    Spirent VLAN Transperancy Traffic Testing For EVPN Service
    ${Spirent_Test_Result}=    Spirent VLAN Transperancy Traffic Testing For EVPN Service
    Log To Console    ${Spirent_Test_Result}
    should be equal    ${Spirent_Test_Result}    Spirent Test Result Passed

TEST to Verify MAC transperancy
    [Documentation]    TEST to Verify MAC transperancy
    [Tags]    Spirent MAC Transperancy Traffic Testing For EVPN Service
    ${Spirent_Test_Result}=    Spirent MAC Transperancy Traffic Testing For EVPN Service
    Log To Console    ${Spirent_Test_Result}
    should be equal    ${Spirent_Test_Result}    Spirent Test Result Passed

Test Addition of Site to Exiting EVPN service
    [Documentation]    Test Addition of Site Exiting EVPN service
    [Tags]    Addition-Of-Site-To-Existing-EVPN
    CONFIGURE INTERFACE    ${R3_net_connect}    ${MAIN_INTERFACE_R3}    ${interface_template}    ${R3_interface_data}
    CONFIGURE SUB-INTERFACE    ${R3_net_connect}    ${SUB_INTERFACE_R3}    ${sub_interface_template}    ${R3_sub_interface_data}
    CONFIGURE l2vpn    ${R3_net_connect}    ${MAIN_INTERFACE_R3}    ${SUB_INTERFACE_R3}    ${l2vpn_template}    ${R3_l2vpn_data}
    CONFIGURE evpn    ${R3_net_connect}    ${evpn_template}    ${R3_evpn_data}
    ${show_result}=    SHOW COMMAND    ${R3_net_connect}    show_l2vpn_BD_template    ${R3_l2vpn_data}
    log to console    ${show_result}
    should be equal    ${show_result}    ${EPN_Result}

Addition of First Accedian Site To Exisiting EVPN Service
    [Documentation]    Addition of Accedian Site To Exisiting EVPN Service
    [Tags]    Addition-of-Accedian-Site-To-Exisiting-EVPN-Service
    ADD VIDSET TO ACCEDIAN    ${Accedian1_net_connect}    ${config_vid_set}    ${Accedian1_vid_set_data}    ${NNI_INTERFACE_ACCEDIAN1}
    CONFIGURE ACCEDIAN REGULATOR    ${Accedian1_net_connect}    ${config_NNI_BW_Regulator}    ${Accedian_NNI_BW_Regulator}
    CONFIGURE ACCEDIAN POLICY    ${Accedian1_net_connect}    ${config_NNI_Policy}    ${Accedian1_NNI_Policy_set_data}    ${NNI_INTERFACE_ACCEDIAN1}    ${UNI_INTERFACE_ACCEDIAN1}
    CONFIGURE ACCEDIAN EPN-CFM    ${Accedian1_net_connect}    ${config_Single_Tagged_CFM}    ${Accedian1_CFM_set_data}    ${Accedian1_vid_set_data}
    CONFIGURE ACCEDIAN EPN-SingleTagged-MEP    ${Accedian1_net_connect}    ${config_Single_Tagged_CFM_MEP}    ${Accedian1_CFM_set_data}    ${Accedian1_vid_set_data}    ${NNI_INTERFACE_ACCEDIAN1}
    ${Accedian1_NNI_Port_MAC_Address}=    SHOW COMMAND    ${Accedian1_net_connect}    extract_Accedian_Port_MAC_address    ${ACCEDIAN1_INTERFACES}
    ${Accedian_NNI_Port_MAC_Value}    get from dictionary    ${Accedian1_NNI_Port_MAC_Address}    MAC_Address
    ${Accedian1_NNI_Port_MAC_Value}=    Convert MAC Address From Accedian TO Cisco Format    ${Accedian_NNI_Port_MAC_Value}
    ${MAC_Address}=    Create Dictionary    Accedian_NNI_Port_MAC_In_Cisco_Format=${Accedian1_NNI_Port_MAC_Value}
    ${MAC_Address_Dict_Cisco_BD}=    SHOW COMMAND    ${R3_net_connect}    show_evpn_evi_mac_filter_with_specific_mac    ${MAC_Address}
    ${MAC_Address_Lerned_in_Cisco_BD}    get from dictionary    ${MAC_Address_Dict_Cisco_BD}    MAC_Address
    log to console    Great Result
    log to console    ${MAC_Address_Lerned_in_Cisco_BD}
    log to console    ${Accedian1_NNI_Port_MAC_Value}
    should be equal    ${Accedian1_NNI_Port_MAC_Value}    ${MAC_Address_Lerned_in_Cisco_BD}

Addition of Second Accedian Site To Exisiting EVPN Service
    [Documentation]    Addition of Accedian Site To Exisiting EVPN Service
    [Tags]    Addition-of-Accedian-Site-To-Exisiting-EVPN-Service
    ADD VIDSET TO ACCEDIAN    ${Accedian2_net_connect}    ${config_vid_set}    ${Accedian2_vid_set_data}    ${NNI_INTERFACE_ACCEDIAN2}
    CONFIGURE ACCEDIAN REGULATOR    ${Accedian2_net_connect}    ${config_NNI_BW_Regulator}    ${Accedian_NNI_BW_Regulator}
    CONFIGURE ACCEDIAN POLICY    ${Accedian2_net_connect}    ${config_NNI_Policy}    ${Accedian2_NNI_Policy_set_data}    ${NNI_INTERFACE_ACCEDIAN2}    ${UNI_INTERFACE_ACCEDIAN2}
    CONFIGURE ACCEDIAN EPN-CFM    ${Accedian2_net_connect}    ${config_Single_Tagged_CFM}    ${Accedian2_CFM_set_data}    ${Accedian2_vid_set_data}
    CONFIGURE ACCEDIAN EPN-SingleTagged-MEP    ${Accedian2_net_connect}    ${config_Single_Tagged_CFM_MEP}    ${Accedian2_CFM_set_data}    ${Accedian2_vid_set_data}    ${NNI_INTERFACE_ACCEDIAN2}
    ${Accedian2_NNI_Port_MAC_Address}=    SHOW COMMAND    ${Accedian2_net_connect}    extract_Accedian_Port_MAC_address    ${ACCEDIAN2_INTERFACES}
    ${Accedian_NNI_Port_MAC_Value}    get from dictionary    ${Accedian2_NNI_Port_MAC_Address}    MAC_Address
    ${Accedian2_NNI_Port_MAC_Value}=    Convert MAC Address From Accedian TO Cisco Format    ${Accedian_NNI_Port_MAC_Value}
    ${MAC_Address}=    Create Dictionary    Accedian_NNI_Port_MAC_In_Cisco_Format=${Accedian2_NNI_Port_MAC_Value}
    ${MAC_Address_Dict_Cisco_BD}=    SHOW COMMAND    ${R1_net_connect}    show_evpn_evi_mac_filter_with_specific_mac    ${MAC_Address}
    ${MAC_Address_Lerned_in_Cisco_BD}    get from dictionary    ${MAC_Address_Dict_Cisco_BD}    MAC_Address
    log to console    Great Result
    log to console    ${MAC_Address_Lerned_in_Cisco_BD}
    log to console    ${Accedian2_NNI_Port_MAC_Value}
    should be equal    ${Accedian2_NNI_Port_MAC_Value}    ${MAC_Address_Lerned_in_Cisco_BD}

Validation of CFM status For EVPN Accedian Site
    ${CFM_Status}=    SHOW COMMAND    ${Accedian1_net_connect}    show_accedian_cfm_status    ${Accedian1_CFM_set_data}
    log to console    ${CFM_Status}
    should be equal    ${CFM_Status}    ${Accedian_CFM_Result}
    ${CFM_Status}=    SHOW COMMAND    ${Accedian2_net_connect}    show_accedian_cfm_status    ${Accedian2_CFM_set_data}
    log to console    ${CFM_Status}
    should be equal    ${CFM_Status}    ${Accedian_CFM_Result}

*** Keywords ***
