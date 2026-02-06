##Importamos la libreria GPIO que nos permite controlar los puertos GPIO
import RPi.GPIO as GPIO


##Definimos el modo BCM que nos permite utilizar los numeros de pines GPIO
GPIO.setmode(GPIO.BCM)

##Definimos los pines de entrada y salida
GPIO.setup(17, GPIO.OUT)  #LED Amarillo
GPIO.setup(27, GPIO.IN)   #Sensor de movimiento
GPIO.setup(22, GPIO.OUT)  #LED Rojo
GPIO.setup(10, GPIO.OUT)  #Zumbador


mov=0

while True :
	if GPIO.input(27) == True:
		mov = mov+1
		print (mov)
	else :
		print ("No detecta nada")

	if mov == 1:
		GPIO.output(17, True)
	
	elif mov == 2:
		GPIO.output(17, False)
		GPIO.output(22, True)
		
	elif mov == 3:
		GPIO.output(22, False)
		GPIO.output(10, True)
		


