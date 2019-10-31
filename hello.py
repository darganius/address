# username
# os name
# user ip add
# router ip address  (default gateway)



import os
import subprocess
username = (subprocess.check_output(['whoami'])).decode('utf-8')
a = (subprocess.check_output(['uname'])).decode('utf-8')
print("Username: {}".format(username))
print("OS name: {}".format(a))
if a == 'Linux' or 'Unix':
    userip = (subprocess.check_output(['ifconfig'])).decode('utf-8')
    splitip = userip.split('\n')
    a = splitip[17]
    b = a.split(' ')
    c = b[9]
    ip = (subprocess.check_output(['ip','route'])).decode('utf-8')
    ip = ip.split(' ')
    ipsplit = ip[2]
    print('User IP address: {}'.format(c))
    print('Router ip address: {}'.format(ipsplit))
elif a == 'Mac':
    userip = (subprocess.check_output(['ifconfig'])).decode('utf-8')
    ip = (subprocess.check_output(['netstat','-nr'])).decode('utf-8')
    print('User IP address: {}'.format(userip))
    print('router ip address: {}'.format(ip))
elif a == 'Windows':
    userip = (subprocess.check_output(['ipconfig'])).decode('utf-8')
    print('User IP address: {}'.format(userip))
    print('Router ip address: {}'.format(ip))
