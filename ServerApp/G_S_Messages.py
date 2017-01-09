import pickle
import socket
import ChatUtils
def getMessage(conn):
    m = b""
    if conn == None:
        return 1
    while 1:
        try:
            conn.settimeout(1.0)
            data = conn.recv(1024)
            m += data
        except socket.timeout:
            continue
        try:
            message = pickle.loads(m)
            if message[1]:
                return 1
            break
        except:
            pass
    print(message[0])
    return message[0]



def sendMessage(conn,message="",Disconnect = False):
    message = [message,Disconnect]#ChatUtils.mail(Message = message , Disconnect = Disconnect)
    if conn != None:
        print(message[0])
        m = pickle.dumps(message)
        d = conn.send(m)
    else:
        return 1
