
def binary_search(numbers,number_to_find,low,high):

	if low > high:
		return False
	mid = int((low+ high) / 2)

	if numbers[mid] == number_to_find:
		return True

	elif numbers[mid] > number_to_find:
		return binary_search(numbers,number_to_find,low, mid -1)
	else:
		return binary_search(numbers,number_to_find,mid+1,high)


if __name__ == "__main__":
	numbers = [6,8,9,4,54,12,25,36,27,29,27,16,27,59,12]
	numbers.sort()
	number_to_find = int(input("Ingresa un numero: "))
	result = binary_search(numbers,number_to_find,0,len(numbers)-1)
	if result == True:
		print("El Numero si esta en la lista")

	else:
		print("El numero no esta en la lista")
