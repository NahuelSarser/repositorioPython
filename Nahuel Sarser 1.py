print("Bienvenido a la calculadora")
num1 = int(input("Ingrese un primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
print("=====================================================================")
print("La suma de los dos números es: ", num1 + num2)
print("=====================================================================")
print("La resta de los dos números es: ", num1 - num2)
print("=====================================================================")
print("La multìplicación de los dos números es: ", num1 * num2)
print("=====================================================================")
if num1 > num2:
    print("La división de los dos números es: ", num1 // num2, ". Número 1 es mayor a Número 2")
    print("=====================================================================")
elif num1 == num2:
    print("La división de los dos números es: ", num1 // num2, ". Número 1 es igual a Número 2.")
    print("=====================================================================")
elif num1 < num2:
    print("La división de los dos números es: ", num2 // num1, ". Número 2 es mayor a Número 1.")
    print("=====================================================================")
if num1 % 2 == 0:
    print("El primer número ingresado: ", num1, ", es par.")
    print("=====================================================================")
else:
    print("El primer número ingresado: ", num1, ", es impar.")
    print("=====================================================================")
if num2 % 10 == 0:
    print("El segundo número ingresado: ", num2, ", es múltiplo de 10.")
    print("=====================================================================")
if num1 < 0 and num2 < 0:
    print("Se han ingresado dos número negativos")
    print("=====================================================================")
elif num1 > 10 or num2 > 10:
    print("Se han ingresado números mayores a 10.")
    print("=====================================================================")
for i in range(num1,num2 + 1,1):
    print("Los número incluidos entre los dos números ingresados son:",i)
print("=====================================================================")
print("Gracias por utilizar el sistema <3")




