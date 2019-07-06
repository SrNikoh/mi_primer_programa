

pokemon_choose = input("With who do you want to fight? (Squirtle / Charmander / Bulbasaur): ").upper()
life_pikachu = 100
opponent_life = 0
squirtle_damage = 10
bulbasaur_damage = 7
charmander_damage = 14
if pokemon_choose == "SQUIRTLE":
    opponent_life = 80
    pokemon_name = Squirtle
elif pokemon_choose == "CHARMANDER":
    opponent_life = 70
    pokemon_name = Charmander
elif pokemon_choose == "BULBASAUR":
    opponent_life = 120
    pokemon_name = Bulbasaur
while life_pikachu > 0 and opponent_life > 0:
    choosed_atack = input("Wich atack do you like to use? (Sparkies / Voltio Ball): ").upper()
    if choosed_atack == "SPARKIES":
        opponent_life -= 10
    elif choosed_atack == "VOLTIO BALL":
        opponent_life -= 12
    print("Nice {} just have {} points of life Come on".format(pokemon_name, opponent_life))
    if pokemon_choose == "SQUIRTLE":
        life_pikachu -= squirtle_damage
        print("{} atack you causing {} of damage".format(pokemon_name, squirtle_damage))
    elif pokemon_choose == "CHARMANDER":
        life_pikachu -= charmander_damage
        print("{} atack you causing {} of damage".format(pokemon_name, charmander_damage))
    elif pokemon_choose == "BULBASAUR":
        life_pikachu -= bulbasaur_damage
        print("{} atack you causing {} of damage".format(pokemon_name, bulbasaur_damage))
    print("Now your lifes points are {}".format( life_pikachu ))
print("El combate ha terminado")
if opponent_life <= 0:
    print("Congrats, you are the pokemon master!")
elif life_pikachu <= 0:
    print("Oh no, you loose, try again")