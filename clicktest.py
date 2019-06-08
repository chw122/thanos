import pymysql
import pyautogui
import sys
import time


db = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='emg_db', charset='utf8')
errorCode=True
sqlData=""
while True:
	with db.cursor() as cursor:
		#sql = """INSERT INTO emg_value(value1, value2, time) VALUES(""" + sqlData + """,NOW());"""
		#cursor.execute(sql)
		#db.commit()
		
		sql2="""SELECT value1 from emg_value order by num desc limit 1"""
		cursor.execute(sql2)
		rows = cursor.fetchall()
		for row in rows:				
			print(row[0])
		if(int(row[0])>600):					#팔을 펼때	
			pyautogui.click(100,100)
			#pyautogui.press('enter')		
			#pyautogui.press('backspace')	#백스페이스 누르기

		sql3="""SELECT value2 from emg_value order by num desc limit 1"""
		cursor.execute(sql3)
		rows = cursor.fetchall()
		for row in rows:				
			print(row[0])
		
		if(int(row[0])>700):				#손 튕굴때
			#pyautogui.click(100,100)
			#time.sleep(100)
			#pyautogui.press('enter')		#마우스좌표에 클릭
			pyautogui.press('backspace')
	
	time.sleep(500)

client_socket.close()
