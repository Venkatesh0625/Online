import socket
import sys
import pickle
import os

class client:
    def __init__(self):
        self.address = ()
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
    def connect_(self,ip_addr,port):
        self.address = (ip_addr,port)
        self.sock.connect(self.address)
        
    def get_addr(self):
        return self.address
    
    def send_(self,string):
        self.sock.send(pickle.dumps(string))
        
    def send_key(self,key):
        self.sock.send(key.exportKey(format = 'PEM',passphrase = None,pkcs = 1))
    
    def close_(self):
        self.sock.close()
    