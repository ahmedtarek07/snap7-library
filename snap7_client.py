import snap7



# Define the PLC address
plc_ip = '192.168.0.1'  # Replace with the IP address of your PLC
plc_rack = 0
plc_slot = 1

# Create a Snap7 client
plc = snap7.client.Client()
# Connect to the PLC
plc.connect(plc_ip, plc_rack, plc_slot)
# get the status of PLC 'RUN , STOP , .. '
state = plc.get_cpu_state() # get plc state
print(f"state {state}")

#Reading data


def ReadBoolFromDB(db_number,byte,size,bit):
    #1- read bool from data block
    # reading =plc.read_area(TYPE : snap7.types.Areas.DB, db number : 1, start byte :0, size of bytes : 1) # get the byte array
    reading =plc.read_area(snap7.types.Areas.DB,db_number,byte,size) # get the byte array

    # a= snap7.util.get_bool(byte array : reading,byte index in the byte array : 0, bit index in the byte array : 0)
    # byte index is the byte index in the byte array : so we take it zero as the first byte
    a = snap7.util.get_bool(reading,byte,bit)

    print(a)


def WriteBooltoDB(db_number, byte, size, bit,value):
    # 1- write bool from data block
    #get the data from the plc in byte array
    # reading =plc.read_area(TYPE : snap7.types.Areas.DB, db number : 1, start byte :0, size of bytes : 1) # get the byte array
    reading = plc.read_area(snap7.types.Areas.DB, db_number, byte, size)  # get the byte array
    #set the value in the specific bit
    # snap7.util.set_bool(byte array : reading,byte index in the byte array : 0, bit index in the byte array : 0, value: True or False)
    # byte index is the byte index in the byte array : so we take it zero as the first byte
    snap7.util.set_bool(reading, 0, bit,value)
    snap7.util.set_bool(reading,0,bit,value)
    #write the data "byte array " in the plc again
    # plc.write_area(type : snap7.types.Areas.DB,db_number,start byte : byte,byte array : reading) # write the byte array again
    plc.write_area(snap7.types.Areas.DB,db_number,byte,reading) # write the byte array again



def ReadintFromDB(db_number,byte,size):
    #1- read int from data block
    # reading =plc.read_area(TYPE : snap7.types.Areas.DB, db number : 1, start byte :0, size of bytes : 2) # get the byte array
    reading =plc.read_area(snap7.types.Areas.DB,db_number,byte,size) # get the byte array

    # a= snap7.util.get_int(byte array : reading,byte index in the byte array : 0)
    # byte index is the byte index in the byte array : so we take it zero as the first byte of the byte array
    a = snap7.util.get_int(reading,0)
    print(a)


def WriteInttoDB(db_number, byte, size,value):
    # 1- write int from data block
    #get the data from the plc in byte array
    # reading =plc.read_area(TYPE : snap7.types.Areas.DB, db number : 1, start byte :0, size of bytes : 2) # get the byte array
    reading = plc.read_area(snap7.types.Areas.DB, db_number, byte, size)  # get the byte array
    #set the value in the specific bit
    # snap7.util.set_bool(byte array : reading,byte index in the byte array : 0, value: number)
    # byte index is the byte index in the byte array : so we take it zero as the first byte
    snap7.util.set_int(reading, 0,value)
    #write the data "byte array " in the plc again
    # plc.write_area(type : snap7.types.Areas.DB,db_number,start byte : byte,byte array : reading) # write the byte array again
    plc.write_area(snap7.types.Areas.DB,db_number,byte,reading) # write the byte array again


def ReadRealFromDB(db_number,byte,size):
    #1- read real from data block
    # reading =plc.read_area(TYPE : snap7.types.Areas.DB, db number : 1, start byte :0, size of bytes : 4) # get the byte array
    reading =plc.read_area(snap7.types.Areas.DB,db_number,byte,size) # get the byte array

    # a= snap7.util.get_int(byte array : reading,byte index in the byte array : 0)
    # byte index is the byte index in the byte array : so we take it zero as the first byte of the byte array
    a = snap7.util.get_real(reading,0)
    print(a)

def WriteRealtoDB(db_number, byte, size,value):
    # 1- write real from data block
    #get the data from the plc in byte array
    # reading =plc.read_area(TYPE : snap7.types.Areas.DB, db number : 1, start byte :0, size of bytes : 4) # get the byte array
    reading = plc.read_area(snap7.types.Areas.DB, db_number, byte, size)  # get the byte array
    #set the value in the specific bit
    # snap7.util.set_bool(byte array : reading,byte index in the byte array : 0, value: number)
    # byte index is the byte index in the byte array : so we take it zero as the first byte
    snap7.util.set_real(reading, 0,value)
    #write the data "byte array " in the plc again
    # plc.write_area(type : snap7.types.Areas.DB,db_number,start byte : byte,byte array : reading) # write the byte array again
    plc.write_area(snap7.types.Areas.DB,db_number,byte,reading) # write the byte array again



def ReadBoolFromMemory(byte,size,bit):
    #1- read bool from data block
    # reading =plc.read_area(TYPE : snap7.types.Areas.mk, db number : 0, start byte :0, size of bytes : 1) # get the byte array
    reading =plc.read_area(snap7.types.Areas.MK,0,byte,size) # get the byte array

    # a= snap7.util.get_bool(byte array : reading,byte index in the byte array : 0, bit index in the byte array : 0)
    # byte index is the byte index in the byte array : so we take it zero as the first byte
    a = snap7.util.get_bool(reading,0,bit)

    print(a)


def WriteBooltoMemory( byte, size, bit,value):
    # 1- write bool from data block
    #get the data from the plc in byte array
    # reading =plc.read_area(TYPE : snap7.types.Areas.MK, db number : 0, start byte :0, size of bytes : 1) # get the byte array
    reading = plc.read_area(snap7.types.Areas.MK, 0, byte, size)  # get the byte array
    #set the value in the specific bit
    # snap7.util.set_bool(byte array : reading,byte index in the byte array : 0, bit index in the byte array : 0, value: True or False)
    # byte index is the byte index in the byte array : so we take it zero as the first byte
    snap7.util.set_bool(reading, 0, bit,value)
    #write the data "byte array " in the plc again
    # plc.write_area(type : snap7.types.Areas.DB,db_number,start byte : byte,byte array : reading) # write the byte array again
    plc.write_area(snap7.types.Areas.MK,0,byte,reading) # write the byte array again

def ReadintFromMemory(byte,size):
    #1- read int from data block
    # reading =plc.read_area(TYPE : snap7.types.Areas.MK, db number : 0, start byte :0, size of bytes : 2) # get the byte array
    reading =plc.read_area(snap7.types.Areas.MK,0,byte,size) # get the byte array

    # a= snap7.util.get_int(byte array : reading,byte index in the byte array : 0)
    # byte index is the byte index in the byte array : so we take it zero as the first byte of the byte array
    a = snap7.util.get_int(reading,0)
    print(a)


def WriteInttoMemory( byte, size,value):
    # 1- write int from data block
    #get the data from the plc in byte array
    # reading =plc.read_area(TYPE : snap7.types.Areas.MK, db number : 1, start byte :0, size of bytes : 2) # get the byte array
    reading = plc.read_area(snap7.types.Areas.MK, 0, byte, size)  # get the byte array
    #set the value in the specific bit
    # snap7.util.set_bool(byte array : reading,byte index in the byte array : 0, value: number)
    # byte index is the byte index in the byte array : so we take it zero as the first byte
    snap7.util.set_int(reading, 0,value)
    #write the data "byte array " in the plc again
    # plc.write_area(type : snap7.types.Areas.MK,db_number,start byte : byte,byte array : reading) # write the byte array again
    plc.write_area(snap7.types.Areas.MK,0,byte,reading) # write the byte array again


def ReadRealFromMemory(byte,size):
    #1- read real from data block
    # reading =plc.read_area(TYPE : snap7.types.Areas.MK, db number : 1, start byte :0, size of bytes : 4) # get the byte array
    reading =plc.read_area(snap7.types.Areas.MK,0,byte,size) # get the byte array

    # a= snap7.util.get_int(byte array : reading,byte index in the byte array : 0)
    # byte index is the byte index in the byte array : so we take it zero as the first byte of the byte array
    a = snap7.util.get_real(reading,0)
    print(a)

def WriteRealtoMemory( byte, size,value):
    # 1- write real from data block
    #get the data from the plc in byte array
    # reading =plc.read_area(TYPE : snap7.types.Areas.MK, db number : 1, start byte :0, size of bytes : 4) # get the byte array
    reading = plc.read_area(snap7.types.Areas.MK, 0, byte, size)  # get the byte array
    #set the value in the specific bit
    # snap7.util.set_bool(byte array : reading,byte index in the byte array : 0, value: number)
    # byte index is the byte index in the byte array : so we take it zero as the first byte
    snap7.util.set_real(reading, 0,value)
    #write the data "byte array " in the plc again
    # plc.write_area(type : snap7.types.Areas.MK,db_number,start byte : byte,byte array : reading) # write the byte array again
    plc.write_area(snap7.types.Areas.MK,0,byte,reading) # write the byte array again


def ReadBoolFromOutPut(byte,size,bit):
    #1- read bool from data block
    # reading =plc.read_area(TYPE : snap7.types.Areas.PE, db number : 1, start byte :0, size of bytes : 1) # get the byte array
    reading =plc.read_area(snap7.types.Areas.PA,0,byte,size) # get the byte array

    # a= snap7.util.get_bool(byte array : reading,byte index in the byte array : 0, bit index in the byte array : 0)
    # byte index is the byte index in the byte array : so we take it zero as the first byte
    a = snap7.util.get_bool(reading,0,bit)

    print(a)


def WriteBooltoOutPut( byte, size, bit,value):
    # 1- write bool from data block
    #get the data from the plc in byte array
    # reading =plc.read_area(TYPE : snap7.types.Areas.PE, db number : 1, start byte :0, size of bytes : 1) # get the byte array
    reading = plc.read_area(snap7.types.Areas.PA, 0, byte, size)  # get the byte array
    #set the value in the specific bit
    # snap7.util.set_bool(byte array : reading,byte index in the byte array : 0, bit index in the byte array : 0, value: True or False)
    # byte index is the byte index in the byte array : so we take it zero as the first byte
    snap7.util.set_bool(reading, 0, bit,value)
    #write the data "byte array " in the plc again
    # plc.write_area(type : snap7.types.Areas.PE,db_number,start byte : byte,byte array : reading) # write the byte array again
    plc.write_area(snap7.types.Areas.PA,0,byte,reading) # write the byte array again

def ReadBoolFromInPut(byte,size,bit):
    #1- read bool from data block
    # reading =plc.read_area(TYPE : snap7.types.Areas.PE, db number : 1, start byte :0, size of bytes : 1) # get the byte array
    reading =plc.read_area(snap7.types.Areas.PE,0,byte,size) # get the byte array

    # a= snap7.util.get_bool(byte array : reading,byte index in the byte array : 0, bit index in the byte array : 0)
    # byte index is the byte index in the byte array : so we take it zero as the first byte
    a = snap7.util.get_bool(reading,0,bit)

    print(a)


def WriteBooltoInPut( byte, size, bit,value):
    # 1- write bool from data block
    #get the data from the plc in byte array
    # reading =plc.read_area(TYPE : snap7.types.Areas.PE, db number : 1, start byte :0, size of bytes : 1) # get the byte array
    reading = plc.read_area(snap7.types.Areas.PE, 0, byte, size)  # get the byte array
    #set the value in the specific bit
    # snap7.util.set_bool(byte array : reading,byte index in the byte array : 0, bit index in the byte array : 0, value: True or False)
    # byte index is the byte index in the byte array : so we take it zero as the first byte
    snap7.util.set_bool(reading, 0, bit,value)
    #write the data "byte array " in the plc again
    # plc.write_area(type : snap7.types.Areas.PE,db_number,start byte : byte,byte array : reading) # write the byte array again
    plc.write_area(snap7.types.Areas.PE,0,byte,reading) # write the byte array again

#for Data Block
# WriteBooltoDB(1,0,1,0,True)
# ReadBoolFromDB(1,0,1,0)
#

# WriteInttoDB(1,2,2,150)
# ReadintFromDB(1,2,2)

# WriteRealtoDB(1,4,4,28.9)
# ReadRealFromDB(1,4,4)

# #for memory


# # WriteBooltoMemory(0,1,0,False)
# ReadBoolFromMemory(0,1,0)


# WriteInttoMemory(2,2,100)
# ReadintFromMemory(2,2)
#

# WriteRealtoMemory(8,4,100.09)
# ReadRealFromMemory(8,4)
#
# #for input

# WriteBooltoInPut(1,1,0,True)
# ReadBoolFromInPut(1,1,0)

# #FOR OUTPUT


WriteBooltoOutPut(0,1,1,False)
ReadBoolFromOutPut(0,1,1)