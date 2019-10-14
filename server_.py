import socket
import sys
import select
import queue
import pickle
import ip_database
class central_socket:
    def __init__(self):
        self.data = ip_database.ip_data()
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.setblocking(0)
        self.address  = ('localhost',int(input("Entr port : ")))
        print("Starting up")
        self.inputs,self.output = [self.server],[]
        self.data_q = {}
        self.to_read,self.to_write,self.to_rectify = [],[],[]

    def listen_(self):
        self.server.bind(self.address)
        self.server.listen(4)
        
    def add_queue(self,client,msg):
        if client not in self.output:
            self.output.append(client)
        try:
            self.data_q[client]
        except:
            self.data_q[client] = queue.Queue()
        self.data_q[client].put(msg)
        

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
                    data_recv = s.recv(1024)
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
                    s.send(pickle.dumps(next_msg))
            
            for s in self.to_rectify:
                    inputs.remove(s)
                    if s in self.outputs:
                        self.outputs.remove(s)
                    s.close()
                    del self.data_q[s]


