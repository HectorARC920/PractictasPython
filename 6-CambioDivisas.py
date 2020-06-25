
def foreing_exchange_calulator(ammount,type_of_divisa):
	rate = 0
	if type_of_divisa == "COL":
	    rate = 163.17
	elif type_of_divisa == "CAN":
		rate = 0.058
	elif type_of_divisa == "US":
		rate = 0.041
	else:
		return print("La divisa no se encuentra en nuestra base de datos o esta escrita mal")

	return rate * ammount

def run():
	print("Calculadora de Divisas")
	print("Convierta pesos mexicanos a otra moneda")
	print("")
	type_of_divisa = str(input("ingrese la moneda a la que desea cambiar, opciones(COL,US,CAN):"))
	ammount = float(input("Ingrese la cantidad que va a convertir"))

	result = foreing_exchange_calulator(ammount,type_of_divisa)

	print("${} pesos mexicanos son ${} ".format(ammount,result) + type_of_divisa)
	print("")


if __name__ == "__main__":
	run()