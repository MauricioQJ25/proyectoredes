'''
    Simple udp socket server
'''
 
import socket
import sys
from twython import Twython
CONSUMER_KEY = 'FJsJbyQOnK7Z06OwyWcXkoGbI'
CONSUMER_SECRET = 'AP8ElOgND8VBwEcjGlyAw14nJX9qDTnIjvK5JCFpLMxZt0CAqi'
ACCESS_KEY = '116272725-8BjUdjcUMgaT5Fw7THCoboK8sPYTe1jPW1xLtY1C'
ACCESS_SECRET = 'fnSxdpabFZqaCFtWMETJ78jqdJJkmZZxtotgbQkGvwXoq'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
 
 
# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#now keep talking with the client
while 1:
    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    #api.update_status(status=data)
    data = d[0]
    addr = d[1]
    api.update_status(status=data)

     
    if not data: 
        break
     
    reply = 'OK...' + data
     
    s.sendto(reply , addr)
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
     
s.close()
