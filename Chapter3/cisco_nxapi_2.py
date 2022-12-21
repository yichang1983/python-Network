# # !/usr/bin/env python3
#
# import requests
# import json
#
# url='http://192.168.17.22/ins'
# switchuser='test'
# switchpassword='Love2Eat'
#
# myheaders={'content-type':'application/json-rpc'}
# payload=[
#   {
#     "jsonrpc": "2.0",
#     "method": "cli",
#     "params": {
#       "cmd": "show version",
#       "version": 1.2
#     },
#     "id": 1
#   }
# ]
# response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
# print(response['result']['body']['sys_ver_str'])





# !/usr/bin/env python3

import requests
import json

url='http://192.168.17.22/ins'
switchuser='test'
switchpassword='Love2Eat'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show int description",
      "version": 1.2
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
print(response)