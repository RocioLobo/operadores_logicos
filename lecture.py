#1.Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:
#Guarda en una variable numero_magico el valor 12345679 (sin el 8)
#Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
#Multiplica el numero_usuario por 9 en sí mismo
#Multiplica el numero_magico por el numero_usuario en sí mismo
#Finalmente muestra el valor final del numero_magico por pantalla

numero_magico=12345679
numero_usuario=input("Ingresa un Numero del 1 al 9: ")
numero_usuario=int(numero_usuario)
numero_usuario= numero_usuario * 9
multiplicacion=numero_usuario *numero_magico
print(f"numero magico:{multiplicacion} ")


#1. Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):

#Si los dos números son iguales
#Si los dos números son diferentes
#Si el primero es mayor que el segundo
#Si el segundo es mayor o igual que el primero

#In [3]:
# Completa el ejercicio aquí
num1 = float( input( "Introduce el primer número: "))
num2 = float( input( "Introduce el segundo número: "))

print( "¿Los números son iguales?:", num1 == num2)
print( "¿Los números son diferentes?:", num1 != num2)
print( "¿El primer número es mayor que el segundo?:", num1 > num2)
print( "¿El segundo número es mayor o igual que el primero?:", num2 >= num2)