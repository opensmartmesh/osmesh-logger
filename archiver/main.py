#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from Server import Server
import datetime

from Message import Message
from MessageManager import MessageManager
from DatabaseConnector import DatabaseConnector


if  __name__ =='__main__':
    if len(sys.argv) > 1: # /dev/ttyACM0
        A = Server(sys.argv[1])
        A.run()
    else:
        print("Missing serial port pathname")
        
        # database creation
        conn = DatabaseConnector.connectSQLiteDB('meshDB.db')

        # MessageManager creation
        messageManager = MessageManager(conn)

        # DB reading
        messageManager.getAllMessages()

        # CSV writing
        df = messageManager.getAllMessagesintoPandaDataframe()
        df.to_csv('csvFile.csv', index = False)

        # DB update
        newMessage = Message('3', datetime.datetime.utcnow(), '0000', '0000', '0000')
        messageManager.putMessage(newMessage)

        # DB post
        newMessage = Message('4', datetime.datetime.utcnow(), '0000', '0000', '0000')
        messageManager.postMessage(newMessage)

        # DB read one Message from ID
        message1 = messageManager.getMessageFromId('6')
        print(message1)
        
        # DB delete
        messageManager.deleteMessage('5')

        conn.close
        
