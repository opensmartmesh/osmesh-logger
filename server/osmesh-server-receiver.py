import serial



class Server():
    def __init__(self):
        '''Constructor with default values only

        TODO have default values and user values as input
        '''
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
            ch     = str(port.read(), encoding="utf-7")
            rline += ch
            if (prevch=='\r' and  ch=='\n') or ch=='':
                return rline
            prevch=ch

    def run(self):
        port = serial.Serial("/dev/ttyACM0", 
            baudrate = self.serial_baudrate, 
            timeout  = self.serial_timeout,
            parity   = self.serial_parity,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS)
        while True:
            print("--- Listening...")
            rline = self.readlineCR(port)
            print("--- Received: "+rline+"\n")

if  __name__ =='__main__':
    A = Server()
    A.run()
