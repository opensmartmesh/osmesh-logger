#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Message import Message

import sqlite3
import datetime
import pandas as pd

class MessageManager():
    
   
    def __init__(self, DB_connection):
        self.conn = DB_connection


    def postMessage(self, message):
        cursor = self.conn.cursor()
        cursor.execute("""INSERT INTO messages(timestamp, node_id, node_type, value) VALUES(?, ?, ?, ?)""", (message.date, message.node_number, message.sensor_type, float(message.sensor_value)))
        self.conn.commit()
    
    def getMessageFromId(self, idMessage):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT id, timestamp, node_id, node_type, value FROM messages WHERE id=?""", (idMessage,))
        messageTemp = cursor.fetchone()
        print(messageTemp)
        message = Message(messageTemp[0], messageTemp[1], messageTemp[2], messageTemp[3], messageTemp[4])
        return message
    
    def getAllMessages(self):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT id, timestamp, node_id, node_type, value FROM messages""")
        messagesList = []
        for row in cursor:
            #print('{0} : {1}, {2}, {3}, {4}'.format(row[0], row[1], row[2], row[3], row[4]))
            messagesList.append(Message(row[0], row[1], row[2], row[3], row[4]))
        return messagesList

    def getAllMessagesintoPandaDataframe(self):
        df = pd.DataFrame(columns = ['id', 'timestamp','node_id','node_type','value'])
        cursor = self.conn.cursor()
        cursor.execute("""SELECT id, timestamp, node_id, node_type, value FROM messages""")
        row_iter = 0
        for row in cursor:
            df.loc[row_iter] =  [row[0], row[1], row[2], row[3], float(row[4])]
            row_iter += 1
        return df    

    def putMessage(self, message):
        cursor = self.conn.cursor()
        cursor.execute("""UPDATE messages SET timestamp = ?, node_id = ?, node_type = ?, value = ? WHERE id = ?""", (message.date, message.node_number, message.sensor_type, message.sensor_value, message.idDB,))
        self.conn.commit()

    def deleteMessage(self, idMessage):
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("""DELETE FROM messages WHERE id=?""", (idMessage,))
            self.conn.commit()
            print("delete OK")
        except Exception as e:
            print("Erreur"+e)

    def parse_line(self, currentDate, line_str):
        """ parse the line given in input

            Return a Message created from the line

        """
        node_number  = "-1" 
        sensor_type  = "nosensor"
        sensor_value = "-1.0"

        coma_list    = line_str.split(',')
        keys1 = []
        keys2 = []

        if (len(coma_list) < 2):
            sensor_type  = "blogmessage"
            message = Message(currentDate, node_number, sensor_type, sensor_value)
            return message
        else:
            keys1 = coma_list[0].split(':')
            keys2 = coma_list[1].split(':')

        if (len(keys1) > 1):
            #if keys[0] == "nodeid"
            node_number = keys1[1] 
        else:
            # No node id found
            node_number = "-2"

        if (len(keys2) > 1):
            sensor_type  = keys2[0]
            sensor_value = keys2[1]
        # else sensor_type = "nosensor"
        
        message = Message(currentDate, node_number, sensor_type, sensor_value)
        return message
