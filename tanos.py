from bluetooth import *	#블루투스 모듈을 사용하기위한 라이브러리
import pymysql		#데이터베이스를 사용하기위한 라이브러리
import pyautogui		#키보드 마우스 입출력을 위한 라이브러리
import sys
import time		#시간 조정을 위한 라이브러리

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='djawleh', db='emg_db', charset='utf8')
#데이터베이스 정보를 통해 연결하는 부분
sqlData=""		#if문 안에 사용될 변수 선언
count=10			#연속 입력을 막기 위한 변수
while True:		#블루투스 연결을 실행하는 반복문
	
	client_socket=BluetoothSocket( RFCOMM )		#클라이언트 소켓 생성
	client_socket.connect(("98:D3:31:FD:9E:A3", 1))		#해당 블루투스 기기와 연결
	
	while True:					#블루투스 연결중 실행하는 반복문
		data = client_socket.recv(1024)					
		#클라이언트 소켓에 블루투스 기기 응답이 들어오는 경우 data에 저장한다. 이 값은 대게 한자릿 수만 먼저 받아온다.
		data2 = client_socket.recv(1024)				
		#클라이언트 소켓에 블루투스 기기 응답이 들어오는 경우 data2에 저장한다. 
		#이 값은 data에 전달된 값을 제외한 나머지 값을 받아온다.

		#print(data.decode(encoding="utf-8"))#정상적인 유효 값이 넘어오는지 확인
		if(data.decode(encoding="utf-8")=="/"):
		#받은 데이터를 utf-8로 디코드하여 가져오고, 해당 값이 판별값인 '/'인지 확인하여 유효값인지 판별한다.
			sqlData =  data2.decode(encoding="utf-8")
			# 유효 데이터 값을 디코드하여 변수에 저장한다. 해당 값은 두 데이터가 ','와 같이 묶여있다.
			with db.cursor() as cursor:			#데이터베이스의 커서를 가져옴
				sql = """INSERT INTO emg_value(value1, value2, time) VALUES(""" + sqlData + """,NOW());"""
				#묶여있는 데이터를 테이블에 시간과 함께 삽입하는 구문을 변수에 저장.
				cursor.execute(sql)			#커서에 저장된 쿼리문 실행.
				db.commit()			#데이터베이스에 업데이트
				
				#데이터베이스 상에 순번으로 정렬, 역순, 최상위하나의 튜플만 가져옴(가장 마지막에 들어간 튜플)
				sql2="""SELECT value1 from emg_value order by num desc limit 1"""
				#데이터베이스 상에 순번으로 정렬, 역순, 최상위하나의 튜플만 가져옴(가장 마지막에 들어간 튜플)
				cursor.execute(sql2)		#커서에 저장된 쿼리문 실행.
				rows = cursor.fetchall()		#커서의 데이터를 rows에 모두 넣는다.
				for row in rows:			#다수의 데이터 중				
					print(row[0])		#첫번째 데이터(하나밖에 없다.)-괄호로 쌓여있다.
				
				if(int(row[0])>500 and count>5):			#팔을 펼때
					count=0					#연속입력 방지
					pyautogui.press('backspace')			#백스페이스 누르기


				sql3="""SELECT value2 from emg_value order by num desc limit 1"""
				#데이터베이스 상에 순번으로 정렬, 역순, 최상위하나의 튜플만 가져옴(가장 마지막에 들어간 튜플)
				cursor.execute(sql3)		#커서에 저장된 쿼리문 실행.
				rows = cursor.fetchall()		#커서의 데이터를 rows에 모두 넣는다.
				for row in rows:			#다수의 데이터 중				
					print(row[0])		#첫번째 데이터(하나밖에 없다.)-괄호로 쌓여있다.
				
				if(int(row[0])>150 and count>5):			#손 튕굴때
					count=0					#연속입력 방지.
					pyautogui.click(100,100)			# x=100,y=100인 위치에 클릭 실행.

		else:	#받은 데이터가 밀리거나 생략되어 유효값이 아닌 경우
			print("data error!!")		#데이터 에러 신호.
			client_socket.close()	#블루투스 클라이언트 소켓을 닫는다.
			time.sleep(1)		#소켓이 닫기도록 지연시간을 둔다.
			break			#비정상 값이므로 반복문을 종료하고 블루투스 시작부분으로 되돌아감.
				
		print ("insert : "+str(count))	#삽입한 데이터 열람 목적.
		count+=1		#연속 입력 방지변수 증가

client_socket.close()				#클라이언트 소켓 닫기.