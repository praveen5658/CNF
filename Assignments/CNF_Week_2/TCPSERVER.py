import socket
import threading
import csv
clients = list()
def function(c):
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        rollnumber = ""
        while True:
            data = c.recv(1024)
            data = data.decode()
            input_one = data.split(' ')
            cou = 0
            if input_one[0] == "MARK-ATTENDANCE":
                for row in csv_reader:
                    if str(row[0]) == str(input_one[1]):
                        cou = 1
                        rollnumber = str(row[0])
                        c.send(("SECRETQUESTION "+str(row[1])).encode())
                        break
                if cou == 0:
                    c.send("ROLLNUMBER-NOTFOUND".encode())
            if (input_one[0]) == "SECRETANSWER":
                # print(input_one[1])
                for row in csv_reader:
                    if str(row[0]) == rollnumber:
                        # print(rollnumber)
                        if str(row[2]) == str(input_one[1]):

                            c.send("ATTENDENCE SUCCESS".encode())
                        else: 
                            c.send(("SECRETQUESTION-"+str(row[1])).encode())
                            break

        

def main():
    totalconnec = int(input("Please provide number of users: "))
    host = '127.0.0.1'
    port = 5000
    sockobj = socket.socket()
    sockobj.bind((host, port))
    sockobj.listen(1)
    for i in range(0, totalconnec):
        connec, addr = sockobj.accept()
        print("Connection established with " + str(addr))
        clients.append(connec)
        thread = threading.Thread(target = function, args = (clients[i],))
        thread.start()
    sockobj.close()

if __name__ == '__main__':
    main()