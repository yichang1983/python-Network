#!/usr/bin/env python3

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
      "cmd": "interface e2/2",      #put command you want
      "version": 1.2
    },
    "id": 1
  },
  {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "description this-is-test",      #put command you want
            "version": 1.2
        },
        "id": 2                 #this is 2nd command
  },
  {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "end",       #put command you want
            "version": 1.2
        },
        "id": 3                 #this is 3rd command
  },
  {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "copy run start",        #put command you want
            "version": 1.2
        },
        "id": 4                #this is 4th command
  },



]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
print(response)