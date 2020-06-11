import serial
import time

# To test the loopback, connect 2 and 3 on the 9pin serial port.
port = input('port(ex. COM1): ')
comm = serial.Serial(port, baudrate=115200, timeout=0)

while True:
    tx_msg = input('send msg: ')
	if msg == 'q' :
	    break
	
	comm.write(tx_msg.encode('utf-8'))
	
	time.sleep(0.5)
	
	if comm.readable():
	   rx_msg = comm.readline()
	   print(rx_msg.decode('utf-8')
	
comm.close()
