operation = input("Que operación quieres hacer? (suma / resta / multiplicacion / division): ")
user_number_one = float(input("Dime el primer número de la operación: "))
user_number_two = float(input("Dime el segundo número de la operación: "))
result = 0

if operation == "multiplicacion":
    result = (user_number_one * user_number_two)

elif operation == "suma":
    result = (user_number_one + user_number_two)

elif operation == "resta":
    result = (user_number_one - user_number_two)
elif operation== "division":
    result = (user_number_one / user_number_two)
print("El resultado de la operación es {}".format(result))
decision = input("Quieres hacer otra operación?(Si / No): ").upper()

while decision == "SI":

    operation = input("Que operación quieres hacer? (suma / resta / multiplicacion / division): ")
    user_number_one = float(input("Dime el primer número de la operación: "))
    user_number_two = float(input("Dime el segundo número de la operación: "))

    if operation == "multiplicacion":
        result = (user_number_one * user_number_two)
        print("El resultado de la operación es {}".format(result))
    elif operation == "suma":
        result = (user_number_one + user_number_two)
        print("El resultado de la operación es {}".format(result))
    elif operation == "resta":
        result = (user_number_one - user_number_two)
        print("El resultado de la operación es {}".format(result))
    elif operation == "division":
        result = (user_number_one / user_number_two)

    decision = input("Quieres hacer otra operación?(Si / No): ").upper()
print("Vuelve cuando necesites hacer un cálculo :D")