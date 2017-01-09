import hashlib

def encmd5(List):
	m = hashlib.md5()
	m.update("".join(List).encode("utf-8"))
	return m.digest()