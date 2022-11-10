import pickle
import socket

class text:
    
    def encrypt(self,public_key):
        self.encoded_message = pickle.loads(public_key.encrypt(pickle.dumps(message)))
        
    def decrypt(self,private_key):
        self.message = pickle.loads(private_key.decrypt(pickle.dumps()))
        
    def clear_text(self):
        self.message = ''
    
    
        