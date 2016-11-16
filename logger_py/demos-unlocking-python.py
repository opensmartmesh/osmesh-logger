


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

### Bitwise operations
# Exactly the same as in C++ with the use of numpy for type casting

def bme_set_all_measures_8(data):
    '''
        Data array of 8bits registers
        0    1    2    3    4    5    6    7
        0xF7 0xF8 0xF9 0xFA 0xFB 0xFC 0xFD 0xFE

        Output 32bits tuple of 3 uncompensated measures: Pressure, Temperature, Humidity
    '''
    adc_P = np.int32(  np.uint32(data[0])<<12 | np.uint32(data[1])<<4 | data[2]>>4  );  # 0xF7<<12 | 0xF8<<4 | 0xF9>>4
    adc_T = np.int32(  np.uint32(data[3])<<12 | np.uint32(data[4])<<4 | data[5]>>4  );  # 0xFA<<12 | 0xFB<<4 | 0xFC>>4
    adc_H = np.int32(  np.uint32(data[6])<<8  | data[7]  );                             # 0xF7<<12 | 0xF8<<4 | 0xF9>>4
    return (adc_P, adc_T, adc_H)

