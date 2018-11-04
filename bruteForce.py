import md5
from networking import Networking,Data

class MD5():
    def __init__(self,start,stop,md):
        self.start=start
        self.stop=stop
        self.mdStr=md
        self.l=len(start)
        self.hlp=self.start


    def tryy(self,index,hlp):
        hlp = list(hlp)
        if hlp[index]!="z":                                  
            hlp[index] = chr(ord(hlp[index])+1)
        else:
            hlp[index]="a"
        hlp = ''.join(hlp)
        return hlp

#####recursive check#####
    def lastCheck(self):
        for x in range(ord("a"),ord("z")+1):
            ezer = md5.new(self.hlp).hexdigest()
            if ezer==self.mdStr:
                return self.hlp
            self.hlp = self.tryy(self.l-1,self.hlp)
            if self.hlp==self.stop:
                return "not found"
        return "nope"
                
    def newCheck(self,z):
        for x in range(ord("a"),ord("z")+1):
            if z>0:
                ezra = self.newCheck(z-1)
                if ezra!="nope":
                    return ezra
                self.hlp = self.tryy(self.l-z-1,self.hlp)
            else:
                ezra = self.lastCheck()
                if ezra!="nope":
                    return ezra
        return "nope"

###########################

    def smartCheck(self):
        while self.hlp!=self.stop:
            ezer = md5.new(self.hlp).hexdigest()
            if ezer==self.mdStr:
                print "ret1"
                return Data(mode = Data.FOUND, result = self.hlp)
            hlp2 = list(self.hlp)
            hlp2[len(hlp2)-1] = chr(ord(hlp2[len(hlp2)-1])+1)
            for x in range(0,len(hlp2)):
                if ord(hlp2[len(hlp2)-1-x])>ord("z"):
                    hlp2[len(hlp2)-1-x]="a"
                    hlp2[len(hlp2)-1-x-1]= chr(ord(hlp2[len(hlp2)-1-x-1])+1)
            if ord(hlp2[0])>ord("z"):
                print "ret2"
                return Data(mode = Data.NOT_FOUND)
            self.hlp = ''.join(hlp2)
        print "ret3"
        return Data(mode = Data.NOT_FOUND)

def main():
    ADDR = ("10.30.57.235",2212)
    NAME = "THEJOKER"
    net = Networking(ADDR)
    net.connect()
    net.send_data(Data(mode = Data.HANDSHAKE,name = NAME))
    count =0
    while net.connected:
        data = []
        while not net.is_queue_empty():
            data.append(net.pop_data())
        for d in data:
            if d.mode == Data.CLOSE:
                net.close()
                break
            elif d.mode == Data.PACKAGE:
                print "package"
                breaker = MD5(d.start,d.stop,d.md5)
                net.send_data(breaker.smartCheck())
        if count>100:
            count=0
            net.send_data(Data(mode = Data.KEEP_ALIVE))
        count = count+1

    

if __name__ == "__main__":
    main()
    
"""                                
x = MD5("aaaaa","azzzz","9b7996ec2cfb97bd416dbb3a7367ad4e")

print x.smartCheck()
"""
