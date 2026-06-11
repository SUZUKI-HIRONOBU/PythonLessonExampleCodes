##  File: netconf.py
#
import yaml

with open("netconf.yaml") as f:
	conf = yaml.safe_load(f)

print(conf)

print(conf['Server']['AllowIP'])
print(conf['Server']['Port'])

print(conf['Client']['ServerIP'])
print(conf['Client']['ServerPort'])

## サーバーのコンフィグレーション
serverconf = conf['Server']
print(serverconf['AllowIP'])
print(serverconf['Port'])

#クライアントのコンフィグレーション
clientconf = conf['Client']
print(clientconf['ServerIP'])
print(clientconf['ServerPort'])
