import random
def run():
	volver_a_jugar = True
	r = True
	while volver_a_jugar == True:
		
		rand_number = random.randint(0,20)
		attempts =  5
		while attempts != 0:
			user_number = int(input("Introduce un numero entero del 0 al 20: "))
			if user_number == rand_number:
				print("adivinaste")
				break
			else:
				if user_number > rand_number:
					print("El numero ingresado es menor")
				elif user_number < rand_number:
					print("El numero ingresado es mayor ")
				attempts = attempts - 1
				print("te quedan {} intentos".format(attempts))

			if(attempts == 0):
				print("te quedaste sin intentos")
				break
		while r:
			reintentar = str(input("Quieres volver a jugar /Si ,No: "))
			if reintentar == "No":
				volver_a_jugar = False
				print("Gracias por jugar")
				r = False
				break
			elif reintentar == "Si":
				volver_a_jugar = True
				r = False
			else:
				print("Debes ingresar Si o No")
				r = True

if __name__ == "__main__":
	run()

