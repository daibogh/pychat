import pickle
import hashlib
def encmd5(List):
	m = hashlib.md5()
	m.update("".join(List).encode("utf-8"))
	return m.digest()

class UserObject(object):
	def __init__(self,username,password,Conn):
		self.username = username
		self.isOnline = False
		self.OpenedChat = None
		self.Conn = Conn
		self.password = password

class mail(object):
    def __init__(self,Message = None , Disconnect = False , ChangeDialog = False):
        self.Message = Message
        self.Disconnect = Disconnect
        self.ChangeDialog = ChangeDialog



class UsersList(object):
	def __init__(self):
		try:
			f = open("/Users/Daibogh/Projects/pychat/ServerApp/UsersDir/UsersList.pkl","rb")
			self.List = pickle.load(f)
			f.close()
		except FileNotFoundError:
			self.List = {}
			f = open("/Users/Daibogh/Projects/pychat/ServerApp/UsersDir/UsersList.pkl","wb")
			self.List = pickle.dump(self.List,f)
			f.close()
			
	def RemoveUser(self,username):
		del self.List[username]
	def AddUser(self,username,password,conn):
		NewUser = UserObject(username,password,conn)
		self.List[username] = NewUser
	def Dump(self):
		for user in self.List.keys():
			print("self.List[user].isOnline")
			print(self.List[user].isOnline)
			self.List[user].isOnline = False
			print("self.List[user].Conn")
			print(self.List[user].Conn)
			if self.List[user].Conn != None:
				self.List[user].Conn.close()
				self.List[user].Conn = None
			self.List[user].OpenedChat = None
			
		f = open("/Users/Daibogh/Projects/pychat/ServerApp/UsersDir/UsersList.pkl","wb")
		pickle.dump(self.List,f)
		f.close()
class dialogObject(object):
	def __init__(self,UsersList):
		self.MessagesStacks = {i:[] for i in UsersList}
		self.List = UsersList
class DialogsList(object):
	def __init__(self):
		self.List = {}
		try:
			f = open("/Users/Daibogh/Projects/pychat/ServerApp/UsersDir/Dialogs.pkl","rb")
			self.List = pickle.load(f)
			f.close()
		except FileNotFoundError:
			
			f = open("/Users/Daibogh/Projects/pychat/ServerApp/UsersDir/Dialogs.pkl","wb")
			pickle.dump(self.List,f)
			f.close()
	

	def AddToStack(self,UsersList,user,message):
		DialogName = encmd5(UsersList)
		self.List[DialogName].MessagesStacks[user].append(message)

	

	def ReadFromStack(self,UsersList,user):
		DialogName = encmd5(UsersList)
		return "\n".join(self.List[DialogName].MessagesStacks[user])+"\n"

	

	def AddNewDialog(self,UsersList):
		DialogName = encmd5(UsersList)
		self.List[DialogName] = dialogObject(UsersList)
	

	def IsThereAChat(self,UsersList):
		DialogName = encmd5(UsersList)
		if DialogName in self.List.keys():
			return True
		else:
			return False












# 		