import serial, time

ser = serial.Serial()
ser.port = "COM7"

# 9600,8,N,1
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE

ser.timeout = 0.1
ser.writeTimeout = 0.1
ser.xonxoff = False
ser.rtscts = False
ser.dsrdtr = False

try:
    ser.open()
except Exception as ex:
    print ("open serial port error " + str(ex))
    exit()

if ser.isOpen():
    try:
        ser.flushInput()
        ser.flushOutput()
        while True:
            #ser.write('RES'.encode())
            response = ser.readline()
            time.sleep(1)
            data = response.decode("utf8").replace('\n', '').replace('\r', '')
            if data != '':
                print(data)
    except KeyboardInterrupt:
        ser.close()
    except Exception as e1:
        print("communicating error " + str(e1))

else:
    print ("open serial port error")