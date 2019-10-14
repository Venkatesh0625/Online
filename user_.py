import socket    
import pickle
from server import *
from client import *
from text import *
import os
from Crypto.Cipher import AES,DES3
from Crypto import Random
from Crypto.Hash import SHA256 as sha256
from Crypto.PublicKey import RSA as rsa

class user:
    def __init__(self):
        self.server = server()
        self.server.listen_()
        self.client = client()
        self.friends = []
        self.private_key = rsa.generate(1024)
        self.public_key = self.private_key.publickey()
        self.to_msg = None
        self.from_msg = None
        
    def send_message(self,ip_addr,message):
        self.to_msg = text()
        self.to_msg.message = message
        self.to_msg.encrypt()
        self.to_msg.clear_text()
        temp_client = find_next_path()
        self.server.add_queue(temp_client,self.to_msg)
        self.to_msg = None
        
    def handle_msg(self):
        for i in self.server.inputs:
            self.from_msg = pickle.loads(self.server.inputs[i])
            
            temp_client = find_next_path()
            self.server.add_queue(temp_client,self.to_msg)
            self.to_msg = None
            
            
        
        
        
        
u = user()
        
        
        
        
        