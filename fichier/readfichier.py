# On va lire un fichier
import os  # permet d'importer le chemain
import random 

if os.path.exists("repas.txt"):
    with open("repas.txt","r+") as file:
        repas_list = file.readlines()
        repas_choix = random.choice(repas_list)
        print("je vous propose, le repas", repas_choix)
        file.close()
else:
    print("Le fichier n'existe pas")        