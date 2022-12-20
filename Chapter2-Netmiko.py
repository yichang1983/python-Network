from netmiko import ConnectHandler

iosv_1 = {'device_type':'cisco_ios','host':'192.168.17.20','username':'root','password':'root'}
net_connect = ConnectHandler(**iosv_1)
net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')
print(output)


net_connect_2 = ConnectHandler(device_type='cisco_ios', host='192.168.17.21', username='root', password='root')
cfg_list = [
    "ip access-list extended TEST1",
    "permit ip any host 1.1.1.1",
    "permit ip any host 1.1.1.2",
    "permit ip any host 1.1.1.3",
    "permit ip any host 1.1.1.4",
    "permit ip any host 1.1.1.5",
]
cfg_output = net_connect_2.send_config_set(cfg_list)
print(cfg_output)




