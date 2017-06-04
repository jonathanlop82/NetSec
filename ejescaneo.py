import socket
s = socket.socket()
s.connect(('192.168.2.2', 22))
s.send('Primal Security n')

banner = s.recv(1024)
print banner
