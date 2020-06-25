#Este ejercicio consiste en determinar cual carácter es el 
#primero que no se repite en una secuencia de caracteres.
def first_not_repeating_char(char_sequence):

    #El diccionario en donde guardaremos las letras y
    #el num de veces que se repite
    seen_letters = {}

    #bucle for para hacer el conteo de las letras
    for letter in char_sequence:
        if letter not in seen_letters:
            seen_letters[letter] = 1
        else:
            seen_letters[letter] += 1  
    
    account = 0
    #bucle for para comparar el valor de las llaves
    for key, value in seen_letters.items():
        #si algun valor es igual a uno significa que solo se repitio una vez
        if value == 1:
            return key
        #si el valor es mayor a 1 el valor el caracter se repitio mas de una vez
        elif value > 1:
            account += 1
            #si la cuenta es igual al numero de elementos en el diccionario significa
            # que se recorrio todo el diccionario y se repitieron todos los caracteres más de una vez"""
            if account == len(seen_letters):
                return "_"

if __name__ == "__main__":
    char_sequence = str(input("Ingrese una secuencia de caracteres: "))
    result = first_not_repeating_char(char_sequence)

    if result == "_":
        print("Todos los caracteres se repiten")
    else:
        print("El primer caracter no repetido es: {}".format(result))