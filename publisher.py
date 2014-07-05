import os, socket, fcntl, struct, sys
import pyperclip
from subprocess import call

import properties as p

# argv
# argv[1] - base dir
# argv[2] - filename

def get_interface_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                ifname[:15]))[20:24])

# target link
link = p.protocol + '://'
if p.get_ip_from is 'properties':
	link += p.ip
elif p.get_ip_from is 'system':
	link += get_interface_ip(p.interface)

if p.enable_port:
	link += ':' + str(p.port)

link += '/public/'

link += sys.argv[3]

if len(sys.argv) is 4:
	if sys.argv[1] == 'copy':
		call(["cp", sys.argv[2] + '/' + sys.argv[3], p.public_dir])
	elif sys.argv[1] == 'move':
		call(["mv", sys.argv[2] + '/' + sys.argv[3], p.public_dir])
else:
	exit()

# sudo apt-get install xclip
pyperclip.setcb(link)