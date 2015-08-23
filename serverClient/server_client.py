# Client-server configuration via ethernet connect
# server client
# Alex Canton

from socket import *
import time 

address = ( '10.1.15.247', 5000) #match arduino and port to define specific communication between arduino and server
client_socket = socket(AF_INET, SOCK_DGRAM) #start set-up for Socket
client_socket.settimeout(2) #timeout after 2 seconds 

while(2): 
	data = "Blue" #set data command to Blue 
	client_socket.sendto(data, address) #send command to the arduino
	try:
		rec_data, addr = client_socket.recvfrom(2048) # read data from arduino
		print rec_data #print data recieved from the arduino
	except:
		pass 
		
	time.sleep(2) # time delay before the next command is 
	
	data = "Red" #set data command to Red 
	client_socket.sendto(data, address) #send command to the arduino
	try:
		rec_data, addr = client_socket.recvfrom(2048) # read data from arduino
		print rec_data #print data recieved from the arduino
	except:
		pass 
		
	time.sleep(2) # time delay before the next command is sent
	
	data = "Green" #set data command to Green 
	client_socket.sendto(data, address) #send command to the arduino
	try:
		rec_data, addr = client_socket.recvfrom(2048) # read data from arduino
		print rec_data #print data recieved from the arduino
	except:
		pass 
		
	time.sleep(2) # time delay before the next command is sent
	
