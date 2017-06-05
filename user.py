#!/usr/bin/env python

import socket
from operators import *
import packet

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

#Ethan adding stuff for user input
print ("Please enter an operation, operand1, and operand2")
op = input('Choose an operation')
opr1 = float(input('Choose first operand'))
opr2 = float(input('Choose second operand'))
print ("op: ",op," opr1: ",opr1," opr2: ",opr2)
if op == '+':
    op = ADD
elif op == '-':
    op = SUB
elif op == '*':
    op = MUL
elif op == '/':
    op = DIV
#End Ethan stuff
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

# Data Compute Packet
dcp = packet.DCPacket(op, opr1, opr2)
s.send(dcp.pack())
# End Data Compute Packet

s.close()
