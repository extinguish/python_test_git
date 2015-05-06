# !/usr/bin/env python

import socket

def print_machine_info():
	host_name = socket.gethostname();
	ip_address = socket.gethostbyname(host_name);
	print "Host name are : %s " %host_name
	print "Host ip address are : %s " %ip_address

	# if __name__ == '__main__':
	# 	print_machine_info()

print_machine_info()

def get_remote_machine_info():
	remote_host_name = "www.baidu.com"
	try:
		print " this host name ip address are : %s --> %s " %(remote_host_name, socket.gethostbyname(remote_host_name))
	except socket.error, e:
		print " exception happend while getting the remote address : %s" %(remote_host_name, e)


get_remote_machine_info()