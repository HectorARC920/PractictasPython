import csv

class Conctact:
    def __init__(self,name,phone,email):
        self._name = name
        self._phone = phone
        self._email = email

    def getName(self):
        return self._name

    def setName(self,name):
        self._name = name

    def getPhone(self):
        return self._phone

    def setPhone(self,phone):
        self._phone = phone

    def getEmail(self):
        return self._email

    def setEmail(self,email):
        self._email = email

class ConctactBook:
    def __init__(self):
        self._conctact = []

    def add(self,name,phone,email):
        contact = Conctact(name,phone,email)
        self._conctact.append(contact)
        self._save()

    def _save(self):
        with open ("C:/Users/Hecto/Desktop/PracticasPython/19-Agenda/contacts.csv","w",newline="") as f:
            writer = csv.writer(f)
            writer.writerow(("Name","Phone","Email" ))
            for contact in self._conctact:
                writer.writerow((contact.getName(),contact.getPhone(),contact.getEmail()))
            

    def show_all(self):
        for contact in self._conctact:
            self._print_contact(contact)

    def _print_contact(self,contact):
        print("----*----*----*----*----*----*---")
        print("Nombre: {}".format(contact.getName()))
        print("Telefono: {}".format(contact.getPhone()))
        print("Email: {}".format(contact.getEmail()))
        print("----*----*----*----*----*----*---")

    def update(self,name):
        for contact in self._conctact:
            if contact.getName() == name:
                newname = str(input("Ingrese nuevo nombre: "))
                contact.setName(newname)
                newphone = str(input("Ingrese nuevo telefono: "))
                contact.setPhone(newphone)
                newemail = str(input("Ingrese nuevo Email: "))
                contact.setEmail(newemail)
                self._save()
            else:
                print("Necesita ingresar un nombre que este registrado en nuestra base de datos")
            
    def search(self,name):
        for contact in self._conctact:
            if name.lower() == contact.getName().lower():
                self._print_contact(contact)
            else:
                print("El nombre no fue encontrado en nuestra base de datos")

    def delete(self,name):
        for contact in self._conctact:
            if name.lower() == contact.getName().lower():
                print("El nombre {} fue borrado de la base de datos".format(contact.getName()))
                self._conctact.remove(contact)
                self._save()
                break
            else:
                print("El nombre ingresado no fue encontrado en la base de datos")

def run():
    contact_book = ConctactBook()
    with open ("C:/Users/Hecto/Desktop/PracticasPython/19-Agenda/contacts.csv","r") as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            contact_book.add(row[0],row[1],row[2])
    while True:
        command = str(input("""
    
    Qué desea hacer?

    [a]ñadir contacto
    [ac]tualizar contacto
    [b]uscar contacto
    [e]liminar contacto
    [l]istar contactos
    [s]alir
    """))

        if command == "a":
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el tel del contacto: '))
            email = str(input('Escribe el email del contacto: '))
            contact_book.add(name,phone,email)
        elif command == "ac":
            name = str(input('Escribe el nombre del contacto: '))
            contact_book.update(name)

        elif command == "b":
            name = str(input("Ingresa el nombre a buscar: "))
            contact_book.search(name)

        elif command == "e":
            name = str(input("Ingresa el nombre a borrar"))
            contact_book.delete(name)

        elif command == "l":
            contact_book.show_all()

        elif command == "s":
            print("s")
            break

        else:
            print("Comando no reconocido")
if __name__ == "__main__":
    print("Bienvenido a la Agenda ")
    run()