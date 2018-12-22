import socket
import threading

def function(s):
    while True:
        data = s.recv(1024)
        data = data.decode()
        input_one = data.split(' ')
        if input_one[1] == "SUCCESS":
            # print(data)
            s.close()
        print(data)

def main():
    host = '127.0.0.1'
    port = 5000


    sockobj = socket.socket()
    sockobj.connect((host, port))

    threading.Thread(target = function, args = (sockobj, )).start()
    while True:
        data = input()
        sockobj.send(data.encode())
    sockobj.close()

if __name__ == '__main__':
        main() 
