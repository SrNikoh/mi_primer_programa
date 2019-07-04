
number_to_guess = 9
user_number = int(input("Adivina el número del 1 al 10: "))

if number_to_guess == user_number:
    print("Has acertado")
else:
    print("Intenta de nuevo sin usar ahora el {} ".format(user_number))
    user_number = int(input())
    if user_number == number_to_guess:
        print("Has ganado")
    else:
        print("Ja, no es ese. Intenta de nuevo sin usar el {} ".format(user_number))
        user_number = int(input())
        if user_number == number_to_guess:
            print("La tercera es la vencida. Has ganado")
        else:
            print("Parece que ese no es, intenta de nuevo ")
            user_number = int(input())
            if user_number == number_to_guess:
                print("Has gando... al cuarto intento")
            else:
                print("Ese tampoco es, intenta de nuevo ")
                user_number = int(input())
                if user_number == number_to_guess:
                    print("Al fin adivinas")
                else:
                    print("No pegas una, mejor vé y suscribete a Nate Gentile :D")



