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

    reading =plc.read_area(snap7.types.Areas.DB,db_number,byte,size)
    a = snap7.util.get_bool(reading,0,bit)

    print(a)


def WriteBooltoDB(db_number, byte, size, bit,value):
    reading = plc.read_area(snap7.types.Areas.DB, db_number, byte, size)
    snap7.util.set_bool(reading, 0, bit,value)
    plc.write_area(snap7.types.Areas.DB,db_number,byte,reading)



def ReadintFromDB(db_number,byte,size):
    reading =plc.read_area(snap7.types.Areas.DB,db_number,byte,size)
    a = snap7.util.get_int(reading,0)
    print(a)


def WriteInttoDB(db_number, byte, size,value):
    reading = plc.read_area(snap7.types.Areas.DB, db_number, byte, size)
    snap7.util.set_int(reading, 0,value)
    plc.write_area(snap7.types.Areas.DB,db_number,byte,reading) # write the byte array again


def ReadRealFromDB(db_number,byte,size):
    reading =plc.read_area(snap7.types.Areas.DB,db_number,byte,size)
    a = snap7.util.get_real(reading,0)
    print(a)

def WriteRealtoDB(db_number, byte, size,value):
    reading = plc.read_area(snap7.types.Areas.DB, db_number, byte, size)  # get the byte array
    snap7.util.set_real(reading, 0,value)
    plc.write_area(snap7.types.Areas.DB,db_number,byte,reading) # write the byte array again



def ReadBoolFromMemory(byte,size,bit):
    reading =plc.read_area(snap7.types.Areas.MK,0,byte,size)
    a = snap7.util.get_bool(reading,0,bit)
    print(a)


def WriteBooltoMemory( byte, size, bit,value):
    reading = plc.read_area(snap7.types.Areas.MK, 0, byte, size)
    snap7.util.set_bool(reading, 0, bit,value)
    plc.write_area(snap7.types.Areas.MK,0,byte,reading)

def ReadintFromMemory(byte,size):
    reading =plc.read_area(snap7.types.Areas.MK,0,byte,size)
    a = snap7.util.get_int(reading,0)
    print(a)


def WriteInttoMemory( byte, size,value):

    reading = plc.read_area(snap7.types.Areas.MK, 0, byte, size)
    snap7.util.set_int(reading, 0,value)
    plc.write_area(snap7.types.Areas.MK,0,byte,reading)


def ReadRealFromMemory(byte,size):
    reading =plc.read_area(snap7.types.Areas.MK,0,byte,size)
    a = snap7.util.get_real(reading,0)
    print(a)

def WriteRealtoMemory( byte, size,value):
    reading = plc.read_area(snap7.types.Areas.MK, 0, byte, size)
    snap7.util.set_real(reading, 0,value)
    plc.write_area(snap7.types.Areas.MK,0,byte,reading)


def ReadBoolFromOutPut(byte,size,bit):
    reading =plc.read_area(snap7.types.Areas.PA,0,byte,size)
    a = snap7.util.get_bool(reading,0,bit)

    print(a)


def WriteBooltoOutPut( byte, size, bit,value):
    reading = plc.read_area(snap7.types.Areas.PA, 0, byte, size)
    snap7.util.set_bool(reading, 0, bit,value)
    plc.write_area(snap7.types.Areas.PA,0,byte,reading)

def ReadBoolFromInPut(byte,size,bit):
    reading =plc.read_area(snap7.types.Areas.PE,0,byte,size)
    a = snap7.util.get_bool(reading,0,bit)

    print(a)


def WriteBooltoInPut( byte, size, bit,value):
    reading = plc.read_area(snap7.types.Areas.PE, 0, byte, size)
    snap7.util.set_bool(reading, 0, bit,value)
    plc.write_area(snap7.types.Areas.PE,0,byte,reading)





#for Data Block
ReadBoolFromDB(1,0,1,0)
WriteBooltoDB(1,0,1,0,True)

ReadintFromDB(1,2,2)
WriteInttoDB(1,2,2,20)

ReadRealFromDB(1,4,4)
WriteRealtoDB(1,4,4,142.24)

#for memory
ReadBoolFromMemory(0,1,0)
WriteBooltoMemory(0,1,0)

ReadintFromMemory(2,2)
WriteInttoMemory(2,2,20)

ReadRealFromMemory(8,4)
WriteRealtoMemory(8,4,124.87)

#for input
ReadBoolFromInPut(0,1,0)
WriteBooltoInPut(0,1,0,True)

#FOR OUTPUT
ReadBoolFromOutPut(0,1,0)
WriteBooltoOutPut(0,1,0,True)