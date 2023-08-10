from flask import *
import os
import base64
import mysql.connector


class users(object):
	def __init__(self):
		print("this is user Init")

	_conn = mysql.connector.connect(user='root',password='',host='localhost',database='mp_fits',port=3306)
	_conn.autocommit = True
	_crsr = _conn.cursor()

	def Login(self,email,password):
		self.email = email.lower()
		print(self.email)
		self.password = password
		print(self.password)

		self._crsr.execute("SELECT * FROM user_details WHERE email = %s ;",[self.email])
		Data = self._crsr.fetchall()	
		print(Data)
		print(type(Data[0][3]))
		print(type(self.password))
		for data in Data :
			if data[2] == self.email and data[3] == self.password:
				session['username'] = data[1]
				session['user_id'] = data[0]
				session['user_email'] = data[2]								
				session['loggedIn'] = True				
				return True
		else:
			return False
	
	def SingleUser(self):
		self.username = session['username']
		self._crsr.execute("SELECT * FROM user_details where username = %s ;",[self.username])
		user = self._crsr.fetchall()
		return user

	def Register(self,username,email,user_pass):
		self.email = email.lower()   	
		self.username = username
		self.user_pass = user_pass

		self._crsr.execute("SELECT * FROM user_details where email = %s;",[self.email])
		Data = self._crsr.fetchall()
		count = 0
		print(Data)
		for data in Data :
			if data[2] == email:
				count = 1
				break
		if count == 1:
			return False
		else:			
			self._crsr.execute("INSERT INTO user_details(username,email,password,createdon,updatedon) VALUES(%s,%s,%s,now(),now())",(self.username,self.email,self.user_pass))
			return True

	def get_trainner(self):
    	
		self._crsr.execute("SELECT * FROM trainer_details")
		trainer = self._crsr.fetchall()
		return trainer
    		

