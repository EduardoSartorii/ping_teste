import os
import sys

os.system('cls')
def pinga_tudo():
	try:
		print('[!] Estamos realizando o teste de ping... [!] \n\n')
		ping = os.system('ping ' + sys.argv[1])
		if ping == 0:
			os.system('cls')
			print('\n[!] Pingamos com sucesso [!]')
		elif ping == 1:
			os.system('cls')
			print('[!] Droga vamos reiniciar sua máquina [!]')
			os.system('shutdown -r -f')
	except IndexError:
		os.system('cls')
		print('\n[?] Necessário colocar um destino, exemplo: "samuel.py 192.168.112.1" [?]')
pinga_tudo()				
	


