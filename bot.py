import sys
import time
import numpy
import win32gui

from selenium import webdriver
from pynput.keyboard import Key, Controller
from selenium.common.exceptions import NoSuchElementException

#NEW CODE

import pymssql  

import json
import requests

from flask import Flask
from flask import request
from flask import Response

token = '1113454307:AAG0zEgg5AL5cS2KE3HQY_-QAdDr8ZhQ0ok'
app = Flask(__name__)

def message(message):
	chat_id = message['message']['chat']['id']
	txt = message['message']['text']

	return chat_id, txt

def send_message(chat_id, text='Check'):
	url=f'https://api.telegram.org/bot{token}/sendMessage'
	bank_mov = {'chat_id':chat_id, 'text':text}

	send = requests.post(url, bank_mov)
	return send

@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		msg = request.get_json()
		chat_id, txt = message(msg)

		# print(chat_id)

		if chat_id != 749172013:
			send_message(chat_id, 'Acceso No Permitido')
		else:
			if txt == 'Saldo':
				send_message(chat_id, 'Su Solicitud Esta Siendo Procesada')			
				Money = Run_bot()
				# Run_bot()
				send_message(chat_id, Money)	
			elif txt == '':
				pass
			else:
				Cost, Cant, Descp = Connect_SG(txt)
				Product = 'Producto: ' + Descp + '\n' + 'Precio: ' + str(Cost) + '\n' + 'Stock: ' + str(Cant)

				send_message(chat_id, Product)
				# send_message(chat_id, 'Palabra Fuera Del Diccionario')
		
			# j = open('Telegram.json', 'w')
			# j.write(json.dumps(msg))
			# j.close()
		return Response('OK', status=200)
	else:
		return '<h1>TODO OK</h1>'

#########

# https://api.telegram.org/bot1113454307:AAG0zEgg5AL5cS2KE3HQY_-QAdDr8ZhQ0ok/getMe ## TEST OK
# https://api.telegram.org/bot1113454307:AAG0zEgg5AL5cS2KE3HQY_-QAdDr8ZhQ0ok/getUpdates ## SEND OK
# https://api.telegram.org/bot1113454307:AAG0zEgg5AL5cS2KE3HQY_-QAdDr8ZhQ0ok/sendMessage?chat_id=749172013&text=Automatic Response
# https://api.telegram.org/bot1113454307:AAG0zEgg5AL5cS2KE3HQY_-QAdDr8ZhQ0ok/setwebhook?url=https://plane.serveo.net/
# https://api.telegram.org/bot1113454307:AAG0zEgg5AL5cS2KE3HQY_-QAdDr8ZhQ0ok/deletewebhook?url=https://plane.serveo.net/
# https://api.telegram.org/bot1113454307:AAG0zEgg5AL5cS2KE3HQY_-QAdDr8ZhQ0ok/getWebhookInfo?url=https://pungo.serveo.net/

keyboard = Controller()  #Create controller

# def main():
# 	Run_bot()
# 	Connect_SG()

def Run_bot():
	#browser = webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver.exe")
	#browser = webdriver.PhantomJS(executable_path="C:/PhantomJS/bin/phantomjs.exe")
	browser = webdriver.Firefox(executable_path="C:/GeckoDriver/geckodriver.exe")
	#browser = webdriver.Edge(executable_path="C:/EdgeDriver/driver.exe")
	browser.get("https://hb.redlink.com.ar/bna/login.htm")

	time.sleep(1.5)
	browser.maximize_window()
	time.sleep(2.5)

	banks_list = ['Nacion']

	for bank in banks_list:
		try:

			user_name = browser.find_element_by_xpath('//input[@id="usuario"]')
			user_name.send_keys('Nicohome')

			time.sleep(2.5)

			user_button = browser.find_element_by_xpath('//a[@class="btn_ingresar"]')
			user_button.click()

			time.sleep(2.5)	
			
			password = browser.find_element_by_xpath('//input[@id="clave"]')
			password.send_keys('12home.1')	

			time.sleep(2.5)	
	
			user_button.click()

			time.sleep(5.5)		

			Find_Saldo = browser.find_element_by_xpath('//tr[@id="1"][@class="jqgrow"]/td[5]')
			Saldo = Find_Saldo.text

			time.sleep(1.5)	

			Salir = browser.find_element_by_xpath('//a[@id="salir"]')	
			Salir.click()

		# except Exception as ex:
		except:
			Saldo = 'Error Al Obtener El Saldo'

	return Saldo


def Connect_SG(Producto):

	try:
		#conn = pymssql.connect(server='192.168.1.200:1433.database.windows.net', user='atila', password='atila', database='Sudeste770')  
		conn = pymssql.connect(server='198.50.20.36:1433.database.windows.net', user='atila', password='atila', database='Sudeste770')  
		cursor = conn.cursor()  
		cursor.execute("SELECT * FROM Productos WHERE CODPRODUCTO ='" + Producto + "'")  
		row = cursor.fetchall() 
		Costo = row[0][14]
		Stock = row[0][20]
		Descripcion = row[0][3]
	except:
		Costo = '-'
		Stock = '-'
		Descripcion = '-'

	return Costo, Stock, Descripcion

if __name__ == "__main__":
	app.run(debug=True)	
    # main()

