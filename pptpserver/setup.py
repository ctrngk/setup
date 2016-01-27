# This script is to set up pptp server in new debian/ubuntu
# usage:
# login as root
# python3 setup.py

import os
import time

a = os.system("echo starting to build pptp server...")
time.sleep(0.5)
name = input("input your vpn user name:")
passwd = input("input your vpn user passwd:")
cmd3_1 = name + "	pptpd	" + passwd + "	\*"
#cmd3_2 = "	* "
cmd3 = "echo " + cmd3_1 + " >> /etc/ppp/chap-secrets"
time.sleep(0.5)
os.system("echo starting to install pptpd...")
os.system('apt-get install pptpd -y')
time.sleep(10)
os.system("echo pptpd established...")
cmd = 'echo localip 10.0.0.1 >> /etc/pptpd.conf'
cmd2 = 'echo remoteip 10.0.0.100-200 >> /etc/pptpd.conf'
os.system(cmd)
os.system(cmd2)
os.system(cmd3)
os.system("echo ms-dns 8.8.8.8 >> /etc/ppp/pptpd-options")
os.system("echo ms-dns 8.8.4.4 >> /etc/ppp/pptpd-options")
os.system("echo net.ipv4.ip_forward = 1 >> /etc/sysctl.conf")
os.system("sysctl -p")
os.system("ipv4 forward take effect...")
time.sleep(2)
cmd_5 = "iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE && iptables-save"
os.system(cmd_5)
os.system("echo iptables established")
time.sleep(0.5)
os.system("echo pptpd server is OK now")
