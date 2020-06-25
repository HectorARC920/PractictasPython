KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
    " ": " ",
}

def cypher(message):
    #Forma 2 de criptar
    words = message.split(" ")
    cypher_message = []
    for word in words:
        cypher_word = ""
        for letter in word:
            cypher_word += KEYS[letter]

        cypher_message.append(cypher_word)
    return " ".join(cypher_message)

    """
    #Forma Num 1 de criptar
	cypher_message = ""
	for letter in message:
		cypher_message += KEYS[letter]
	return cypher_message
    """

def dechyper(message):
    #Forma 2 de criptar
    words = message.split(" ")
    decyphed_words = [] 
    for word in words:
        dechyper = ""
        for letter in word:
            for key,value in KEYS.items():
                if letter == value:
                    dechyper += key
                    break
        decyphed_words.append(dechyper)
    return " ".join(decyphed_words)
    """
    #Forma 1 de cifrar
	decyphed_message = ""
	for letter in message:
		for key,value in KEYS.items():
			if value == letter:
				decyphed_message += key
				break
	return decyphed_message
    """

def run():
	while True:
	
		command = str(input("""Bienvenido a criptografia miji que desea hacer?

	[c]riptar
	[d]ecriptar
	[s]alir
    ---*---*---*---*---*---*---*---*---*---*: """))
		if command == "c":
			message = str(input("Ingresa tu mensaje a criptar: "))
			result = cypher(message)
			print("El mensaje cifrado es: {}".format(result))
		elif command == "d":
			message = str(input("Ingresa tu mensaje a decriptar"))
			result = dechyper(message)
			print("EL mensaje decifrado es : {}".format(result))
		elif command == "s":
			print("Salgase alv")
			break
if __name__ == "__main__":
	run()