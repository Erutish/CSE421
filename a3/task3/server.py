import socket
import  threading

HEADER=16
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())  # Server IP address
ADDR=(SERVER,PORT)
FORMAT='UTF-8'
DISCONNECT_MESSAGE = "End"

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #-->IP4 address,TCP
server.bind(ADDR)

def handle_client(conn,addr):
    print("Connected with client\n")
    connected=True
    while connected:
        msg_lenght=conn.recv(HEADER).decode(FORMAT)
        if msg_lenght:
            msg_lenght=int(msg_lenght)
            msg=conn.recv(msg_lenght).decode(FORMAT)
            if msg=="DISCONNECT_MESSAGE":
                connected=False
                conn.send("Goodbye".encode(FORMAT))
                print("Client Disconnected")
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

def start():
    server.listen()
    print(f" [LISTENING] Server is listening....")
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"Total clients connected currently: {threading.active_count()-1}")

start()

