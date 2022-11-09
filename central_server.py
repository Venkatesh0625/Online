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
            #print(self.to_read,"\n",self.to_write)
            for s in self.to_read:
                if s is self.server:
                    print("New Connection ")
                    client , client_addr = s.accept()
                    client.setblocking(0)
                    self.inputs.append(client)
                    self.data_q[client] = queue.Queue()
                else:
                    data_recv = s.recv(4096)
                    if data_recv:
                        if s not in self.output:
                            self.output.append(s)
                        #Checking whether the data is a private key class 
                        #Storing ip_address of the node by getting the 
                        try:
                            got = rsa.importKey(data_recv,passphrase = None)
                            if isinstance(got,Crypto.PublicKey.RSA._RSAobj):
                                self.data.add_ip(s.getpeername(),got) 
                        #Will get an error if it is not a Crypto.publickey object 
                        except ValueError:
                            got = pickle.loads(data_recv)
    
                            if got[:12] =='predecessor$':
                                self.data_q[s].put(pickle.dumps(self.data.get_predecessor(got[13:])))
                                
                            elif got[:11] == 'public_key$':
                                self.data_q[s].put(self.data.get_private_key(got[11:]).exportKey(format = 'PEM',passphrase = None,pkcs = 1))
                            
                            elif got[:7] == 'delete$':
                                self.data.delte(got[7:])
                                self.data_q[s].put(pickle.dumps('removed'))
                    
                        if s in self.output:
                            self.output.remove(s)
                        self.inputs.remove(s)
                        s.close()
                        del self.data_q[s]
                    
            
            for s in self.to_write:
                try:
                    next_msg = self.data_q[s].get_nowait()
                    print(next_msg)
                except queue.Empty:
                    self.output.remove(s)
                else:
                    s.send(next_msg)
            
            for s in self.to_rectify:
                    inputs.remove(s)
                    if s in self.outputs:
                        self.outputs.remove(s)
                    s.close()
                    del self.data_q[s]
                    
                    
                    
centre = central_server.central_socket()
centre.listen_()
centre.connect_()


