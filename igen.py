import time
import os
import random
from tabulate import tabulate

table = [["Warrior", 100], ["BOSS", 200]]
print(tabulate(table, headers='firstrow', tablefmt='grid'))


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

class Poti:
    def __init__(self, nev, heal, mennyiseg):
        self.nev = nev
        self.heal = heal
        self.mennyiseg = mennyiseg

potions = {"Hp":Poti("Hp", 20, 1)}

class Ability:
    def __init__(self, nev, dmg, mennyiseg):
        self.nev = nev
        self.dmg = dmg
        self.mennyiseg = mennyiseg

kepessegek = {"Warrior_1":Ability("Ezüstszelídítés", 20, 1),
              "Warrior_2":Ability("Armor", 20, 1),
              "Mage_1":Ability("Mágikus Mátrix", 20, 1),
              "Mage_2":Ability("Morfikus Képmás", random.randrange(20, 60), 1),
              "Summoner_1":Ability("Szellemtárs", 20, 1),
              "Summoner_2":Ability("Thrash", 0, 1),
              "Assassin_1":Ability("Rejtett Penge", 20, 1),
              "Assassin_2":Ability("Ugrás", 20, 1)}

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total:
        print()

def fighting(karakter, room, heal):
    time.sleep(2.5)
    print("-----------------------------------------------HARC KÖVETKEZIK 20 MP MÚLVA!-----------------------------------------------")
    time.sleep(0.2)
    os.system("cls")
    player_turn = True
    while True:
        os.system("cls")
        if player_turn:
            print("Sima támadáshoz -> 0\nKépesség használatához -> 1\nHealeléshez -> +")
            player_attack = input("Választásod: ")
            table = [[characters[karakter].nev, characters[karakter].hp], [room.enemy.nev, room.enemy.hp]]
            print(tabulate(table, headers='firstrow', tablefmt='grid'))
            if player_attack == "0":
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
                print(f"Sebeztél a szörnyre {player_dmg} damaget!\n")

                for i in range(8):
                    printProgressBar(i, 8, prefix = 'Progress:', suffix = 'Complete', length = 50)
                    time.sleep(0.2)

                sebzes_p = mob_hp - player_dmg
                room.enemy.hp = sebzes_p
                player_turn = False
            elif player_attack == "+":
                if potions[heal].mennyiseg == 0:
                    print("Elfogyott a potionod!")
                    time.sleep(2)
                    continue
                characters[karakter].hp = characters[karakter].hp + potions[heal].heal
                potions[heal].mennyiseg -= 1
                print(f"Healeltél {potions[heal].heal} életerőt!")
                player_turn = False
            if player_attack == '1':
                if characters[karakter].nev == "Warrior":
                    all_data = [["Warrior képességei", "Leírás", "Felhasználhatóság"],
                                ["Ezüstszelídítés", "Sasha", kepessegek["Warrior_1"].mennyiseg],
                                ["Armor", "Richard", kepessegek["Warrior_2"].mennyiseg]]

                    print(tabulate(all_data, headers='firstrow', tablefmt='grid'))
                    player_attack_kepesseg = input("Add meg a választott képességed számát:")
                    if kepessegek["Warrior_"+player_attack_kepesseg].mennyiseg == 0:
                        print("Elfogyott a kepesseged!")
                        time.sleep(2)
                        continue
                    elif "Warrior_"+player_attack == "Warrior_1":
                        Warrior_1_dmg = kepessegek["Warrior_"+player_attack_kepesseg].dmg
                        kepessegek["Warrior_" + player_attack_kepesseg].mennyiseg -= 1
                        mob_hp = room.enemy.hp
                        sebzes_p = mob_hp - Warrior_1_dmg
                        room.enemy.hp = sebzes_p
                        print(f"Sebzésed mértéke az Ezüstszelídítés képesség használatával: {Warrior_1_dmg} Damage")
                        for i in range(8):
                            printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                            time.sleep(0.2)
                        if kepessegek["Warrior_"+player_attack_kepesseg].mennyiseg == 0:
                            player_turn = True
                        else:
                            player_turn = False

                    elif "Warrior_"+player_attack_kepesseg == "Warrior_2":
                        Warrior_2_hp = characters[karakter].hp + 20
                        kepessegek["Warrior_" + player_attack_kepesseg].mennyiseg -= 1
                        print(f"Az életerőd az armor képességed felhasználásával {Warrior_2_hp} mennyiségűre nőtt!")
                        for i in range(8):
                            printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                            time.sleep(0.2)
                        if kepessegek["Warrior_" + player_attack_kepesseg].mennyiseg == 0:
                            player_turn = True
                        else:
                            player_turn = False

                elif characters[karakter].nev == "Mage":
                    all_data = [["Warrior képességei", "Leírás", "Felhasználhatóság"],
                                ["Mágikus Mátrix", "Sasha", kepessegek["Mage_1"].mennyiseg],
                                ["Morfikus Képmás", "Richard", kepessegek["Mage_2"].mennyiseg]]

                    print(tabulate(all_data, headers='firstrow', tablefmt='grid'))
                    player_attack_kepesseg = input("Add meg a választott képességed számát:")
                    if kepessegek["Mage_"+player_attack_kepesseg].mennyiseg == 0:
                        print("Elfogyott a kepesseged!")
                        time.sleep(2)
                        continue
                    elif "Mage_"+player_attack_kepesseg == "Mage_1":
                        Mage_1_dmg = kepessegek["Mage_" + player_attack_kepesseg].dmg
                        mob_hp = room.enemy.hp
                        sebzes_p = mob_hp - Mage_1_dmg
                        room.enemy.hp = sebzes_p
                        kepessegek["Mage_" + player_attack_kepesseg].mennyiseg -= 1
                        print(f"Sebzésed mértéke a Mágikus Mátrix képesség használatával: {Mage_1_dmg} Damage")
                        if kepessegek["Mage_" + player_attack_kepesseg].mennyiseg == 0:
                            player_turn = True
                        else:
                            player_turn = False

                    elif "Mage_" + player_attack_kepesseg == "Mage_2":
                        Mage_2_dmg = kepessegek["Mage_2"].dmg * 2
                        mob_hp = room.enemy.hp
                        sebzes_p = mob_hp - Mage_2_dmg
                        room.enemy.hp = sebzes_p
                        kepessegek["Mage_" + player_attack_kepesseg].mennyiseg -= 1
                        print(f"A Morfikus Képmás képesség használatával a sebzesed kétszeresét sebezted a szörnyre!\n"
                              f"Sebzésed mértéke a képesség használatával: {Mage_2_dmg} Damage")
                        if kepessegek["Mage_" + player_attack_kepesseg].mennyiseg == 0:
                            player_turn = True
                        else:
                            player_turn = False

                elif characters[karakter].nev == "Summoner":
                    all_data = [["Summoner képességei", "Leírás", "Felhasználhatóság"],
                                ["Szellemtárs", "Sasha", kepessegek["Summoner_1"].mennyiseg],
                                ["Thrash", "Richard", kepessegek["Summoner_2"].mennyiseg]]

                    print(tabulate(all_data, headers='firstrow', tablefmt='grid'))
                    player_attack_kepesseg = input("Add meg a választott képességed számát:")
                    if kepessegek["Summoner_"+player_attack_kepesseg].mennyiseg == 0:
                        print("Elfogyott a kepesseged!")
                        time.sleep(2)
                        continue
                    elif "Summoner_" + player_attack_kepesseg == "Summoner_1":
                        Summoner_1_dmg = kepessegek["Summoner_" + player_attack_kepesseg].dmg
                        mob_hp = room.enemy.hp
                        sebzes_p = mob_hp - Summoner_1_dmg
                        room.enemy.hp = sebzes_p
                        kepessegek["Summoner_" + player_attack_kepesseg].mennyiseg -= 1
                        print(f"Sebzésed mértéke az Szellemtárs képesség használatával: {Summoner_1_dmg} Damage")
                        if kepessegek["Summoner_" + player_attack_kepesseg].mennyiseg == 0:
                            player_turn = True
                        else:
                            player_turn = False

                    elif "Summoner_" + player_attack_kepesseg == "Summoner_2":
                        Summoner_2_dmg = characters[karakter].dmg
                        mob_hp = room.enemy.hp
                        sebzes_p = mob_hp - Summoner_2_dmg
                        room.enemy.hp = sebzes_p
                        kepessegek["Summoner_" + player_attack_kepesseg].mennyiseg -= 1
                        print(f"Sebzésed mértéke az Thrasht képesség használatával: {Summoner_2_dmg} Damage\n"
                              f"Mégegyszer te jössz, mivel Thrasht felhasználva támadtál!")
                        if kepessegek["Summoner_" + player_attack_kepesseg].mennyiseg == 0:
                            player_turn = True
                        else:
                            player_turn = False

                elif characters[karakter].nev == "Assassin":
                    all_data = [["Assassin képességei", "Leírás", "Felhasználhatóság"],
                                ["Rejtett Penge", "Sasha", kepessegek["Assassin_1"].mennyiseg],
                                ["Ugrás", "Richard", kepessegek["Assassin_2"].mennyiseg]]

                    print(tabulate(all_data, headers='firstrow', tablefmt='grid'))
                    player_attack_kepesseg = input("Add meg a választott képességed számát:")
                    if kepessegek["Assassin_" + player_attack_kepesseg].mennyiseg == 0:
                        print("Elfogyott a kepesseged!")
                        time.sleep(2)
                        continue
                    elif "Assassin_" + player_attack_kepesseg == "Assassin_1":
                        Assassin_1_dmg = kepessegek["Assassin_" + player_attack_kepesseg].dmg
                        mob_hp = room.enemy.hp
                        sebzes_p = mob_hp - Assassin_1_dmg
                        room.enemy.hp = sebzes_p
                        kepessegek["Assassin_" + player_attack_kepesseg].mennyiseg -= 1
                        print(f"Sebzésed mértéke az Szellemtárs képesség használatával: {Assassin_1_dmg} Damage")
                        if kepessegek["Assassin_" + player_attack_kepesseg].mennyiseg == 0:
                            player_turn = True
                        else:
                            player_turn = False

                    elif "Assassin_" + player_attack_kepesseg == "Assassin_2":

                        if kepessegek["Assassin_" + player_attack_kepesseg].mennyiseg == 0:
                            player_turn = True
                        else:
                            player_turn = False

            if player_attack == "exit":
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

            for i in range(8):
                printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                time.sleep(0.2)

            characters[karakter].hp = sebzes_e
            player_turn = True
            if sebzes_e <= 0:
                print("\nVesztettél az ellenfeleddel szemben!")
                time.sleep(2.5)
                exit("Próbáld újra előről!")

        if room.enemy.hp <= 0:
            print("\nSikeresen legyőzted az ellenfeledet!\n")
            characters[karakter].hp = characters[karakter].max_hp
            if room.enemy.nev == "kemikus_boss":
                os.system("cls")
                print("Gratulálok végig vitted a játékot!")
                print("Reméljük tetszett!\n"
                      "Készítette: - Bácsi Péter\n"
                      "            - Szabó Kristóf\n")
                if characters[karakter].nev == "Summoner":
                    print("+ Respect, impossible nehézségen vitted végig a játékot! Mehetsz lottózni!")
                time.sleep(5)
                exit()
            room.enemy = None
            time.sleep(2)
            break

def fighting(karakter, room, heal):
    time.sleep(2.5)
    print("-----------------------------------------------HARC KÖVETKEZIK 20 MP MÚLVA!-----------------------------------------------")
    time.sleep(0.2)
    os.system("cls")
    player_turn = True
    while True:
        os.system("cls")
        if player_turn:
            print("Támadáshoz -> 0\nKépességhez -> 1")
            player_attack = input("Támadás (támadáshoz-> 1): ")
            if characters[karakter].nev == "Warrior":
                all_data = [["Warrior képességei", "Leírás", "Felhasználhatóság"],
                            ["Ezüstszelídítés", "Sasha", kepessegek["Warrior_" + player_attack].mennyiseg],
                            ["Armor", "Richard", kepessegek["Warrior_" + player_attack].mennyiseg]]

                print(tabulate(all_data, headers='firstrow', tablefmt='grid'))
            if characters[karakter].nev == "Mage":
                all_data = [["Warrior képességei", "Leírás", "Felhasználhatóság"],
                            ["Mágikus Mátrix", "Sasha", kepessegek["Mage_" + player_attack].mennyiseg],
                            ["Morfikus Képmás", "Richard", kepessegek["Mage_" + player_attack].mennyiseg]]

                print(tabulate(all_data, headers='firstrow', tablefmt='grid'))
            if characters[karakter].nev == "Summoner":
                all_data = [["Summoner képességei", "Leírás", "Felhasználhatóság"],
                            ["Szellemtárs", "Sasha", kepessegek["Summoner_" + player_attack].mennyiseg],
                            ["Thrash", "Richard", kepessegek["Summoner_" + player_attack].mennyiseg]]

                print(tabulate(all_data, headers='firstrow', tablefmt='grid'))
            if characters[karakter].nev == "Assassin":
                all_data = [["Assassin képességei", "Leírás", "Felhasználhatóság"],
                            ["Rejtett Penge", "Sasha", kepessegek["Assassin_" + player_attack].mennyiseg],
                            ["Ugrás", "Richard", kepessegek["Assassin_" + player_attack].mennyiseg]]

                print(tabulate(all_data, headers='firstrow', tablefmt='grid'))
            table = [[characters[karakter].nev, characters[karakter].hp], [room.enemy.nev, room.enemy.hp]]
            print(tabulate(table, headers='firstrow', tablefmt='grid'))
            if player_attack == "0":
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
                print(f"Sebeztél a szörnyre {player_dmg} damaget!\n")

                for i in range(8):
                    printProgressBar(i, 8, prefix = 'Progress:', suffix = 'Complete', length = 50)
                    time.sleep(0.2)

                sebzes_p = mob_hp - player_dmg
                room.enemy.hp = sebzes_p
                player_turn = False
            elif player_attack == "+":
                if potions[heal].mennyiseg == 0:
                    print("Elfogyott a potionod!")
                    time.sleep(2)
                    continue
                characters[karakter].hp = characters[karakter].hp + potions[heal].heal
                potions[heal].mennyiseg -= 1
                print(f"Healeltél {potions[heal].heal} életerőt!")
                player_turn = False

            elif characters[karakter].nev == "Warrior":
                if kepessegek["Warrior_"+player_attack].mennyiseg == 0:
                    print("Elfogyott a kepesseged!")
                    time.sleep(2)
                    continue
                elif "Warrior_"+player_attack == "Warrior_1":
                    Warrior_1_dmg = room.enemy.hp - kepessegek["Warrior_"+player_attack].dmg
                    kepessegek["Warrior_" + player_attack].mennyiseg -= 1
                    print(f"Sebzésed mértéke az Ezüstszelídítés képesség használatával: {Warrior_1_dmg} Damage")
                    for i in range(8):
                        printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                        time.sleep(0.2)
                    if kepessegek["Warrior_"+player_attack].mennyiseg == 0:
                        player_turn = True
                    else:
                        player_turn = False

                elif "Warrior_"+player_attack == "Warrior_2":
                    Warrior_2_hp = characters[karakter].hp + 20
                    print(f"Az életerőd az armor képességed felhasználásával {Warrior_2_hp} mennyiségűre nőtt!")
                    for i in range(8):
                        printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                        time.sleep(0.2)
                    if kepessegek["Warrior_" + player_attack].mennyiseg == 0:
                        player_turn = True
                    else:
                        player_turn = False

            elif characters[karakter].nev == "Mage":
                if kepessegek["Mage_"+player_attack].mennyiseg == 0:
                    print("Elfogyott a kepesseged!")
                    time.sleep(2)
                    continue
                elif "Mage_"+player_attack == "Mage_1":
                    Mage_1_dmg = room.enemy.hp - kepessegek["Mage_" + player_attack].dmg
                    kepessegek["Mage_" + player_attack].mennyiseg -= 1
                    print(f"Sebzésed mértéke a Mágikus Mátrix képesség használatával: {Mage_1_dmg} Damage")
                    if kepessegek["Mage_" + player_attack].mennyiseg == 0:
                        player_turn = True
                    else:
                        player_turn = False

                elif "Mage_" + player_attack == "Mage_2":
                    Mage_2_dmg = kepessegek["Mage_2"].dmg * 2
                    room.enemy.hp = room.enemy.hp - Mage_2_dmg
                    kepessegek["Mage_" + player_attack].mennyiseg -= 1
                    print(f"A Morfikus Képmás képesség használatával a sebzesed kétszeresét sebezted a szörnyre!\n"
                          f"Sebzésed mértéke a képesség használatával: {Mage_2_dmg} Damage")
                    if kepessegek["Mage_" + player_attack].mennyiseg == 0:
                        player_turn = True
                    else:
                        player_turn = False

            elif characters[karakter].nev == "Summoner":
                if kepessegek["Summoner_"+player_attack].mennyiseg == 0:
                    print("Elfogyott a kepesseged!")
                    time.sleep(2)
                    continue
                elif "Summoner_" + player_attack == "Summoner_1":
                    Summoner_1_dmg = room.enemy.hp - kepessegek["Summoner_" + player_attack].dmg
                    kepessegek["Summoner_" + player_attack].mennyiseg -= 1
                    print(f"Sebzésed mértéke az Szellemtárs képesség használatával: {Summoner_1_dmg} Damage")
                    if kepessegek["Summoner_" + player_attack].mennyiseg == 0:
                        player_turn = True
                    else:
                        player_turn = False

                elif "Summoner_" + player_attack == "Summoner_2":
                    Summoner_2_dmg = room.enemy.hp - characters[karakter].dmg
                    kepessegek["Summoner_" + player_attack].mennyiseg -= 1
                    print(f"Sebzésed mértéke az Thrasht képesség használatával: {Summoner_2_dmg} Damage\n"
                          f"Mégegyszer te jössz, mivel Thrasht felhasználva támadtál!")
                    if kepessegek["Summoner_" + player_attack].mennyiseg == 0:
                        player_turn = True
                    else:
                        player_turn = False

            elif characters[karakter].nev == "Assassin":
                if kepessegek["Assassin_" + player_attack].mennyiseg == 0:
                    print("Elfogyott a kepesseged!")
                    time.sleep(2)
                    continue
                elif "Assassin_" + player_attack == "Assassin_1":
                    Assassin_1_dmg = room.enemy.hp - kepessegek["Assassin_" + player_attack].dmg
                    kepessegek["Assassin_" + player_attack].mennyiseg -= 1
                    print(f"Sebzésed mértéke az Szellemtárs képesség használatával: {Assassin_1_dmg} Damage")
                    if kepessegek["Assassin_" + player_attack].mennyiseg == 0:
                        player_turn = True
                    else:
                        player_turn = False

                elif "Assassin_" + player_attack == "Assassin_2":

                    if kepessegek["Assassin_" + player_attack].mennyiseg == 0:
                        player_turn = True
                    else:
                        player_turn = False

            if player_attack == "exit":
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

            for i in range(8):
                printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                time.sleep(0.2)

            characters[karakter].hp = sebzes_e
            player_turn = True
            if sebzes_e <= 0:
                print("\nVesztettél az ellenfeleddel szemben!")
                time.sleep(2.5)
                exit("Próbáld újra előről!")

        if room.enemy.hp <= 0:
            print("\nSikeresen legyőzted az ellenfeledet!\n")
            characters[karakter].hp = characters[karakter].max_hp
            if room.enemy.nev == "kemikus_boss":
                os.system("cls")
                print("Gratulálok végig vitted a játékot!")
                print("Reméljük tetszett!\n"
                      "Készítette: - Bácsi Péter\n"
                      "            - Szabó Kristóf\n")
                if characters[karakter].nev == "Summoner":
                    print("+ Respect, impossible nehézségen vitted végig a játékot! Mehetsz lottózni!")
                time.sleep(5)
                exit()
            room.enemy = None
            time.sleep(2)
            break