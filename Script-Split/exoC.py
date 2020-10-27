# ==============================================================================
# title           :exoC.py                                                     #
# description     :Add note and names                                          #
# author          :Odka - Elie BEN AYOUN                                       #
# date            :29/10/2017                                                  #
# version         :0.1                                                         #
# usage           :python(3.*) exoB.py                                         #
# python_version  :3.4.3                                                       #
# ==============================================================================
from operator import attrgetter, itemgetter

toto = {}
prenom = 0
nb = 0
moya = 0

print("Programme ajoutant le nom de l'eleve ainsi que sa note suite à 1 contrôle :")

while prenom != 'Q':
    nb += 1
    prenom = input("Renseigne ton prenom :")

    if prenom == 'Q':
        break
    toto[prenom] = int(input("Renseigne ta note :"))
    if prenom != 'Q':
        print(toto, "\n")

print("Les notes dans l'ordre décroissant !\n")
print(sorted(toto.items(), key=itemgetter(1), reverse=True), "\n")
print("Les notes dans l'ordre croissant !\n")
print(sorted(toto.items(), key=itemgetter(1), reverse=False))

nb = nb -1


