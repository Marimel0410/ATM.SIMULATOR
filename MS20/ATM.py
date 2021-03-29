print ("Bienvenidos a su Cajero automatico")
estado = int (input ("¿Esta usted registrado ya ? (1.Si o 2.no )   " ))

import random as dr

Numeroclientenuevo = ["1234", 
"1255","6765","0988"]
 # a, Anexa
 #w, elimina 
import os 
Balance = 2000  


if estado == 2:
	print ("Usted debe registrarse")
	Archivo = open("Datos_Clientes.txt","w")
	Archivo.write("Clinte nuevo \n")
	nombre = input ("ingresa tu Nombre y Apellido\n")
	Archivo.write(nombre)
	print ()
	Pin = int(input("Ingresa tu PIN\n"))
	Archivo.write('Pin =% s' % Pin)
	Archivo.close()
	indice = dr.randint (0, len (Numeroclientenuevo) -1)
	nc = Numeroclientenuevo[indice]
	print ("Este es su numero de cuenta asignado:  ", nc)
	print (nombre , "  Bienvenido/a, usted fue registrado exitosamenre")
	print ("Para realizar alguna accion debe iniciar otra vez")
	
if estado == 1:
	user = input ("Ingresa tu nombre: ")
	try:
   	 Clave = int(input ("Ingresa tu PIN"))
	except TypeError:
   		print ("Debe escribir datos numericos")

print ("¿Que accion desea realizar?")
print (""" 
		1. Consultar Balance  
		2. Retirar 
		3. Transacción
		""")

accion = int(input("Ingrese una Acción  "))

if accion == 1:
	print ("Su balance actual es  ", Balance)
if accion == 2:
	K = int(input("Ingrese el monto a retirar"))
	r = Balance - K
	print ("Su balance actual es de: ", r)
if accion == 3:
	p = input ("Infrese el nombre y apellido de la persona")
	print ("La transferencia ha sido exitosa")
 
	


