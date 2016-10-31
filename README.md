# Open Smart Mesh Logger

Your central node holds the database and the logger serves as a translator from
the network radio messages to the messages send to the central server to be
saved in the databse.

To see how the server interacts with the database see osmesh-server-api

__Here is a global picture of the logger__

           \                        /            \       /
    osmesh  |--> | USB UART | ---> |  Translator  |-->  |  Archiver
    node   /                        \   c++      /       \  python

The logger is the sum of the Translator and the Archiver.
Translator and Archiver might be fused later into the same application.

## How to compile and run the  C++ translator

### Compiling

You need to have scons installed

To compile:
    # cd osmesh-logger/translator
    # scons

### Running the logger

    # cd osmesh-logger/translator
    # ./ser

Here are command line options:

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

## How to run the python archiver

    # cd osmesh-logger/archiver
    # python main.py

For now the archiver is not linked to the translator, so it is awaiting for some
data from the serial port, sent by an arduino for instance.


