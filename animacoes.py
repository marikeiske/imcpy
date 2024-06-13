from time import * 
from os import *



def calc (raio, altura):
    A = raio*raio*3.14
    V = A * altura
    print(" Calculado !", V)
    return V



# Emojis

def loading():
    for i in range (7):
        if i == 0:
            system("cls")
            print("🟩🟩🟩🟩🟩🟩")
            sleep(1)
        if i == 1:
            system("cls")
            print("⬜🟩🟩🟩🟩🟩")
            sleep(1)
        if i == 2:
            system("cls")
            print("⬜⬜🟩🟩🟩🟩")
            sleep(1)
        if i == 3:
            system("cls")
            print("⬜⬜⬜🟩🟩🟩")
            sleep(1)
        if i == 4:
            system("cls")
            print("⬜⬜⬜⬜🟩🟩")
            sleep(1)
        if i == 5:
            system("cls")
            print("⬜⬜⬜⬜⬜🟩")
            sleep(1)
        if i == 6:
            system("cls")
            print("⬜⬜⬜⬜⬜⬜")
            sleep(1)