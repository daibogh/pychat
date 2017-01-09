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