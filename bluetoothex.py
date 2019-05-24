from bluetooth import *
# Create the client socket
client_socket=BluetoothSocket( RFCOMM )
client_socket.connect(("98:D3:31:FD:9E:A3", 1))
while True:
        #msg = input("Send : ")
        #client_socket.send(msg)
        data = client_socket.recv(1024)        
        print ("receive : [%s]" % data)
print ("Finished")
client_socket.close()
