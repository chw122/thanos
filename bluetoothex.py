from bluetooth import *
import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='djawleh', db='emg_db', charset='utf8')

# Create the client socket
client_socket=BluetoothSocket( RFCOMM )
client_socket.connect(("98:D3:31:FD:9E:A3", 1))
while True:
	#msg = input("Send : ")
	#client_socket.send(msg)
	data = client_socket.recv(1024)
	data2 = client_socket.recv(1024)
	#if(data[:1}=='/')	
	sqlData = data.decode(encoding="utf-8") + data2.decode(encoding="utf-8")
	print (sqlData)

	with db.cursor() as cursor:
		sql = """INSERT INTO emg_value(value, time) VALUES(""" + sqlData + """,NOW());"""
		cursor.execute(sql)
		db.commit()
print ("Finished")
client_socket.close()
