def recursive(num):
    if num == 1:
        return 1
    elif num < 1:
        return 0
    else:
        return num + recursive(num-1)
if __name__ == "__main__":
    num = int(input("Ingresa un numero y lo sumare de forma recursiva: "))
    result = recursive(num)
    print("El Resultado de la suma recursiva de {} es {}".format(num,result))