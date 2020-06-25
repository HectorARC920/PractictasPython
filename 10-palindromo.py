#forma 1 de hacerlo
def palindrome(word):
	reversed_letters = word[::--1]
	if reversed_letters.uper() == word.uper():
		return True
	return False
#forma 2 de hacerlo
def palindrome2(word):
	reversed_letters = []
	for letter in word:
		reversed_letters.insert(0,letter)
	reversed_word = "".join(reversed_letters)

	if word == reversed_word:
		return True
	return reversed_word


if __name__ == "__main__":
	word = str(input("Ingresa una palabra y te dire si es un palindromo: "))
	result = palindrome2(word)
	if result == True:
		print("Tu palabra es un palindromo")
	else:
		print("Tu palabra no es un palindromo")