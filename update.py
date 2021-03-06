from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.149.141',
    'username': 'naval',
    'password': 'cisco',
}
iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.149.142',
    'username': 'naval',
    'password': 'cisco',
}
iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.149.143',
    'username': 'naval',
    'password': 'cisco',
}
iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.149.144',
    'username': 'naval',
    'password': 'cisco',
}
iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.149.145',
    'username': 'naval',
    'password': 'cisco',
}


cfg_file = "iosv_access"

all_devices = [iosv_l2_s3, iosv_l2_s4, iosv_l2_s5]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_from_file(cfg_file)
    print(output)

with open('iosv_core') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l2_s1, iosv_l2_s2]

output = net_connect.send_command("show ip interface brief")
print (output)

f.closed
