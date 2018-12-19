import socket

def Main():
	host = '127.0.0.1'
	port = 5868

	s = socket.socket()
	s.connect((host, port))

	message = input("Enter here : ")
	while message != 'q':
		s.send(message.encode())
		data = s.recv(1024).decode()
		print("Message received from server is : " + str(data))
		message = input("Enter here : ")
	s.close()

if __name__ == "__main__":
	Main()
