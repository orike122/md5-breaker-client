import socket,Queue,threading
"""
Example

net = Networking(("10.43.20.2",4320))
net.connect()

--------get data--------
if not net.is_queue_empty:
    data = net.pop_data()

if data.mode == Data.PACKAGE:
    start = data.start
    end = data.end
    md5 = data.md5
elif data.mode = Data.CLOSE:
    net.close()

--------send data--------
data = Data(mode = Data.NOT_FOUND)
or
data = Data(mode = Data.FOUND, result = "4320")
or
data = Data(mode = Data.KEEP_ALIVE)
or
data = Data(mode = Data.HANDSHAKE,name = "TheJoker")
finally
net.send_data(data)
"""
class Data(object):
    NOT_FOUND = 0
    FOUND = 1
    KEEP_ALIVE = 2
    HANDSHAKE = 4
    #from server
    CLOSE = 3
    PACKAGE = 5
    def __init__(self,mode = None ,raw_data = None, name = None, result = None):
        assert (not mode and raw_data) or (mode and not raw_data), "Either raw_data or mode have to be used while the other is not!"
        self.raw_data = raw_data
        self.name = name
        self.result = result
        self.mode = mode
        if self.mode == Data.FOUND:
            assert result, "you must supply result in FOUND mode!"
        elif self.mode == Data.HANDSHAKE:
            assert name, "you must supply name in HANDSHAKE mode!"
        self.process()

    def process(self):
        if self.mode == Data.NOT_FOUND:
            self.raw_data = "not found"
        elif self.mode == Data.FOUND:
            self.raw_data = "found:" + self.result
        elif self.mode == Data.KEEP_ALIVE:
            self.raw_data = "keep-alive"
        elif self.mode == Data.HANDSHAKE:
            self.raw_data = "name: " + self.name
        elif self.raw_data == "close":
            self.mode = Data.CLOSE
        elif self.raw_data.startswith('start:'):
            self.raw_data = self.raw_data.replace("start:","")
            self.raw_data = self.raw_data.replace("end:","")
            self.raw_data = self.raw_data.replace("md5:","")
            self.start,self.stop,self.md5 = self.raw_data.split(",")
        


    
class Networking(object):

    def __init__(self,addr):
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
            self.send_thread.start()
            self.listen_thread.start()
        except socket.error as err:
            print "canno't connect - socket error: " + str(err)
    
    def send_loop(self):
        while self.connected:
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
        self.data_buffer = data.raw_data
        
    def recv(self,size):
        data = self.socket.recv(size)
        self.data_queue.put(Data(raw_data=data))
        
    def listen_loop(self,size):
        while self.connected:
            try:
                self.recv(size)
            except socket.error as err:
                print "socket error: " + str(err)
                self.close()
        
    def pop_data(self):
        data = None
        try:
            data = self.data_queue.get()
        except Queue.Empty:
            print "Queue is empty! canno't pop data!"
            
        return data

    def is_queue_empty(self):
        return self.data_queue.empty()

        
