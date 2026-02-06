##Importamos la libreria GPIO que nos permite controlar los puertos GPIO
import RPi.GPIO as GPIO
import time

##Definimos el modo BCM que nos permite utilizar los numeros de pines GPIO
GPIO.setmode(GPIO.BCM)

##Definimos pines de entrada y salida
GPIO.setup(17, GPIO.OUT)  #LED Amarillo
GPIO.setup(27, GPIO.IN)  #Sensor de movimiento
GPIO.setup(22, GPIO.OUT)  #LED Rojo
GPIO.setup(10, GPIO.OUT)  #Zumbador



mov=0
clave = 1234

while True :
	if GPIO.input(27) == True:
		mov = mov+1
		time.sleep(1)
		print (mov)
	else :
		print ("No detecta nada")
		time.sleep(1)

	if mov == 1:
		GPIO.output(17, True)
		#time.sleep(1)
	elif mov == 2:
		GPIO.output(17, False)
		GPIO.output(22, True)
		#time.sleep(1)
	elif mov == 3:
		GPIO.output(22, False)
		GPIO.output(10, True)
		time.sleep(5)
		contraseña =int(input("Introduce la clave para desactivar la alarma: "))

		if clave != contraseña :
			print ("AVISANDO A LA POLICIA")
			mov = 0

		elif clave == 1234 and clave == contraseña :
			print ("ALARMA DESACTIVADA")
			GPIO.output(10, False)
			mov=0
			
		else  :
			print ("ALARMA DESACTIVADA")
			GPIO.output(10, False)
			mov=0