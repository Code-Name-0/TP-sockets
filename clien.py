import socket
import struct 
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 40000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.connect((SERVER_HOST, SERVER_PORT))
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
	while True:
		operation = input("###########################################################\noperation: ")	
		sock.sendall(operation.encode('utf-8'))
		data = sock.recv(1024).decode('utf-8')
		print(data)
		if(data == "closed"):
			break