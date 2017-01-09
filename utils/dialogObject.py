lass dialogObject(object):
	def __init__(self,UsersList):
		self.MessagesStacks = {i:[] for i in UsersList}
		self.List = UsersList