import md5
import threading

class MD5():
    def __init__(self,start,stop,md):
        self.start=start
        self.stop=stop
        self.mdStr=md
        self.l=len(start)
        self.hlp=self.start
        self.middle = self.seperate()

    def tryy(self,index,hlp):
        hlp = list(hlp)
        if hlp[index]!="z":                                  
            hlp[index] = chr(ord(hlp[index])+1)
        else:
            hlp[index]="a"
        hlp = ''.join(hlp)
        return hlp

    def seperate(self):
        start2 = list(self.start)
        stop2 = list(self.stop)
        s = []
        z=""
        for x in range(0,len(start2)):
            s.append(ord(stop2[x])-ord(start2[x]))
        for x in range(0,len(s)):
            z=z+chr(ord(start2[x])+(s[x]/2))
        return z

    def do():
        pass #to do, threading
#####recursive check#####
    def lastCheck(self):
        for x in range(ord("a"),ord("z")+1):
            ezer = md5.new(self.hlp).hexdigest()
            print self.hlp
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
                    if ezra!="not found":
                        return ezra
                    return "not found"
                self.hlp = self.tryy(self.l-z-1,self.hlp)
            else:
                ezra = self.lastCheck()
                if ezra!="nope":
                    if ezra!="not found":
                        return ezra
                    return "not found"
        return "nope"

###########################

####not recursive check####
    def check(self):
        hlp = self.start
        for x in range(ord("a"),ord("z")+1):
            for x in range(ord("a"),ord("z")+1):
                for x in range(ord("a"),ord("z")+1):
                    for x in range(ord("a"),ord("z")+1):
                        for x in range(ord("a"),ord("z")+1):
                            for x in range(ord("a"),ord("z")+1):
                                ezer = md5.new(hlp).hexdigest()
                                if ezer==self.mdStr:
                                    return hlp
                                hlp = self.tryy(5,hlp)
                            hlp = self.tryy(4,hlp)
                        hlp = self.tryy(3,hlp)
                    hlp = self.tryy(2,hlp)
                hlp = self.tryy(1,hlp)
            hlp = self.tryy(0,hlp)

        return "not found"
#############################

        
start = "aaaaa"
stop = "bbbbb"

x = MD5(start,stop,"de4b33a0ca6fcc673c62f3952a7daa21")

x.do()



            
                            
                            
                            
                                    
