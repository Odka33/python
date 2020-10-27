# ==============================================================================
# title           :exoB.py                                                     #
# description     :Add name to a list                                          #
# author          :Odka - Elie BEN AYOUN                                       #
# date            :29/10/2017                                                  #
# version         :0.1                                                         #
# usage           :python(3.*) exoB.py                                         #
# python_version  :3.4.3                                                       #
# ==============================================================================

liste = []
prenom = 0
print("Liste de prénon entrez 'Q' pour terminer !")
while prenom != 'Q':
    print("-------------")
    prenom = input("Entrez un prenom :")
    liste.append(prenom)
    liste.sort()
    print(liste)

