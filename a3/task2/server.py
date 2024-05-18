import socket

HEADER=16
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())  # Server IP address
ADDR=(SERVER,PORT)
FORMAT='UTF-8'
DISCONNECT_MESSAGE = "End"

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #-->IP4 address,TCP
server.bind(ADDR)

server.listen()
print("[LISTENING] Server is listening...")
while True:
    conn,addr=server.accept()
    connected=True
    while connected:
        msg_lenght=conn.recv(HEADER).decode(FORMAT)
        if msg_lenght:
            msg_lenght=int(msg_lenght)
            msg=conn.recv(msg_lenght).decode(FORMAT)
            if msg=="DISCONNECT_MESSAGE":
                connected=False
                conn.send("Goodbye".encode(FORMAT))
            else:
                count=0
                for i in msg:
                    if i in "aeiouAEIOU" :
                        count+=1
                
                if count==0:
                    conn.send("Not enough vowels".encode(FORMAT))
                elif count<=2:
                    conn.send("Enough vowels I guess".encode(FORMAT))
                else:
                    conn.send("Too many vowels".encode(FORMAT))

conn.close()
