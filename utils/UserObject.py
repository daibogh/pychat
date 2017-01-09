class UserObject(object):
	def __init__(self,username,password,Conn):
		self.username = username
		self.isOnline = False
		self.OpenedChat = None
		self.Conn = Conn
		self.password = password