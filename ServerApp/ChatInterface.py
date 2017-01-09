import socket
import threading
from Python_Classes.UsersInformation import Users
from G_S_Messages import *
import os
import ChatUtils
import sys
import select
encmd5 = ChatUtils.encmd5
mail = ChatUtils.mail






class ChatInterface(threading.Thread):
    
    





    def __init__(self, connection, address,usr,dialogs):
        threading.Thread.__init__(self)
        self.conn = connection
        self.address = address
        print(self.conn,self.address)
    
        self.usr = usr
        self.users = self.usr.List
        self.dialogs = dialogs
        self.signal = True
     


    def run(self):
        print("login")
        self.LogIn()
        
        

 





    def LogIn(self):
    
        check = sendMessage(self.conn,"choose you username")
        if check:
            return 1
        username = getMessage(self.conn)
        print(username)
        if username not in self.users.keys():
            check = sendMessage(self.conn," ".join(["where is no such user","would you like to register new user?(y/n)"]))
            if check:
                return 1
            answer = getMessage(self.conn)
            
            if answer == "y":
                self.register()
            else:
                check = sendMessage(self.conn,"connection is closed")
                if check:
                    return 1
                self.conn.close()
                pass
        else:
            check = sendMessage(self.conn,"type a password")
            if check:
                return 1
            password = getMessage(self.conn)
            if self.users[username].password == password:
                self.username = username
               
                self.users[username].Conn = self.conn
                self.users[username].isOnline = True
                self.interface(self.conn)
            else:
                check = sendMessage(self.conn,"connection is closed")
                if check:
                    return 1
                self.conn.close()
        return 0
        

    






    def register(self):
    
        while 1:
            check = sendMessage(self.conn,"type new username")
            if check:
                return 1
            NewUsername = getMessage(self.conn)
            if NewUsername not in self.users.keys():
                break
            else:
                check = sendMessage(self.conn,"you cannot use this name!")
                if check:
                    return 1
        while 1:
            check = sendMessage(self.conn,"type a password")
            if check:
                return 1
            password = getMessage(self.conn)
            check = sendMessage(self.conn,"type password again")
            if check:
                return 1
            password2 = getMessage(self.conn)
            if password == password2:
                break
            else:
                check = sendMessage(self.conn,"passwords not equal")
                if check:
                    return 1
        
        self.usr.AddUser(NewUsername,password,self.conn)
        
        check = sendMessage(self.conn,"new user has been added to database!")
        if check:
            return 1
        self.LogIn()
        return 0
        

    





    def interface(self,conn):
    
        while 1:
            check = sendMessage(conn,"type \'chat\' to switch on application")
            if check:
                return 1
            message = getMessage(conn)
            if message == "chat":
                result = self.ChatApplication()
                if result == "exit":
                    if conn:
                        conn.close()
                        return 0
            else:
                check = sendMessage(conn,"your message is " + message)
                if check:
                    return 1
    
    
    






    def ChatApplication(self):
        signal = 0
        while not signal:
            tempUsers = list(self.users.keys())
            tempUsers.remove(self.username)
            NewMessage = ["choose one or a few of this users","ctrl-c to refresh list","********"]+tempUsers+["********"]
            check = sendMessage(self.conn,"\n".join(NewMessage))
            if check:
                return 1
            # CurrentUser = getMessage(self.conn)
            CurrentUsers = getMessage(self.conn).split()
            flag = False
            for i in CurrentUsers:
                if i not in tempUsers:
                    sendMessage(self.conn,"there's no such user(s)")
                    flag = True
                    break
            if flag:
                continue
            else:
                CurrentUsers.append(self.username)
                CurrentUsers = sorted(CurrentUsers)
                self.users[self.username].OpenedChat = CurrentUsers
                signal = self.__chat(CurrentUsers)
        return "exit"
            # if CurrentUser in tempUsers:
            #     self.users[self.username].OpenedChat = CurrentUser
            #     self.__chat(self.users[CurrentUser])
            #     return 0
            # elif CurrentUser == "ctrl-c":
            #     pass
            # else:
            #     sendMessage(self.conn,"there's no such user")









    def __chat(self,CurrentUsers):
        if not self.dialogs.IsThereAChat(CurrentUsers):
            print('add new dialog\n\n\n')
            self.dialogs.AddNewDialog(CurrentUsers)
        else:
            check = sendMessage(self.conn,self.dialogs.ReadFromStack(CurrentUsers,self.username))
            if check:
                return 1
        NewCurrentUsers = sorted(CurrentUsers[:])
        NewCurrentUsers.remove(self.username)
        print(CurrentUsers)
        print(NewCurrentUsers)
        # if not CurrentUser.isOnline:
        #     sendMessage(self.conn,"this user is not online!")
        #     return 1
        # elif CurrentUser.OpenedChat != self.username:
        #     sendMessage(self.conn,"this user is not talking with you")
        #     return 1
        while 1:
            try:
                message = getMessage(self.conn)
            except ConnectionResetError:
                self.conn = None
                self.users[self.username].isOnline = False
                self.users[self.username].OpenedChat = None
                return 1
            message = "".join([self.username,"->",message])
            for GettingUser in NewCurrentUsers:
                if self.users[GettingUser].isOnline and self.users[GettingUser].OpenedChat == CurrentUsers:
                    check = sendMessage(self.users[GettingUser].Conn, message)
                    if check:
                        return 1
                else:
                    print(GettingUser)
                    print(self.users[GettingUser].isOnline)
                    print("opened chat is")
                    print(self.users[GettingUser].OpenedChat)
                    self.dialogs.AddToStack(CurrentUsers,GettingUser,message)
            # m = sendMessage(CurrentUser.Conn, "".join([self.username,"->",message]))

    
   








