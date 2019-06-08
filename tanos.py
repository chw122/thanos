from bluetooth import *
import pymysql
import pyautogui
import sys
import time


db = pymysql.connect(host='localhost', port=3306, user='root', passwd='12345', db='emg_db', charset='utf8')
errorCode=True
sqlData=""
while True:
	# Create the client socket
	
	client_socket=BluetoothSocket( RFCOMM )
	client_socket.connect(("98:D3:31:FD:9E:A3", 1))
	
	while True:
		data = client_socket.recv(1024)
		data2 = client_socket.recv(1024)

		print(data.decode(encoding="utf-8"))
		if(data.decode(encoding="utf-8")=="/"):
			sqlData =  data2.decode(encoding="utf-8")

			with db.cursor() as cursor:
				sql = """INSERT INTO emg_value(value1, value2, time) VALUES(""" + sqlData + """,NOW());"""
				cursor.execute(sql)
				db.commit()
				
				sql2="""SELECT value2 value1 from emg_value order by num desc limit 1"""
				cursor.execute(sql2)
				rows = cursor.fetchall()
				for row in rows:				
					print(row[0])
					print(row[1])
				
				
				if(int(row[1])>600)					#팔을 펼때	
					pyautogui.click(100,100)
					pyautogui.press('enter')		
					#pyautogui.press('backspace')	#백스페이스 누르기
				elif(int(row[0])>600):				#손 튕굴때
					pyautogui.click(100,100)
					time.sleep(100)
					pyautogui.press('enter')		#마우스좌표에 클릭
				

		else:
			print("data error!!")
			client_socket.close()
			time.sleep(10)
			break
		
		
		print ("insert : "+sqlData)

client_socket.close()