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
