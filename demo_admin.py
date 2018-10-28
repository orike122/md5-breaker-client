import socket


def main():
    soc = socket.scoket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind(("0.0.0.0",4320))
    soc.listen(1)
    client,client_addr = soc.accept()
    sendmd5(client)
    while True:
        print client.recv(1024)

def sendmd5(soc):
    soc.send("start:aaaaa,stop:aaaaz,md5:e80b5017098950fc58aad83c8c14978e")
    
if __name__ == "__main__":
    main()
