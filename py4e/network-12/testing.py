import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('w3.org', 80))
command = ('GET https://www.w3.org/TR/PNG/iso_8859-1.txt HTTP/1.0\r\n\r\n'.encode())
mysocket.send(command)

while True:
  data = mysocket.recv(512)
  if(len(data) < 1):
    break
  print(data.decode())
mysocket.close()