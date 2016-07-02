import serial

import sys

import pandas as pd
import datetime

class Server():
    def __init__(self, serial_port):
        '''Constructor with default values only

        TODO have default values and user values as input
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
        coma_list = line_str.split(',')
        node_number = coma_list[0].split(':')[1]
        sensor_type, sensor_value = coma_list[1].split(':')
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
                self.df.loc[self.row_iter] =  [datetime.datetime.utcnow(),node_number, sensor_type, float(sensor_value)]
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
