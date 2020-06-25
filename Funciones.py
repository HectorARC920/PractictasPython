# -*- coding: utf-8 -*-
import turtle



def main():
    window = turtle.Screen()
    david = turtle.Turtle()

    make_square(david)
    turtle.mainloop()

def make_square(david):
    length = int(input('ingrese el tamaño del cuadrado: '))

    for i in range(4):
        make_line_and_turn(david,length)

def make_line_and_turn(david,length):
    david.forward(length)
    david.right(90)

if __name__ == '__main__':
    main()


