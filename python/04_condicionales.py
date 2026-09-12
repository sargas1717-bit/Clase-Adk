# Uso de estructuras condicionales (if, elif, else)
edad = 18
tiene_identificacion = True

if edad >= 18 and tiene_identificacion:
    print("Acceso permitido. Eres mayor de edad y tienes identificación.")
elif edad >= 18 and not tiene_identificacion:
    print("Eres mayor de edad, pero necesitas tu identificación para ingresar.")
else:
    print("Acceso denegado. Eres menor de edad.")