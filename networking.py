import socket

class Networking(object):

    def __init___(self,addr):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = addr
    def connect(self):
        self.socket.connect(self.addr)
    def recv(self,size):
        self.data = self.socket.recv(size)
    def __repr__(self):
        pass
        
