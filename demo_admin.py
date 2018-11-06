import socket


def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind(("0.0.0.0",4321))
    soc.listen(1)
    client,client_addr = soc.accept()
    print "connected"
    sendmd5(client)
    while True:
        d= client.recv(1024)
        print d
        if "found" in d:
            print d

def sendmd5(soc):
    soc.send("start:aaaaa,stop:aaaaz,md5:e80b5017098950fc58aad83c8c14978e")
    
if __name__ == "__main__":
    main()
