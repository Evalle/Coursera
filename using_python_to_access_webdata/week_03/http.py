import socket

message = 'GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n'
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(('www.pythonlearn.com', 80))
mysock.send(message.encode('utf-8'))

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode('utf-8'))
mysock.close()
