print(
    ''''
    ==== Bienvenido a tu Calculadora ====
    '''
)


class Calculadora:
    def __init__(self):
        pass

    def pedirDatos(self):
        dato1 = float(input('Primera cantidad: '))
        dato2 = float(input('Segunda cantidad: '))
        return dato1, dato2

    def suma(self, a, b): return a + b
    def resta(self, a, b): return a - b
    def multi(self, a, b): return a * b
    def division(self, a, b): return a / b


calculadora = Calculadora()

while True:
    opcion = int(input('''
                       Coloque el numero de la operacion que desea realizar:
                       1.Suma
                       2.Resta
                       3.Multiplicar
                       4.Dividir
                       5.Salir de la Calculadora: '''))

    if opcion in [1, 2, 3, 4]:
        dato1, dato2 = calculadora.pedirDatos()

        if opcion == 1:
            print(calculadora.suma(dato1, dato2))

        elif opcion == 2:
            print(calculadora.resta(dato1, dato2))

        elif opcion == 3:
            print(calculadora.multi(dato1, dato2))

        elif opcion == 4:
            print(calculadora.division(dato1, dato2))

    elif opcion == 5:
        print('Hasta pronto.')
        break
    else:
        print('Opcion no valida, por favor intente nuevamente.')
