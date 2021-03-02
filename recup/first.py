

nom = input("quel est votre nom ")
age = input("Quel est votre age ")
try:
    age_prochain = int(age) + 1
except:
    print("Erreur age invalid")
else:
    print("Vous vous appelez " + nom)
    print("Vous etes age de "+age + " ans")
    print("L'an prochain vous aurrez " + str(age_prochain)+" ans")