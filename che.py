import socket
import time
PORT=8888
server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address=('10.2.47.167',PORT)
server_socket.bind(address)
server_socket.settimeout(10)
while True:
    try:
        now=time.time()
        receive_data,client = server_socket.recvfrom(1024)
        #print(receive_data.decode())
        t=receive_data.decode()
        #print(t)
        if(t=='0'):
            print("stop")
        if(t=='1'):
            print("run")
        if(t=='2'):
            print("back")
        if(t=='3'):
            print("left")
        if(t=='4'):
            print("right")
    except socket.timeout:
        print("time out")

