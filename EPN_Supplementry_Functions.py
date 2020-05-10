# -*- coding: utf-8 -*-
from typing import TextIO
from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2 import Environment
import os
#import templates as t1
file_path = os.path.dirname(os.path.realpath(__file__))
def Config_EPN (EPN_Topology) :
    EPN_Nodes = EPN_Topology['Topology Info']
    No_EPN_Nodes = EPN_Nodes['EPN_Nodes']
    print(No_EPN_Nodes)
    Device_Details = EPN_Topology['Device Details']
    EPN_Site_Template = Template('EPN-Site-Template')
    i=1
    a = EPN_Site_Template.render(component=Device_Details['R' + str(1)])
    #for i in range(No_EPN_Nodes):
     #   a[i] = EPN_Site_Template.render(component=Device_Details['R'+str(i+1)])
      #  print(a[i])
    print(a)
    return(1)

