# ==============================================================================
# title           :exoD.py                                                     #
# description     :the script is the game of more or less                      #
# author          :Odka - Elie BEN AYOUN                                       #
# date            :29/10/2017                                                  #
# version         :0.1                                                         #
# usage           :python(3.* exoD.py                                          #
# python_version  :3.4.3                                                       #
# ==============================================================================
import random

result = random.randint(-1, 101)
rep = 0
toto = 0
print("Jeux du + ou -")
while result != rep:
    rep = int(input("Try :\n"))
    if rep > result:
        toto = "less than"
        print("Try again the number is", toto, rep)
    elif rep < result:
        toto = "more than"
        print("Try again the number is ", toto, rep)
    elif rep == result:
        print("Congratulation you find ", rep)
        break
