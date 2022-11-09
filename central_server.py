import socket
import sys
import select
import queue
import pickle
import ip_database
import Crypto
from Crypto.Cipher import AES,DES3
from Crypto import Random
from Crypto.Hash import SHA256 as sha256
from Crypto.PublicKey import RSA as rsa

class central_socket:
    def __init__(self):
        self.data = ip_database.ip_data()
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.setblocking(0)
        self.address  = ('localhost',9999)
        print("Starting up")
        self.inputs,self.output = [self.server],[]
        self.data_q = {}
        self.to_read,self.to_write,self.to_rectify = [],[],[]

    def listen_(self):
        self.server.bind(self.address)
        self.server.listen(4)

        def helper3(self):
        data_recv = s.recv(1024)
        if data_recv:
            if s not in self.output:
                self.output.append(s)
            if pickle.loads(data_recv)[:12] == 'finger_table':
                s.send(pickle.dumps('finger_table'))
            else:
                got = text()
                got.process()
                
        else:
            print("Removing")
            if s in self.output:
                self.output.remove(s)
            self.inputs.remove(s)
            s.close()
            del self.data_q[s]

    def helper1(self):
        for s in self.to_read:
            if s is self.server:
                print("New Connection ")
                client , client_addr = s.accept()
                client.setblocking(0)
                self.inputs.append(client)
                self.data_q[client] = queue.Queue()
            else:
                this.helper3()
    
    def helper2(self):
        for s in self.to_write:
            try:
                next_msg = self.data_q[s].get_nowait()
            except queue.Empty:
                self.output.remove(s)
            else:
                s.send(next_msg)
        
        for s in self.to_rectify:
                inputs.remove(s)
                if s in outputs:
                    self.outputs.remove(s)
                s.close()
                del self.data_q[s]

    def connect_(self):
        while self.inputs:
            print("Waiting .....")
            self.to_read,self.to_write,self.to_rectify = select.select(self.inputs,self.output,self.inputs)
            #print(self.to_read,"\n",self.to_write)
            self.helper1()
            self.helper2()
                    
centre = central_server.central_socket()
centre.listen_()
centre.connect_()


