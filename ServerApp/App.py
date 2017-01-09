import socket
import threading
import pickle,sys
import ChatUtils
from ChatInterface import ChatInterface

def main():
    # pill2kill = threading.Event()
    usr = ChatUtils.UsersList()
    dialogs = ChatUtils.DialogsList()
    print(dialogs)
    print(usr)
    users = usr.List
    sock = socket.socket()
    sock.bind(("", int(sys.argv[1])))
    sock.listen()
    sockets = []
    mass = []
    while len(mass) < 1000:
        try:
            connection, address = sock.accept()
            sockets.append(connection)
            NewSocket = ChatInterface(connection, address,usr,dialogs)
            mass.append(NewSocket)
            NewSocket.start()
            print("mass is " + str(len(mass)))
        except KeyboardInterrupt:
            print("closing sockets")
            for i in sockets:
                i.close()
            print("closing is complete")
            print("exiting processes")

            sock.close()
            for i in range(len(mass)):
                mass[i].signal = False
                # mass[i].do_run = False
                # mass[i].join()
                print(mass[i])
                # pill2kill.set()
                mass[i].join()
                # mass[i].Event()
            print("exiting is completed")
            print("start dumping")
            print(users)
            usr.Dump()
            print("dumping is completed")
            break

    pass








if __name__ == "__main__":
    main()
