#!/usr/bin/env python
import socket
import struct
import threading

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
TIMEOUT = 0.500     # set the timeout to 500ms
BACKLOG_LIMIT = 4
BUFFER_SIZE = 20

THREAD_ID = 1

class ServerThread(threading.Thread):

    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        global THREAD_ID
        self.id = THREAD_ID
        self.conn = conn
        self.client_ip = addr
        THREAD_ID = THREAD_ID + 1

    # Handle comms b/t a client and the server
    def run(self):
        data = self.conn.recv(BUFFER_SIZE)
        if not data:
            self.report('error receiving data from client, closing thread')
            return
        self.report('received data:{}'.format(data))
        self.conn.send(data)

    def get_id(self):
        return self.id

    def get_name(self):
        return 'Thread-{}'.format(self.id)

    def to_string(self):
        return '{}, hosting:{}'.format(self.get_name(), self.client_ip)

    def report(self, msg):
        print('{}::\n\t{}'.format(self.to_string(), msg))

def init_server():

    print('Running server on IP={}:{}\n'.format(TCP_IP, TCP_PORT))

    # set up the TCP socket
    sock = socket.socket()
    sock.bind((TCP_IP, TCP_PORT))

    # listen for client connections
    sock.listen(BACKLOG_LIMIT)

    while sock:
        # accept connection from a client
        conn, addr = sock.accept()
        conn.settimeout(TIMEOUT)
        print('Connection from host on IP={}'.format(addr))

        # create a thread to handle comms w/ client host
        thd = ServerThread(conn, addr)
        print('Server Thread {} created'.format(thd.get_name()))
        thd.start()

    sock.close()
    print('\nListening socket is \'None\', server shutting down!\n')

# run the server
init_server()
