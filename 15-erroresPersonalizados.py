paises = {
    "mexico":122,
    "colombia":50,
    "argentina":44,
    "peru":32,
    "venezuela":22
    }

def run():
    try:
        pais = str(input("Ingrese un pais y te dire su población en millones: ")).lower()
        print("{} cuenta con {} millones de habitantes".format(pais,paises[pais]))
    except KeyError:
        print("{} no existe en nuestra base de datos".format(pais))
if __name__ == "__main__":
    run()