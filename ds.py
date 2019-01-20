import hashlib as hsh

#Blockchain data structure

class Block:
    def __init__(self,index,tstmp,data,previous_hash):
        self.index=index
        self.tstmp=tstmp
        self.data=data
        self.previous_hash=previous_hash
        self.hash=self.hashit()

    def hashit(self):
        hshr=hsh.sha256()
        #hash of current depends on hash of previous block
        dt=str(self.index)+str(self.tstmp)+str(self.data)+str(self.previous_hash)
        hshr.update(dt.encode('utf-8'))
        return hshr.hexdigest()


