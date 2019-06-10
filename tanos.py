from bluetooth import *	#������� ����� ����ϱ����� ���̺귯��
import pymysql		#�����ͺ��̽��� ����ϱ����� ���̺귯��
import pyautogui		#Ű���� ���콺 ������� ���� ���̺귯��
import sys
import time		#�ð� ������ ���� ���̺귯��

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='djawleh', db='emg_db', charset='utf8')
#�����ͺ��̽� ������ ���� �����ϴ� �κ�
sqlData=""		#if�� �ȿ� ���� ���� ����
count=10			#���� �Է��� ���� ���� ����
while True:		#������� ������ �����ϴ� �ݺ���
	
	client_socket=BluetoothSocket( RFCOMM )		#Ŭ���̾�Ʈ ���� ����
	client_socket.connect(("98:D3:31:FD:9E:A3", 1))		#�ش� ������� ���� ����
	
	while True:					#������� ������ �����ϴ� �ݺ���
		data = client_socket.recv(1024)					
		#Ŭ���̾�Ʈ ���Ͽ� ������� ��� ������ ������ ��� data�� �����Ѵ�. �� ���� ��� ���ڸ� ���� ���� �޾ƿ´�.
		data2 = client_socket.recv(1024)				
		#Ŭ���̾�Ʈ ���Ͽ� ������� ��� ������ ������ ��� data2�� �����Ѵ�. 
		#�� ���� data�� ���޵� ���� ������ ������ ���� �޾ƿ´�.

		#print(data.decode(encoding="utf-8"))#�������� ��ȿ ���� �Ѿ������ Ȯ��
		if(data.decode(encoding="utf-8")=="/"):
		#���� �����͸� utf-8�� ���ڵ��Ͽ� ��������, �ش� ���� �Ǻ����� '/'���� Ȯ���Ͽ� ��ȿ������ �Ǻ��Ѵ�.
			sqlData =  data2.decode(encoding="utf-8")
			# ��ȿ ������ ���� ���ڵ��Ͽ� ������ �����Ѵ�. �ش� ���� �� �����Ͱ� ','�� ���� �����ִ�.
			with db.cursor() as cursor:			#�����ͺ��̽��� Ŀ���� ������
				sql = """INSERT INTO emg_value(value1, value2, time) VALUES(""" + sqlData + """,NOW());"""
				#�����ִ� �����͸� ���̺� �ð��� �Բ� �����ϴ� ������ ������ ����.
				cursor.execute(sql)			#Ŀ���� ����� ������ ����.
				db.commit()			#�����ͺ��̽��� ������Ʈ
				
				#�����ͺ��̽� �� �������� ����, ����, �ֻ����ϳ��� Ʃ�ø� ������(���� �������� �� Ʃ��)
				sql2="""SELECT value1 from emg_value order by num desc limit 1"""
				#�����ͺ��̽� �� �������� ����, ����, �ֻ����ϳ��� Ʃ�ø� ������(���� �������� �� Ʃ��)
				cursor.execute(sql2)		#Ŀ���� ����� ������ ����.
				rows = cursor.fetchall()		#Ŀ���� �����͸� rows�� ��� �ִ´�.
				for row in rows:			#�ټ��� ������ ��				
					print(row[0])		#ù��° ������(�ϳ��ۿ� ����.)-��ȣ�� �׿��ִ�.
				
				if(int(row[0])>500 and count>5):			#���� �
					count=0					#�����Է� ����
					pyautogui.press('backspace')			#�齺���̽� ������


				sql3="""SELECT value2 from emg_value order by num desc limit 1"""
				#�����ͺ��̽� �� �������� ����, ����, �ֻ����ϳ��� Ʃ�ø� ������(���� �������� �� Ʃ��)
				cursor.execute(sql3)		#Ŀ���� ����� ������ ����.
				rows = cursor.fetchall()		#Ŀ���� �����͸� rows�� ��� �ִ´�.
				for row in rows:			#�ټ��� ������ ��				
					print(row[0])		#ù��° ������(�ϳ��ۿ� ����.)-��ȣ�� �׿��ִ�.
				
				if(int(row[0])>150 and count>5):			#�� ƨ����
					count=0					#�����Է� ����.
					pyautogui.click(100,100)			# x=100,y=100�� ��ġ�� Ŭ�� ����.

		else:	#���� �����Ͱ� �и��ų� �����Ǿ� ��ȿ���� �ƴ� ���
			print("data error!!")		#������ ���� ��ȣ.
			client_socket.close()	#������� Ŭ���̾�Ʈ ������ �ݴ´�.
			time.sleep(1)		#������ �ݱ⵵�� �����ð��� �д�.
			break			#������ ���̹Ƿ� �ݺ����� �����ϰ� ������� ���ۺκ����� �ǵ��ư�.
				
		print ("insert : "+str(count))	#������ ������ ���� ����.
		count+=1		#���� �Է� �������� ����

client_socket.close()				#Ŭ���̾�Ʈ ���� �ݱ�.