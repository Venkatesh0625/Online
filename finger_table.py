import socket
import struct 

def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]

def int2ip(addr):
    return socket.inet_ntoa(struct.pack("!I", addr))
       
class node:
    def __init__(self,ip):
        self.ip=ip
        self.left=None
        self.right=None

class table:
    def __init__(self):
        self.root=None
        self.height=0
        self.flag=0
    
    def insert_node(self, root, ip):
        if(root==None):
            return(node(ip))
        if(ip2int(root.ip)>ip2int(ip)):
            root.left=self.insert_node(root.left, ip)
        else:
            root.right=self.insert_node(root.right, ip)
        return(root)
    def insert(self,ip):
        self.root = self.insert_node(self.root,ip)
        self.root = self.splay(self.root,ip)
    
    
    def zig(self, root):
        x=root.left
        root.left=x.right
        x.right=root
        return(x)
    
    def zag(self,root):
        x=root.right
        root.right=x.left
        x.left=root
        return(x)
    
    def zigzig(self, root):
        return(self.zig(self.zig(root)))
    
    def zagzag(self, root):
        return(self.zag(self.zag(root)))
    
    def zigzag(self, root):
        root.left=self.zag(root.left)
        return(self.zig(root))
    
    def zagzig(self, root):
        root.right=self.zig(root.right)
        return(self.zag(root))
    
    def splay(self, root, data):
        if(root!=None):
            self.height+=1
            r=ip2int(root.ip)
            d=ip2int(data)
            if(d!=r):
                if(d<r):
                    root.left=self.splay(root.left, data)
                else:
                    root.right=self.splay(root.right, data)
                self.flag+=1
                self.height-=1
            else:
                self.height-=1
                return(root)
            if(self.flag==2):
                if(d<r):
                    c1=ip2int(root.left.ip)
                    if(d<c1):
                        root=self.zigzig(root)
                    else:
                        root=self.zigzag(root)
                else:
                    c2=ip2int(root.right.ip)
                    if(d>c2):
                        root=self.zagzag(root)
                    else:
                        root=self.zagzig(root)
                self.flag=0
            elif(self.height==0):
                if(d<r):
                    root=self.zig(root)
                else:
                    root=self.zag(root)
                self.flag=0
        return(root)
    def search(self, root, data, pred):
        if(root!=None):
            d=ip2int(data)
            r=ip2int(root.ip)
            if(d < r):
                if(root.left!=None):
                    return(self.search(root.left, data, pred))
                else:
                    return(pred.ip)
            elif(d > r):
                if(root.right!=None):
                    return(self.search(root.right, data, root))
                else:
                    return(root.ip)
            else:
                return(root.ip)
    def getmin(self, root):
        if(root!=None and root.left!=None):
            return(self.getmin(root.left))
        else:
            return root.ip            
    def getmax(self, root):
        if(root!=None and root.right!=None):
            return(self.getmax(root.right))
        else:
            return root.ip
    def find_path(self, ip):
        min_node=self.getmin(self.root)
        min_data=ip2int(min_node)
        ipdata=ip2int(ip)
        if(min_data<ipdata):
            parent=self.search(self.root, ip, self.root)
            self.root=t.splay(self.root, parent)
        else:
            max_node=self.getmax(self.root)
            self.root=self.splay(self.root, max_node)
        
    def inorder_(self, root):
        if(root!=None):
            print(root.ip)
            self.inorder_(root.left)
            self.inorder_(root.right)
    def inorder(self):
        self.inorder_(self.root)
        
    def clear(self):
        self.root = None
            
t=table()
ip = ["6","7","9","1"]
for i in ip:
    t.insert(i)
t.inorder()
ip="123.34.45.65"
t.find_path(ip)
print(t.root.ip)