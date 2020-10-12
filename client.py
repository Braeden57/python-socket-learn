import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = '169.254.95.158'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(ADDR)
    def send(msg):
        message = msg.encode(FORMAT)
        msg_length = len(msg)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)

    print('Type "disconnect" to disconnect from the server.')
    while True:
        x = input('>')
        if x.upper() == 'DISCONNECT':
            send(DISCONNECT_MESSAGE)
            break
        else: send(x)
except ConnectionRefusedError: print('Unable to Connect to server.\nThe Server may be down or is unavailable.')
