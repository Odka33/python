import time
import random
import shutil
import datetime
import os
import signal
import os.path
from operator import attrgetter, itemgetter
from random import randrange
from datetime import datetime
#from fabric.api import *
print("########################################################################################")
time.sleep(0.2)
print("#---------------------Choisissez votre programme a executer----------------------------#")
time.sleep(0.2)
print("#--------------------A =Exercice A-----------B =Exercice B-----------------------------#")
time.sleep(0.2)
print("#--------------------C =Exercice C-----------D =Exercice D-----------------------------#")
time.sleep(0.2)
print("#--------------------D2=Exercice D-----------G =Exercice G-----------------------------#")
time.sleep(0.2)
print("#--------------------G2=Exercice G-----------H =Exercice H-----------------------------#")
time.sleep(0.2)
print("#-----------------------cree par Arsene , Elie et Charly ------------------------------#")
time.sleep(0.2)
print("########################################################################################")
# ==============================================================================
# title           :exoA.py                                                     #
# description     :Calculate two numbers                                       #
# author          :Odka - Elie BEN AYOUN                                       #
# date            :29/10/2017                                                  #
# version         :0.1                                                         #
# usage           :python(3.*) exoA.py                                         #
# python_version  :3.4.3                                                       #
# ==============================================================================
def exoA():
    print("Bienvenusdans le programme de calcul\n")

    dodo = int(input("Entrez un nombre :\n"))

    fufu = int(input("Entrez un second nombre :\n"))
    print("dodo + fufu = ", dodo + fufu)


################B
# ==============================================================================
# title           :exoB.py                                                     #
# description     :Add name to a list                                          #
# author          :Odka - Elie BEN AYOUN                                       #
# date            :29/10/2017                                                  #
# version         :0.1                                                         #
# usage           :python(3.*) exoB.py                                         #
# python_version  :3.4.3                                                       #
# ==============================================================================
def exoB():
    print("Bienvenus dans l'exercice B liste de prenom")
    liste = []
    prenom = 0
    print("Liste de prénon entrez 'Q' pour terminer !")
    while prenom != 'Q':
        print("-------------")
        prenom = input("Entrez un prenom :")
        liste.append(prenom)
        liste.sort()
        print(liste)


################C
# =============================================================================#
# title           :exoC.py                                                     #
# description     :Add note and names                                          #
# author          :Odka - Elie BEN AYOUN                                       #
# date            :29/10/2017                                                  #
# version         :0.1                                                         #
# usage           :python(3.*) exoB.py                                         #
# python_version  :3.4.3                                                       #
# ==============================================================================
def exoC():
    toto = {}
    prenom = 0
    nb = 0
    moya = 0

    print("Programme ajoutant le nom de l'eleve ainsi que sa note suite à un contrôle :")

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
    nb = nb - 1
    ################D


def exoD():
    nombrePropose = 0
    print("\nJeux du plus ou moins !")
    chiffregagnant = randrange(1, 100)

    while nombrePropose != chiffregagnant:
        print("-----------------------------------------------------------")
        print("Seras-tu trouver le nombre ?\n" "Rentre un nombre :")
        nombrePropose = input()
        print("-----------------------------------------------------------\n")

        nombrePropose = int(nombrePropose)

        if nombrePropose < chiffregagnant:
            print("C'est plus !\n")
        elif nombrePropose > chiffregagnant:
            print("C'est moins !\n")
        else:
            print("Bien ouej poto t'a trouver le chiffre gagnant !!!!\n")


################D2
# ==============================================================================
# title           :exoD.py                                                     #
# description     :the script is the game of more or less                      #
# author          :Odka - Elie BEN AYOUN                                       #
# date            :29/10/2017                                                  #
# version         :0.1                                                         #
# usage           :python(3.* exoD.py                                          #
# python_version  :3.4.3                                                       #
# ==============================================================================
def exoD2():
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


################
# ==============================================================================
# title           :exoG.py                                                     #
# description     :This script make a save of the repository python.           #
# author          :Odka - Elie BEN AYOUN                                       #
# date            :29/10/2017                                                  #
# version         :0.1                                                         #
# usage           :python(3.*) exoG.py                                         #
# python_version  :3.4.3                                                       #
# ==============================================================================
def exoG():
    from datetime import datetime
    def signal_handler(signal, frame):
        print("\n", " ne fais pas quitter pendant la sauvegarde popo , merci ")

    signal.signal(signal.SIGINT, signal_handler)
    print("<><><><><><><><><><><><><><><><><><><><><>")
    print("<>", "Welcome to your custom backup manager", "<>")
    print("<><><><><><><><><><><><><><><><><><><><><>")
    print("\nif all goes well the contents of your boot \nfolder should be saved in tar.gz in '/tmp/'.\n")

    soule = '/tmp/boot.tar.gz'
    boit = '/tmp/boot'
    rhum = 'gztar'
    arrange = '/'
    picole = '/tmp/old/boot.tar.gz'
    avale = '/tmp/old/boot'
    siffle = '/tmp/boot2'
    savedir = '/tmp/oldsave/'
    pinte = '/tmp/boot3'
    yo = '/tmp/boot3.tar.gz'
    lourd = 'boot'
    ouloulou = '/old/test/'

    while os.path.exists(yo) != True:
        if os.path.exists(soule) == False:
            shutil.make_archive(boit, rhum, arrange, lourd)
        elif os.path.exists(soule) == True:
            shutil.make_archive(avale, rhum, arrange, lourd)
            timet = os.path.getmtime(soule)
            timeb = datetime.fromtimestamp(timet).strftime('%Y-%m-%d %H:%M:%S')
            times = os.path.getmtime(picole)
            timer = datetime.fromtimestamp(times).strftime('%Y-%m-%d %H:%M:%S')
            if timeb != timer:
                os.remove(soule)
                shutil.make_archive(boit, rhum, arrange, lourd)
                shutil.make_archive(siffle, rhum, arrange, lourd)
                shutil.make_archive(pinte, rhum, arrange, lourd)
                print("All went well !")
    print("<><><><><><><><><><><><><><><><><><><><><>")
    input("test le caractére d'achappement ctrl + c")


################G2
def exoG2():
    root_directory = os.path.join('C:/', 'Sauvegarde')
    save_directory = os.path.join('C:/', 'Backups')

    date = datetime.datetime.now().strftime('%Y%m%d%M%S')

    statinfo = os.stat(save_directory)
    print(os.listdir(save_directory))
    print("\n")

    print("Suppression des anciens backups")
    backups = os.listdir(save_directory)
    for f in backups:
        f = os.path.join(save_directory, f)
        f_time = os.stat(f)
        print(f_time)
        if statinfo.st_mtime > f_time.st_mtime:
            os.remove(f)

    print("-----------------------------------------------------------\n")
    print("Sauvegarde de " + root_directory + "\nDans -> " + save_directory + "\n")
    print("-----------------------------------------------------------\n")

    shutil.make_archive(
        save_directory + '/' + date + '_sauvegarde', 'gztar',
        root_directory,
        'test',
        )

    print("\n-----------------------------------------------------------\n")
    print(" La sauvegarde a bien etait fait !\n")


def exoH():
    print("Pour cette exercice il faut avoir installer avec pip 'fabric'")
#       print("vous etes sur la configuration de votre transfert ssh")
#
#        env.host_string = input("votre ip: ")
#        env.user = input("votre user: ")
#        env.password = input("votre password: ")

#        put(input('le chemin de ton fichier a save poto: '), input('le chemin du backup poto: '))

prog = input("Rentrer un caractere correspondant au script :\n")
while prog != 'Q':
    if prog == 'A':
        exoA()
        prog = input("Rentrer un caractere correspondant au script :\n")
    if prog == 'B':
        exoB()
        prog = input("Rentrer un caractere correspondant au script :\n")
    if prog == 'C':
        exoC()
        prog = input("Rentrer un caractere correspondant au script :\n")
    if prog == 'D':
        exoD()
        prog = input("Rentrer un caractere correspondant au script :\n")
    if prog == 'D2':
        exoD2()
        prog = input("Rentrer un caractere correspondant au script :\n")
    if prog == 'G':
        exoG()
        prog = input("Rentrer un caractere correspondant au script :\n")
    if prog == 'G2':
        exoG2()
        prog = input("Rentrer un caractere correspondant au script :\n")
    if prog == 'H':
        exoH()
        prog = input("Rentrer un caractere correspondant au script :\n")

    time.sleep(2)
    print("########################################################################################")
    time.sleep(2)
    print("#--------------------------cree par Arsene , Elie et Charly ---------------------------#")
    time.sleep(2)
    print("########################################################################################")
exit(0)