
print("1 - Para sumar")
print("2 - Para restar")
print("3 - Para multiplicar")
print("4 - Para dividir")
print("5 - Para potenciar")
print("6 - Para raiz")


numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese otro numero: "))
operacion = int(input("Ingrese la operacion: "))

def dividir(num,div):
  return num/div

if operacion == 4:
    try:
        print (dividir(numero1,numero2))
    except ZeroDivisionError:
        print("Trataste de dividir entre cero ")