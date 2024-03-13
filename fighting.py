from enemyk import *
import time
import os

class player:
    def __init__(self, nev, hp, dmg):
        self.nev = nev
        self.hp = hp
        self.dmg = dmg
        self.max_hp = hp

characters = {"Warrior":player("Warrior", 150, random.randrange(40, 50)), #easy
        "Mage":player("Mage", 105, random.randrange(20, 60)), #hard
        "Assassin":player("Assassin", 110, random.randrange(40, 50)), #medium
        "Summoner":player("Summoner", 100, random.randrange(10, 67))} #impossible


def fighting(karakter, room):
    time.sleep(2.5)
    print("-----------------------------------------------HARC KÖVETKEZIK 20 MP MÚLVA!-----------------------------------------------")
    time.sleep(20)
    os.system("cls")
    print(f"-----------------------\nPlayer hp: {characters[karakter].hp}\nMob hp: {room.enemy.hp}\n-----------------------")
    player_turn = True
    while True:
        os.system("cls")
        print(f"-----------------------\nPlayer hp: {characters[karakter].hp}\nMob hp: {room.enemy.hp}\n-----------------------")
        if player_turn:
            a = input("Támadás (támadáshoz-> 1): ")
            if a == "1":
                player_dmg = characters[karakter].dmg
                if characters[karakter].nev == "Warrior":
                    characters[karakter].dmg = random.randrange(40, 50)
                if characters[karakter].nev == "Mage":
                    characters[karakter].dmg = random.randrange(20, 60)
                if characters[karakter].nev == "Assassin":
                    characters[karakter].dmg = random.randrange(40, 50)
                if characters[karakter].nev == "Summoner":
                    characters[karakter].dmg = random.randrange(10, 67)
                mob_hp = room.enemy.hp
                sebzes_p = mob_hp - player_dmg
                print(f"Sebeztél a szörnyre {player_dmg} damaget!\n")
                time.sleep(1.5)
                room.enemy.hp =sebzes_p
                player_turn = False
                if sebzes_p <= 0:
                    print("Sikeresen legyőzted az ellenfeledet!\n")
                    characters[karakter].hp = characters[karakter].max_hp
                    if room.enemy.nev == "kemikus_boss":
                        print("Gratulálok végig vitted a játékot!")
                        print("Reméljük tetszett!\n"
                             "Készítette: - Bácsi Péter\n"
                             "            - Szabó Kristóf")
                        time.sleep(5)
                        exit()
                    room.enemy = None
                    time.sleep(2)
                    break
            elif a == "exit":
                exit()
        else:
            player_hp = characters[karakter].hp
            if room.enemy.nev == "kutya":
                room.enemy.dmg = random.randrange(20, 34)
            if room.enemy.nev == "medve":
                room.enemy.dmg = random.randrange(30, 33)
            if room.enemy.nev == "kemikus_boss":
                room.enemy.dmg = random.randrange(20, 35)
            if room.enemy.nev == "soldier":
                room.enemy.dmg = random.randrange(25, 30)
            mob_dmg = room.enemy.dmg
            sebzes_e = player_hp - mob_dmg
            print(f"\nSebezett a szörny rád {mob_dmg} damaget!\n")
            time.sleep(1.5)
            characters[karakter].hp = sebzes_e
            player_turn = True
            if sebzes_e <= 0:
                print("Vesztettél az ellenfeleddel szemben!")
                time.sleep(5)
                exit("Próbáld újra előről!")

