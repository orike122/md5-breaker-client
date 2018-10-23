import socket,Queue,threading
class Data(object):
    #TODO fix wrong logics
    #from client
    NOT_FOUND = 0
    FOUND = 1
    KEEP_ALIVE = 2
    HANDSHAKE = 4
    #from server
    CLOSE = 3
    PACKAGE = 5
    def __init__(self,mode = None ,raw_data = None, name = None, start = None, stop = None, md5 = None, result = None):
        assert (not mode and raw_data) or (mode and not raw_data), "Either raw_data or mode have to be used while the other is not!"
        self.raw_data = raw_data
        self.name = name
        self.start = start
        self.stop = stop
        self.md5 = md5
        self.result = result
        self.mode = mode
        if self.mode == FOUND:
            assert result, "you must supply result in FOUND mode!"
        elif self.mode == HANDSHAKE:
            assert name, "you must supply name in HANDSHAKE mode!"
        elif self.mode == PACKAGE:
            assert start, "you must supply start in PACKAGE mode!"
            assert start, "you must supply stop in PACKAGE mode!"
            assert start, "you must supply md5 in PACKAGE mode!"
    def handle_mode(self):
        if self.mode == NOT_FOUND:
            self.raw_data = "not found"
        elif self.mode == FOUND:
            self.raw_data = "found: " + result
        elif self.mode == KEEP_ALIVE:
            self.raw_data = "keep-alive"
        elif self.mode == HANDSHAKE:
            self.raw_data = "name: " + name
        elif self.raw_data == "close":
            self.mode = CLOSE
        
    def __repr__(self):
        pass

    
class Networking(object):

    def __init___(self,addr):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = addr
        self.data_queue = Queue.Queue()
        self.recv_size = 1024
        self.listen_thread = threading.Thread(target = lambda: self.listen_loop(self.recv_size))
        self.send_thread = threading.Thread(target = self.send_loop)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        self.data_buffer = None
        self.connected = False
        
    def connect(self):
        try:
            self.socket.connect(self.addr)
            self.connected = True
        except socket.error as err:
            print "canno't connect - socket error: " + str(err)
    
    def send_loop(self)
        while connected:
            if self.data_buffer:
                try:
                    self.send_data(self.data_buffer)
                except socket.error as err:
                    print "socket error: " + err
                    self.close()
                except Exception as err:
                    print "general error in send_loop: " + str(err)
                    raise err
                finally:
                    self.data_buffer = None
                
    def close(self):
        self.connected = False
        self.socket.close()
        
    def send_data(self,data):
        self.data_buffer = data
        
    def recv(self,size):
        self.data = self.socket.recv(size)
        #TODO: add logic based on protocol
        
    def listen_loop(self,size):
        while self.connected:
            try:
                data = self.recv(size)
                self.data_queue.put(Data(data))
            except socket.error as err:
                print "socket error: " + str(err)
                self.close()
            
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

        
