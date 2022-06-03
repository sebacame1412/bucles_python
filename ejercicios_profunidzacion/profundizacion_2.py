# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

from __future__ import division


print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

numero_1 = 8
numero_2 = 2

print("Para utilizar la calculadora debe ingresar el simbolo de la ecuación que desea realizar")
print("Para finalizar debe escribir la palabra FIN")
simbolo = str(input("Ingrese el simbolo de la ecuacion que desea realizar\n"))

while simbolo == "fin":
    break

if simbolo == "+":
     suma = numero_1 + numero_2
     print("El resultado de la suma entre los numeros es:", suma)
     

if simbolo == "-":
         resta = numero_1 - numero_2
         print("El resultado de la resta entre los numeros es:", resta)
         
if simbolo == "*":
        multiplicacion = numero_1 * numero_2
        print("El resultado de la multiplicación entre los numeros es:", multiplicacion)
              
if simbolo == "/":
        division = numero_1 / numero_2
        print("El resultado de la división entre los numeros es:", division)
        
if simbolo == "**":
        exponente = numero_1 ** numero_2
        print("El exponente entre los numeros es:", exponente)
        
#  while simbolo != "+" or not "-" or not "*" or not "/" or not "**":
#    print("Debe ingresar un caracter valido, vuelva a intentarlo")
#    continue
#  Quise intentar esto para que el programa se repita hasta que se
#  escriba la palabra fin pero no me salio, me rindo.






               

