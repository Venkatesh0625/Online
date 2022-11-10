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

        

    def connect_(self):
        while self.inputs:
            print("Waiting .....")
            self.to_read,self.to_write,self.to_rectify = select.select(self.inputs,self.output,self.inputs)
                    
centre = central_server.central_socket()
centre.listen_()
centre.connect_()


