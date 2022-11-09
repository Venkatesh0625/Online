import socket
import sys
import select
import queue
import pickle
import ip_database
# Rename field "server"
class ServerMain:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.setblocking(0)
        self.address  = ('localhost',8889)
        print("Starting up")
        self.inputs,self.output = [self.server],[]
        self.data_q = {}
        self.to_read,self.to_write,self.to_rectify = [],[],[]

    def listen_(self):
        self.server.bind(self.address)
        self.server.listen(1000)

    def add_queue(self,socket,msg):
        try:
            self.data_q[socket]
        except ValueError:
            self.data_q[socket] = queue.Queue()
        self.data_q[socket].put(msg)
        if socket not in self.output:
            self.to_write.append(socket)


    def connect_o(self):
        while self.inputs:
            self.to_read,self.to_write,self.to_rectify = select.select(self.inputs,self.output,self.inputs)
            
            


