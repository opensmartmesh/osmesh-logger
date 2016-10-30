# Open Smart Mesh Logger

Your central node holds the database and the logger serves as a translator from
the network radio messages to the messages send to the central server to be
saved in the databse.

To see how the server interacts with the database see osmesh-server-api


# Compile and Run the  C++ translator

## Compiling

You need to have scons installed

To compile use hit:
scons

## Running the logger

help 

Command line example 
'./ser param1=value1 param2=value2':

Parameters:

- port:	the serial device to be used
  Mandatory
  e.g 'port=/dev/ttyUSB0'

- logfile: file where the logged data will be saved.
  Optionnal
  e.g 'logfile=logfile.txt'

- logout: e.g 'logcmd=1'
  Optional

- configfile:
  Optional if not provided, an attempt is made to read config from 'configfile.txt' if available.
  e.g 'configfile=conf2.txt'
