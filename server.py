import socket
import sys
import select
import queue
import pickle
import ip_database
class server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.setblocking(0)
        self.address  = ('localhost',8889)
        print("Starting up")
        self.inputs,self.output = [self.server],[]
        self.data_q = {}
        self.to_read,self.to_write,self.to_rectify = [],[],[]

    def listen_(self):
        self.server.bind(self.address)
        self.server.listen(1000)

    def add_queue(self,socket,msg):
        try:
            self.data_q[socket]
        except:
            self.data_q[socket] = queue.Queue()
        self.data_q[socket].put(msg)
        if socket not in self.output:
            self.to_write.append(socket)
        
    def connect_(self):
        while self.inputs:
            print("Waiting .....")
            self.to_read,self.to_write,self.to_rectify = select.select(self.inputs,self.output,self.inputs)
            print(self.to_read,"\n",self.to_write)
            for s in self.to_read:
                if s is self.server:
                    print("New Connection ")
                    client , client_addr = s.accept()
                    client.setblocking(0)
                    self.inputs.append(client)
                    self.data_q[client] = queue.Queue()
                else:
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


