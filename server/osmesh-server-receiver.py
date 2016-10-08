import serial

import sys

import pandas as pd
import datetime

class Server():
    def __init__(self, serial_port):
        '''Constructor with default values only

        TODO have default values and user values as input
        
        test
        '''
        self.serial_port     = serial_port
        self.serial_baudrate = 115200
        self.serial_parity   = serial.PARITY_ODD
        self.serial_timeout  = None
        
        self.df = pd.DataFrame(columns = ['timestamp','node_id','node_type','value'])
        self.row_iter = 0


    def readlineCR(self, port):
        '''Listen on the serial port and construct a string until \r\n is met
        '''
        print("--- Reading line")
        rline  = ""
        prevch = ''
        while True:
            ch     = str(port.read(), encoding="utf-7")
            #ch     = str(port.read())
            rline += ch
            if (prevch=='\r' or  ch=='\n') or ch=='':
                return rline
            prevch=ch

    def parse_line(self,line_str):
        node_number  = "-1" 
        sensor_type  = "nosensor"
        sensor_value = "-1.0"

        coma_list    = line_str.split(',')
        keys1 = []
        keys2 = []

        if (len(coma_list) < 2):
            sensor_type  = "blogmessage"
            return node_number, sensor_type, sensor_value
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

        return node_number, sensor_type, sensor_value
        
    def run(self):
        port = serial.Serial(self.serial_port, 
            baudrate = self.serial_baudrate, 
            timeout  = self.serial_timeout,
            parity   = self.serial_parity,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS)
        while True:
            print("--- Listening...")
            rline = self.readlineCR(port)
            try:
                print("Parsing line: "+rline)
                node_number, sensor_type, sensor_value = self.parse_line(rline)
                self.df.loc[self.row_iter] =  [datetime.datetime.utcnow(), node_number, sensor_type, float(sensor_value)]
                self.row_iter += 1
                self.df.to_csv('../../test.csv',index = False)

            except ValueError:
                print("ValueError Exception")
                print(str(len(rline))+" "+rline)
            print("--- Received: "+rline+"\n")

if  __name__ =='__main__':
    if len(sys.argv) > 1:
        A = Server(sys.argv[1])
        A.run()
    else:
        print("Missing serial port pathname")
