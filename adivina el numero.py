numero_a_adivinar = int(input("Dime el número que quieres que tu compañero adivine(1 / 100): "))
par_impar = numero_a_adivinar % 2

print("Comienzan las adivinanzas")

if par_impar == 0:
    print("El numero que ha elegido tu amigo es par")
else:
    print("El numero que ha elegido tu amigo es impar")
numero_adivinado = int(input("Sabes que número es? (1 / 100)"))

if numero_adivinado == numero_a_adivinar:
    print("Seguro has hecho trampa o eres todo un genio, has ganado.")
else:
    print("Ese no es, vamos con otra pista")

if numero_a_adivinar < 50:
    print("El numero de tu amigo es menor a 50")
    numero_adivinado = int(input("Sabes que número es? (1 / 50)"))
else:
    print("El numero de tu amigo es mayor que 50")
    numero_adivinado = int(input("Sabes que número es? (50 / 100)"))

if numero_adivinado == numero_a_adivinar:
    print("WoW, que grandes habilidades tienes, bien hecho")
else:
    print("Ese tampoco es, vamos con otra pista mas")

if numero_a_adivinar <= 25:
    print("El numero de tu amigo es menor que 25")
    while numero_adivinado != numero_a_adivinar:
        numero_adivinado = int(input("Ese numero no es"))
elif numero_a_adivinar >= 75:
    print("El numero de tu amigo es mayor a 75")
    while numero_adivinado != numero_a_adivinar:
        numero_adivinado = int(input("Ese numero no es"))
elif print("El numero de tu amigo está entre 25 y 75"):
    while numero_adivinado != numero_a_adivinar:
        numero_adivinado = int(input("Ese numero no es"))

print("Bien hecho, lo has adivinado")