import serial, time
from openpyxl import Workbook
  
ser = serial.Serial()
ser.port = "COM3"
  
#9600,8,N,1
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS 
ser.parity = serial.PARITY_NONE 
ser.stopbits = serial.STOPBITS_ONE 

ser.timeout = 0.1           
ser.writeTimeout = 0.1      
ser.xonxoff = False    
ser.rtscts = False     
ser.dsrdtr = False     

wbTitle=['電壓','電流','功率','時間']
try: 
    ser.open()
except Exception as ex:
    print ("open serial port error " + str(ex))
    exit()
  
if ser.isOpen():  
    try:
        wb=Workbook()
        ws=wb.create_sheet('Log',0)
        ws.append(wbTitle)

        ser.flushInput() 
        ser.flushOutput() 
        while True :
            ser.write('RES\r\n'.encode())
            time.sleep(0.001)  
            response = ser.readline()
            data=(response.decode("utf8")).split(" ")
            data.append(time.strftime("%H:%M:%S"))

            if len(data) == 4:
                print("read V I P data:")
                ws.append(data)
                print(data)

    except KeyboardInterrupt :
        wb.save('Log資料.xlsx')
        ser.close()
        print('停止LOG')
        print('匯出Excel檔 OK!')
    except Exception as e1:
        print ("communicating error " + str(e1))
  
else:
    print ("open serial port error")

