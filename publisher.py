# -*- coding: utf-8 -*-
import os, socket, fcntl, struct, sys, subprocess
from subprocess import call
import pyperclip

import properties as p

# argv[1] - 'copy' or 'move'
# argv[2] - base dir
# argv[3] - filename

title = 'Ссылка скопирована в буфер обмена'

def sendmessage(message):
    subprocess.Popen(['notify-send', title, message])
    return

def get_interface_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                ifname[:15]))[20:24])

link = p.protocol + '://'
if p.get_ip_from is 'properties':
	link += p.ip
elif p.get_ip_from is 'system':
	link += get_interface_ip(p.interface)

if p.enable_port:
	link += ':' + str(p.port)

link += '/public/' + sys.argv[3]

if len(sys.argv) is 4:
	if sys.argv[1] == 'copy':
		call(["cp", sys.argv[2] + '/' + sys.argv[3], p.public_dir])
	elif sys.argv[1] == 'move':
		call(["mv", sys.argv[2] + '/' + sys.argv[3], p.public_dir])
else:
	exit()

pyperclip.setcb(link.replace(' ', '%20'))

if p.notify:
	sendmessage(link)