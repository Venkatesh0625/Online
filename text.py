import pickle
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
class text:
    def __init__(self):
        self.sender_ip = '127.0.0.1'
        self.receiver_ip = '127.0.0.1'
        self.encoded_msg = ''
        self.message = ''
    
        