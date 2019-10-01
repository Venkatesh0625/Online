import socke
import sys
import pickle
messages = ['This is the message','It will be sent','in parts']
server_addr = ('localhost',8100)
socks = [socket.socket(socket.AF_INET,socket.SOCK_STREAM),
         socket.socket(socket.AF_INET,socket.SOCK_STREAM)]
for s in socks:
    s.connect(server_addr)
for message in messages:
    for s in socks:
        s.send(pickle.dumps(message))
    for s in socks:
        data = s.recv(1024)
        print(s.getpeername(),pickle.loads(data))
        if not data:
            s.close()
    
