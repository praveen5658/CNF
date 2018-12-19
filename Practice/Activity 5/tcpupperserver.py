import socket

def Main():
	host = '127.0.0.1'
	port = 5868

	s = socket.socket()
	s.bind((host, port))

	s.listen(1)

	c, addr = s.accept()

	print("connection from : " + str(addr))

	while True:
		data = c.recv(1024).decode()
		if not data:
			break
		print("message from client : " + str(data))
		data = str(data).upper()
		print("message after converting to Upper : " + str(data))
		c.send(data.encode())
	print("Connection closed!")
	c.close()

if __name__ == "__main__":
	Main()