

def average_temps(temps):
	average = 0
	for temp in temps:
		sum_temps = average + temp
	sum_temps = average / len(temps)
	return sum_temps

if __name__ == "__main__":
	temps = [20,24,23,24,25,25,26]
	average = average_temps(temps)
	print("El promedio de la temperaturas es {}".format(average))