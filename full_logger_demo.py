


######   #######  #     #  #######  
#     #  #        ##   ##  #     #  
#     #  #        # # # #  #     #  
#     #  #####    #  #  #  #     #  
#     #  #        #     #  #     #  
#     #  #        #     #  #     #  
######   #######  #     #  #######  

## This demo shows you can do everything in python

### Convert HEX string to Integers:
print("Convert 0xaeadbeef to Integer:")
print(int("0xaeadbeef", 0))


### Read from a binary stream
with open(filename, 'rb') as fileobj:
    for chunk in iter(lambda: fileobj.read(4), ''):
        integer_value = struct.unpack('<I', chunk)[0]

### Read from serial port (already shown in archiver/Server.py)

