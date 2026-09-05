#operadores booleanos
#and, or, not
#Operadores de comparación
#==, !=, <, >, <=, >=
#mayor que >
#menor que <
#igual a ==
#mayor o igual que >=
#menor o igual que <=
#diferente de !=


#mayor que >
num1 = 10
num2 = 11

#print(f" {num1} es mayor que {num2}: {num1 > num2}") #True
#print(f" {num1} es menor que {num2}: {num1 < num2}") #False
#print(f" {num1} es igual a {num2}: {num1 == num2}") #False
#print(f" {num1} es diferente de {num2}: {num1 != num2}") #True
#print(f" {num1} es mayor o igual que {num2}: {num1 >= num2}") #True
#print(f" {num1} es menor o igual que {num2}: {num1 <= num2}") #False

#Condicionales
# if, elif, else
#if num1 > num2:
# print(f"{num1} es mayor que {num2}")
#elif num1 == num2:
#  print(f"{num1} es igual a {num2}")
#elif num1 < num2:
# print(f"{num1} es menor que {num2}")  
#else:
# print(f"{num1} no es mayor que {num2}")

# condicionales para un lady_night
# edad = 11
# dia = "sabado"
# if (edad >= 18) and (dia == "sabado"):
#     print("Puedes entrar al lady night")
# else:
#     print("No puedes entrar al lady night eres menor de edad")

# age = 21
# day = "sabado"
# gender = "femenino"
# if (day == "sabado") or (day == "viernes"):
#     if  gender == "femenino":
#         if age >= 18:
#             print("Puedes entrar al lady night")
#         else:
#             print("No puedes entrar al lady night eres menor de edad")
#     else:
#         print("No puedes entrar al lady night eres hombre")
# else:
#     print("No puedes entrar al lady night hoy no es sabado ni viernes")

#tipos de datos
#cadenas de caracteres
name = "Jose"
name2= 'Jose'

#nuemeros
num1 = 12
num2 = 12.5

# print(type(num2))
# print(type(num1))
# print(type(name))

#Listas
name_list =["Jose", 
            "Maria",
              "Juan"]
num_list = [1, 2, 3, 4, 5]
weather_list = ["soleado",
                 "lluvioso",
                   "nublado"]

# print(name_list)
# print(num_list)
# print(weather_list)

#diccionarios
person_dict = {
    "name": "Jose",
    "last_name": "Rojas",
    "age": 27,
    "city": "Barcelona",
    "Color_favorito": ["Azul", "Rojo"]
}
print(person_dict["age"])