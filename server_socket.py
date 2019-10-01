import socket
import sys
import select
import queue
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(0)

server_addr = ('localhost',8100)
server.bind(server_addr)
server.listen(5)

inputs = [server]
outputs = []
message_q = {}

while input:
    readable , writable ,exceptional = select.select(inputs,outputs,inputs)
    for s in readable:
        if s is server:
            connection,client_addr = s.accept()
            connection.setblocking(0)
            inputs.append(connection)
            message_q[connection] =  queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                message_q[s].put(data)
                if s not in outputs:
                    outputs.append(s)
            else:
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                del message_q[s]
    for s in writable:
        try:
            next_msg = message_q[s].get_nowait()
        except queue.Empty:
            outputs.remove(s)
        else:
            s.send(next_msg)
        for s in exceptional:
            inputs.remove(s)
            if s in outputs:
                outputs.remove(s)
            s.close()
            del message_q[s]
            
