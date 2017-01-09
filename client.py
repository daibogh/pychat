# import getch as g
import socket
import time
import threading
import pickle
import os,sys

def getMessage(conn):
    message = b""
    while 1:
        # print("lolec")
        try:
            conn.settimeout(1.0)
            data = conn.recv(1024)
            message += data
        except socket.timeout:
            continue
        try:
            message = pickle.loads(message)
            # print(message[0])
            break
        except:
            pass
    return message
def sendMessage(conn,message):
    message = pickle.dumps(message)
    try:
        a = conn.send(message)
    except ConnectionResetError:
        print("unfortunately, connection is closed")
        return 1
    return 0

class GettingForm(threading.Thread):
    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.conn = connection
        # self.address = address
    def run(self):
        self.Interface()
    def Interface(self):
        # write = sys.stdout.write
        while self.conn!= None:
            # print("lol")
            try:
                message = getMessage(self.conn)
                if message[1]:
                    # print("test")
                    self.conn.close()
            except ConnectionResetError:
                print("unfortunately, connection is closed")
                break
            print(message[0])
            # write(str(message))
            # print(message)
            pass

class SendingForm(threading.Thread):
    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.conn = connection
        # self.address = address
    def run(self):
        try:
            self.Interface()
        except BrokenPipeError:
            return 0
    def Interface(self):
        while self.conn != None:
            try:
                message = [input(),False]#mail(Message =input())
                sendMessage(self.conn,message)
            except KeyboardInterrupt:

                self.conn.close()
                print("connection is closed")
                os._exit()
        self.conn.close()
        print("programm is closed")


def main():
    sock = socket.socket()
    sock.connect((sys.argv[1],int(sys.argv[-1])))
    # client = NewThread(sock)
    # client.start()
    Get = GettingForm(sock)
    Send = SendingForm(sock)
    Send.start()
    Get.start()
    

if __name__ == "__main__":
    main()