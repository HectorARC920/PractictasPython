import random
def user_letter():
	letter = str.upper(str(input("Ingrese una letra mi brodi: ")))
	while len(letter) > 1:
		print("Solo debe igresar una letra perrin")
		letter = str.upper(input("Ingrese una letra mi brodi: "))
	return letter

def random_word():
	word_list = ["Leche","Chabo","Chocolate","Filantropo","Cacahuate","Juvenil","Computadora","Caca","Xbox","Correr"]
	word = str.upper(word_list[random.randint(0,len(word_list))-1])
	return word

def show_display(tries,hidden_word,used_letters):
	print(IMAGES[tries])
	print("")
	print(hidden_word)
	print("Las letras que has utilizado son: {}".format(used_letters[::1]))
	print("---*---*---*---*---*")

def run():
	word = random_word()
	hidden_word = ["-"] * len(word)
	tries = 0
	used_letters = []
	while True:
		show_display(tries,hidden_word,used_letters)
		current_letter = user_letter()
		used_letters.append(current_letter)
		letter_indexes = []

		for idx in range(len(word)):
			if current_letter == word[idx]:
				letter_indexes.append(idx)

		if len(letter_indexes) == 0:
			tries +=1

			if tries == 7:
				show_display(tries,hidden_word,used_letters)
				print("")
				print("PERDISTE :C")
				print("La palabra que estabas buscando era {}".format(word))
				break

		else:
			for idx in letter_indexes:
				hidden_word[idx] = current_letter

			letter_indexes = []
		try:
			hidden_word.index("-")
		except ValueError:
			print("")
			print("Felicidades, Ganaste la palabra es: {}".format(word))
			break




if __name__ == "__main__":
	print("BIENVENIDO AL JUEGO DEL AHORCADO")
	IMAGES = ["""
	+---+
	    |
	    |
	    |
	    |
	    |
	======""","""
	+---+
	0   |
	    |
	    |
	    |
	    |
	======""","""
	+---+
	0   |
	|   |
	    |
	    |
	    |
	======""","""
	+---+
	0   |
	|\  |
	    |
	    |
	    |
	======""","""
	+---+
	0   |
   /|\  |
	    |
	    |
	    |
	======""","""
	+---+
	0   |
   /|\  |
	|   |
	    |
	    |
	======""","""
	+---+
	0   |
   /|\  |
	|   |
	 \  |
	    |
	======""","""
	+---+
	0   |
   /|\  |
	|   |
   / \  |
	    |
	======"""]
	
	run()