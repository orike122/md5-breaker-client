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
        self.data_queue = Queue.Queue()
        self.listen = False
        self.recv_size = 1024
        self.listen_thread = threading.Thread(target = lambda: self.listen_loop(self.recv_size))
        
    def connect(self):
        self.socket.connect(self.addr)
        
    def recv(self,size):
        self.data = self.socket.recv(size)
        
    def listen_loop(self,size):
        while self.listen:
            data = self.socket.recv(size)
            self.data_queue.put(Data(data))
            
    def start_listening(self):
        self.listen = True
        self.listen_thread.start()
        
    def stop_listening(self):
        self.listen = False
        
    def pop_data(self):
        data = None
        try:
            data = self.data_queue.get()
        except Queue.Empty:
            print "Queue is empty! canno't pop data!"
            
        return data

    def is_queue_empty(self):
        return self.data_queue.empty()

        
