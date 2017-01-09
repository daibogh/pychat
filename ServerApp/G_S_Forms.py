class GettingForm(threading.Thread):
    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.conn = connection
        # self.address = address
    def run(self):
        self.Interface()
    def Interface(self):
        while 1:
            message = getMessage(self.conn)
            print(message)
            pass



class SendingForm(threading.Thread):
    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.conn = connection
        # self.address = address
    def run(self):
        self.Interface()
    def Interface(self):
        while 1:
            try:
                pass
                message = input()
                t = sendMessage(self.conn,message)
            except KeyboardInterrupt:

                self.conn.close()
                print("connection is closed")
                os._exit()
