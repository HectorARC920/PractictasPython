def ReadFile():
    count = 0
    with open("MiArchivo.txt","r") as f:
        for line in f:
            count += line.count("2")
        print("El num 2 se encuentra {} veces en el texto".format(count))

def WriteFile():
    with open('MiArchivo.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))

if __name__ == '__main__':
    #WriteFile()
    ReadFile()