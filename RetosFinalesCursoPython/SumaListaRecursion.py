def run(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + run(lista[1:])


if __name__ == "__main__":
    lista = [1,2,3]
    result = run(lista)
    print("La suma es: {}".format(result))
