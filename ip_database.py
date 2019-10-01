
class ip_data:
    def __init__(self):
        self.data = []
        
    def delte(self,ip_addr):
        if ip_addr in self.data:
            self.data.remove(ip_addr)
    
    def add_ip(self,ip_addr):
        if ip_addr not in self.data:
            self.data.append(ip_addr)
    
    def get_predecessor(self,ip_addr):
        if ip_addr in self.data:
            return self.data[self.data[self.data.index(ip_addr)] - 1]
    
    
        