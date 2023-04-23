import socket



def calculate(data):
	if ('+' in data):
		op1 = data.split('+')[0]
		op2 = data.split('+')[1]
		# print(int(op1))
		if( op1.isdigit() and op2.isdigit() ):
			result = int(op1) + int(op2)
		else:
			return  "invalid input..."
		
	elif ('*' in data):
		op1 = data.split('*')[0]
		op2 = data.split('*')[1]
		if( op1.isdigit() and op2.isdigit() ):
			result = int(op1) * int(op2)
		else:
			return  "invalid input..."
			
	elif ('/' in data):
		op1 = data.split('/')[0]
		op2 = data.split('/')[1]
		if( op1.isdigit() and op2.isdigit() ):
			result = int(op1) / int(op2)
		else:
			return  "invalid input..."
			
	elif ('-' in data):
		op1 = data.split('-')[0]
		op2 = data.split('-')[1]
		if( op1.isdigit() and op2.isdigit() ):
			result = int(op1) - int(op2)
		else:
			return  "invalid input..."
	else:
		return "IDK"

	return data + " = " + str(result)


HOST = "127.0.0.1"
PORT = 40000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM )	as sock:
	sock.bind((HOST, PORT))
	while True:
		sock.listen()
		connection, address = sock.accept()
		with connection:
			print(f"connection from :{address}")
			while True:
				data = connection.recv(1024)
				data = data.decode('utf-8')
				if (data in ['q', 'Q', "exit", "quit"]):
					connection.sendall(b"closed")
					connection.close()
					break
				result = calculate(data)
				connection.sendall(str(result).encode('utf-8'))