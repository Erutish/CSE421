import socket

HEADER=16
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())  # Server IP address
ADDR=(SERVER,PORT)
FORMAT='UTF-8'
DISCONNECT_MESSAGE = "End"

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #-->IP4 address,TCP
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length +=b' '*(HEADER-len(send_length)) # padding
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


connected=True

while connected:
    input_message=input("Please enter your Hours: ")
    if input_message!="I'm done":
        send(input_message)
    else:
        connected=False
        send(DISCONNECT_MESSAGE)