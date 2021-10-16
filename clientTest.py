import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('computer', 8080))
client.send('I am CLIENT'.encode())
from_server = client.recv(4096).decode()
client.send('stop'.encode())
client.close()
print(from_server)

