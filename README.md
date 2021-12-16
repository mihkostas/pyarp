# pyarp
pyarp is an arp spoofing tool made in python with the ```scapy``` library, <br/> 
first make the files executable:
	
	chmod 755 pyarp*
usage:  

	./pyarp.sh <target_ip_1> <target_ip_2>
stop program:

	./pyarp.sh -s
must run as root.<br/>
if you dont have scapy, install with:

	pip3 install scapy
