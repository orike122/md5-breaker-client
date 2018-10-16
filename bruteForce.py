import md5

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

x = MD5("aa","cc","de4b33a0ca6fcc673c62f3952a7daa21")
print x.newCheck(x.l-1)

            
                            
                            
                            
                                    
