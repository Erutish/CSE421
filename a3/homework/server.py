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
                salary=0
                hour=int(msg)
                if hour<=40:
                    salary=hour*200
                    conn.send(f"Salary is {salary} Taka".encode(FORMAT))
                elif hour>40:
                    salary=8000+(hour-40)*300
                    conn.send(f"Salary is {salary} Taka".encode(FORMAT))
                    

conn.close()
