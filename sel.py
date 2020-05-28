import sys
import time
import numpy
import win32gui

from selenium import webdriver
from pynput.keyboard import Key, Controller
from selenium.common.exceptions import NoSuchElementException

def main():
	Run_bot()

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

			time.sleep(2.5)		

			Find_Saldo = browser.find_element_by_xpath('//tr[@id="1"][@class="jqgrow"]/td[5]')
			Saldo = Find_Saldo.text

			time.sleep(7.5)	

			Salir = browser.find_element_by_xpath('//a[@id="salir"]')	
			Salir.click()

			time.sleep(3.5)

			print(Saldo)

		except Exception as ex:
			print(ex)
			continue
			
if __name__ == "__main__":
	main()