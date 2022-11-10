import socket    
import pickle
from server import Server
from client import Client
from text import text
from finger_table import node, table
import os
from Crypto.Cipher import AES,DES3
from Crypto import Random
from Crypto.Hash import SHA256 as sha256
from Crypto.PublicKey import RSA as rsa

class user:
    def __init__(self):
        self.server = server()
        self.finger_table = table()
        self.server.listen_()
        self.local_ip = socket.gethostbyname(socket.gethostname())
        self.client = client()
        self.friends = []
        self.private_key = rsa.generate(2048)
        self.public_key = self.private_key.publickey()
        self.to_msg = None
        self.from_msg = None
        self.messages = {}
        
    def send_message(self,message):
        self.to_msg = text()
        self.to_msg.message = message
        self.to_msg.encrypt()
        self.to_msg.clear_text()
        temp_client = find_path()
        self.server.add_queue(temp_client,self.to_msg)
        self.to_msg = None
        
    def handle_msg(self):
        for i in self.server.inputs:
            self.from_msg = pickle.loads(self.server.inputs[i])
            if isinstance(self.from_msg,list):
                self.update_table(self.from_msg)
            elif self.from_msg.destination_ip == self.local_ip:
                self.from_msg.decrypt()
                try:
                    self.messages[self.from_msg.sender_ip].append(self.from_msg.message)
                except ValueError:
                    self.messages[self.from_msg.sender_ip] = [self.from_msg.message]
            else:
                temp_client = find_next_path()
                self.server.add_queue(temp_client,self.from_msg)
            self.from_msg = None
            
    def update_table(self,table):
        self.finger_table.clear()
        for i in table:
            finger_table.insert(i)
        
        
            
u = user()
        
        
        
        
        