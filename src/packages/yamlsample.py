##  File: yamlsample.py
#
#

import yaml

conf_list=[]
yamlfiles=["set1.yaml","set2.yaml","set3.yaml","set4.yaml","set5.yaml","set6.yaml"]

for filename in yamlfiles:
	with open(filename) as yamldat:
		conf = yaml.safe_load(yamldat)
		conf_list.append(conf)

for conf in conf_list:
	print(type(conf),conf)
