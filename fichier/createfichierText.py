
# On cree un fichier student.txt avec la fonction open
file = open("student.txt", "w+")
file.write("Mor\n")
file.write("Moustapha\n")
file.write("Abdou\n")
file.close()

# On fait la mm chose frace à une boucle
list_student = ["Mor", "Moustapha", "Abdou"]

with open("student.txt","w+") as file :
    for student in list_student:
        file.write(student + "\n")
file.close()
