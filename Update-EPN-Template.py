# -*- coding: utf-8 -*-
from typing import TextIO
from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2 import Environment
from EPN_Supplementry_Functions import Config_EPN
#from yaml import load, FullLoader
import json
templateFilePath = FileSystemLoader('D:\Kishor\Automation\\template')
jinjaEnv = Environment(loader=templateFilePath)
jTemplate = jinjaEnv.get_template('EVPN-Bridge-config.txt')
actual_config: TextIO
#with open("EPN-config.yml") as actual_config:
  #actual_config = yaml.load(actual_config, Loader=FullLoader)
#app_json = dumps(actual_config)
#print(app_json)
with open("device.json") as data_file:
    data_config = json.load(data_file)
print(data_config)
flag = Config_EPN(data_config)
print(flag)
#Device_Details = data_config['Device Details']
#for i in range (2) :
#   print(Device_Details['R'+ str(i+1)])
#R2_device = Device_Details['R2']
#R2_Bridge = R2_device['Bridge']
#print(R2_Bridge)
#for key in actual_config:
#            print(key, actual_config[key])
#output = jTemplate.render(ansible_mounts=app_json)
#output_File_Handler = open ('D:\Kishor\Automation\EPN\output.json', 'w')
#output_File_Handler.write(app_json)
#output_File_Handler.close()

