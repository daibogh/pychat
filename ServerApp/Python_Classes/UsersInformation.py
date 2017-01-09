import pickle
class Users(object):
    def __init__(self,filename):
        self.filename = filename
        f = open(filename,"rb")
        self.data = pickle.load(f)
        f.close()
    def Save(self):
    	f = open(self.filename,"wb")
    	pickle.dump(self.data,f)
    	f.close()
    def Refresh(self):
        f = open(self.filename,"rb")
        data = pickle.load(f)
        for i in data.keys():
            if i not in self.data.keys():
                self.data[i] = data[i]
    def RemoveUser(self,user):
    	self.Refresh()
    	self.data.pop(user,none)
    	self.Save()
    def AddUser(self,user,passwd):
    	self.Refresh()
    	self.data[user] = passwd
    	self.Save()
