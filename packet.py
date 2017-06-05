#!/usr/bin/env python
import struct
from operators import *

DCP_FORMAT = '>cdd'

class Packet(object):

    def __init__(self, fmt, *data):
        self.fmt = fmt
        self.data = data

    def pack(self):
        return struct.pack(self.fmt, *self.data)

class DCPacket(Packet):

    def __init__(self, operator, *operands):
        super(DCPacket, self).__init__(DCP_FORMAT, operator, *operands)
        self.operator = operator
        if operator == ADD or operator == SUB   \
           or operator == MUL or operator == DIV:
            self.operand1 = operands[0]
            self.operand2 = operands[1]

    def get_operator(self):
        return self.operator

    def get_operands(self):
        if self.operator == ADD or self.operator == SUB   \
           or self.operator == MUL or self.operator == DIV:
            return (self.operand1, self.operand2)
        return None

    @staticmethod
    def unpack(byte_string):
        print(byte_string)
        data = struct.unpack(DCP_FORMAT, byte_string)
        if data[0] == ADD or data[0] == SUB   \
           or data[0] == MUL or data[0] == DIV:
            return DCPacket(data[0], data[1], data[2])
        return None
