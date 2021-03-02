numbers = [3, 4, 6, 9,54, 1,7 ]
camarades = ["Moustapha", "Abdou", "Moussa", "Adn"]
camarades.sort()
print(camarades)

def say_mor(name):
    print("Bonjour mon ami: ", name)

say_mor("Mor")

def cube(num):
    return  num*num*num
print(cube(9))

mot_cache = "mor"
trouve_mot = ""
while trouve_mot != mot_cache:
    trouve_mot = input("Entrer un mot: ")
print("Bravo vous avez trouvé le mot " + trouve_mot)


def translation(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aoieu":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translation(input("Donner une phrase")))

