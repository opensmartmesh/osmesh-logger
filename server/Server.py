#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Message import Message
from MessageManager import MessageManager
from DatabaseConnector import DatabaseConnector

import serial
import sys
import pandas as pd
import datetime
import sqlite3

class Server():
    
    def __init__(self, serial_port):
        '''Constructor with default values only

        TODO have default values and user values as input
        
        '''
        self.serial_port     = serial_port
        self.serial_baudrate = 115200
        self.serial_parity   = serial.PARITY_ODD
        self.serial_timeout  = None


    def readlineCR(self, port):
        '''Listen on the serial port and construct a string until \r\n is met
        '''
        print("--- Reading line")
        rline  = ""
        prevch = ''
        while True:
            if (sys.version_info.major==3):
                ch     = str(port.read(), encoding="utf-7") # for Python 3
            elif (sys.version_info.major==2):
                ch     = str(port.read())                  # for python 2
            else:
                print("The used version of Python is too old : version "+str(sys.version_info.major))
                return rline
            rline += ch
            if (prevch=='\r' or  ch=='\n') or ch=='':
                return rline
            prevch=ch


    def run(self):
        port = serial.Serial(self.serial_port, 
            baudrate = self.serial_baudrate, 
            timeout  = self.serial_timeout,
            parity   = self.serial_parity,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS)
        
        # database creation
        conn = DatabaseConnector.connectSQLiteDB('meshDB.db')

        # MessageManager creation
        self.messageManager = MessageManager(conn)
        
        # reading loop
        print("Python version detected : "+str(sys.version_info.major))
        while True:
            print("--- Listening...")
            rline = self.readlineCR(port)
            currentDate = datetime.datetime.utcnow()
            try:
                print("Parsing line: "+rline)
                message = self.messageManager.parse_line(currentDate, rline)
                
                # CSV writing
                #self.df.loc[self.row_iter] =  [datetime.datetime.utcnow(), node_number, sensor_type, float(sensor_value)]
                #self.df.to_csv('./test.csv',index = False)
                
                # DB writing
                self.messageManager.postMessage(message)


            except ValueError:
                print("ValueError Exception")
                print(str(len(rline))+" "+rline)
            except Exception as e:
                print("Erreur"+e)
                conn.rollback()
                # raise e

            print("--- Received: "+rline+"\n")
            
        # closing of the database
        conn.close()

