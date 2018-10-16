import socket,Queue,threading
class Data(object):
    
    def __init__(self,param):
        #TODO: implement Data fields and functions according to the protocall
        pass
    def __repr__(self):
        pass
    
class Networking(object):

    def __init___(self,addr):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = addr
        self.data_queue = Queue()

    def connect(self):
        self.socket.connect(self.addr)
    def recv(self,size):
        self.data = self.socket.recv(size)

        
