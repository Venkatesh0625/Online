from Crypto.Cipher import AES,DES3
from Crypto import Random
from Crypto.Hash import SHA256 as sha256
from Crypto.PublicKey import RSA as rsa

class ip_data:
    def __init__(self):
        self.data = []
        
    def delte(self,ip_addr):
        for i in self.data:
            if i[0] == ip_addr:
                self.data.remove(i)
             
    def add_ip(self,ip_addr,key):
        flag = bool(1)
        for i in self.data:
            if i[0] == ip_addr:
                flag = bool(0)
        if flag:
            self.data.append((ip_addr,key))
            return 'added'
        else:
            return 'already_added'
        
    def get_predecessor(self,ip_addr):
        for i in range(self.data.len()):
            if self.data[i][0] == ip_addr:
                return str(self.data[i-1][0])
        return 0
    
    def get_private_key(self,ip_addr):
        for i in self.data:
            if i[0] == ip_addr:
                #returning the public key
                return str(i[1].exportKey(format = 'PEM',passphrase = None,pkcs = 1))
        return 'ip doesn\'t exists'
    def get_tree(self,ip_addr):
        n = len(self.data)
        idx = 0 
        for i in range(len(self.data)):
            if self.data[0] == ip_addr:
                #getting the index of the given ip in the ip data
                idx = i
                break
        #Making the index of 2**n order 
        arr = [self.data[(idx + 2**i)%n][0] for i in range(ceil(log(n,2)))]
        return arr
                
            
        
                
        
                
        