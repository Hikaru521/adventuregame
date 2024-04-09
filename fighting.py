import time
import os
import random
from tabulate import tabulate
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

kepessegek = {"Warrior_1":Ability("Ezüstszelídítés", 40, 1),
              "Warrior_2":Ability("Armor", 0, 1),
              "Mage_1":Ability("Mágikus Mátrix", 40, 1),
              "Mage_2":Ability("Morfikus Képmás", random.randrange(20, 60), 1),
              "Summoner_1":Ability("Szellemtárs", 40, 1),
              "Summoner_2":Ability("Thrash", 0, 1),
              "Assassin_1":Ability("Rejtett Penge", 100, 1),
              "Assassin_2":Ability("Gyüjtő", 40, 1)}

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
            choice = [["Sima támadáshoz","Képesség használatához","Healeléshez",],
                     ["0", "1", "+"]]
            print(tabulate(choice, headers='firstrow', tablefmt='grid'))
            table = [[characters[karakter].nev, characters[karakter].hp], [room.enemy.nev, room.enemy.hp]]
            print(tabulate(table, headers='firstrow', tablefmt='grid'))
            player_attack = input("Választásod: ")
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
                    printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                    time.sleep(0.25)

                sebzes_p = mob_hp - player_dmg
                room.enemy.hp = sebzes_p
                player_turn = False
            elif player_attack == "+":
                if potions[heal].mennyiseg == 0:
                    print("Elfogyott a potionod!")
                    time.sleep(2)
                    continue
                else:
                    characters[karakter].hp = characters[karakter].hp + potions[heal].heal
                    potions[heal].mennyiseg -= 1
                    print(f"Healeltél {potions[heal].heal} életerőt!")
                    for i in range(8):
                        printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                        time.sleep(0.25)
                    player_turn = False
            if player_attack == '1':
                if characters[karakter].nev == "Warrior":
                    all_data = [["Warrior képességei", "Leírás", "Felhasználhatóság", "Száma"],
                                ["Ezüstszelídítés", "Erősebb sebzést ad le az ellenfélnek!", kepessegek["Warrior_1"].mennyiseg, 1],
                                ["Armor", "A Warrior életerejéhez ad hozzá + 40 armort!", kepessegek["Warrior_2"].mennyiseg, 2]]

                    print(tabulate(all_data, headers='firstrow', tablefmt='grid'))
                    player_attack_kepesseg = input("Add meg a választott képességed számát:")
                    if player_attack_kepesseg not in ("1", "2"):
                        print("Ez nem választás volt!")
                        time.sleep(2)
                        continue
                    if kepessegek["Warrior_" + player_attack_kepesseg].mennyiseg == 0:
                        print("Elfogyott a kepesseged!")
                        time.sleep(2)
                        continue
                    elif "Warrior_" + player_attack_kepesseg == "Warrior_1":
                        Warrior_1_dmg = kepessegek["Warrior_" + player_attack_kepesseg].dmg
                        kepessegek["Warrior_" + player_attack_kepesseg].mennyiseg -= 1
                        mob_hp = room.enemy.hp
                        sebzes_p = mob_hp - Warrior_1_dmg
                        room.enemy.hp = sebzes_p
                        print(f"Sebzésed mértéke az Ezüstszelídítés képesség használatával: {Warrior_1_dmg} Damage")
                        for i in range(8):
                            printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                            time.sleep(0.25)
                        if kepessegek["Warrior_" + player_attack_kepesseg].mennyiseg == 0:
                            player_turn = False
                        else:
                            player_turn = True

                    elif "Warrior_" + player_attack_kepesseg == "Warrior_2":
                        Warrior_2_hp = characters[karakter].hp
                        modositott_hp = Warrior_2_hp + 40
                        characters[karakter].hp = modositott_hp
                        kepessegek["Warrior_" + player_attack_kepesseg].mennyiseg -= 1
                        print(f"Az életerőd az armor képességed felhasználásával {modositott_hp} mennyiségűre nőtt!")
                        for i in range(8):
                            printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                            time.sleep(0.25)
                        if kepessegek["Warrior_" + player_attack_kepesseg].mennyiseg == 0:
                            player_turn = False
                        else:
                            player_turn = True

                elif characters[karakter].nev == "Mage":
                    all_data = [["Warrior képességei", "Leírás", "Felhasználhatóság", "Száma"],
                                ["Mágikus Mátrix", "Erősebb sebzést ad le az ellenfélnek!", kepessegek["Mage_1"].mennyiseg, "1"],
                                ["Morfikus Képmás", "Generál egy képmást aki a saját sebzésedet\nmégegyszer leadja az ellenfélre!", kepessegek["Mage_2"].mennyiseg, "2"]]

                    print(tabulate(all_data, headers='firstrow', tablefmt='grid'))
                    player_attack_kepesseg = input("Add meg a választott képességed számát:")
                    if player_attack_kepesseg not in ("1", "2"):
                        print("Ez nem választás volt!")
                        time.sleep(2)
                        continue
                    if kepessegek["Mage_" + player_attack_kepesseg].mennyiseg == 0:
                        print("Elfogyott a kepesseged!")
                        time.sleep(2)
                        continue
                    elif "Mage_" + player_attack_kepesseg == "Mage_1":
                        Mage_1_dmg = kepessegek["Mage_" + player_attack_kepesseg].dmg
                        mob_hp = room.enemy.hp
                        sebzes_p = mob_hp - Mage_1_dmg
                        room.enemy.hp = sebzes_p
                        kepessegek["Mage_" + player_attack_kepesseg].mennyiseg -= 1
                        print(f"Sebzésed mértéke a Mágikus Mátrix képesség használatával: {Mage_1_dmg} Damage")
                        for i in range(8):
                            printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                            time.sleep(0.25)
                        if kepessegek["Mage_" + player_attack_kepesseg].mennyiseg == 0:
                            player_turn = False
                        else:
                            player_turn = True

                    elif "Mage_" + player_attack_kepesseg == "Mage_2":
                        Mage_2_dmg = kepessegek["Mage_2"].dmg * 2
                        mob_hp = room.enemy.hp
                        sebzes_p = mob_hp - Mage_2_dmg
                        room.enemy.hp = sebzes_p
                        kepessegek["Mage_" + player_attack_kepesseg].mennyiseg -= 1
                        print(f"Sebzésed mértéke a Morfikus Képmás képesség használatával: {Mage_2_dmg} Damage")
                        for i in range(8):
                            printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                            time.sleep(0.25)
                        if kepessegek["Mage_" + player_attack_kepesseg].mennyiseg == 0:
                            player_turn = False
                        else:
                            player_turn = True

                elif characters[karakter].nev == "Summoner":
                    all_data = [["Summoner képességei", "Leírás", "Felhasználhatóság", "Száma"],
                                ["Szellemtárs", "Erősebb sebzést ad le az ellenfélnek!", kepessegek["Summoner_1"].mennyiseg, "1"],
                                ["Thrash", "Leadsz egy sebzést majd mégegyszer te jössz\nmivel Thrash lebénította neked az ellenfelet\nviszont csak 1 körre!", kepessegek["Summoner_2"].mennyiseg, "2"]]

                    print(tabulate(all_data, headers='firstrow', tablefmt='grid'))
                    player_attack_kepesseg = input("Add meg a választott képességed számát:")
                    if player_attack_kepesseg not in ("1", "2"):
                        print("Ez nem választás volt!")
                        time.sleep(2)
                        continue
                    if player_attack_kepesseg not in ("1", "2"):
                        print("Ez nem választás volt!")
                        time.sleep(2)
                        continue
                    if kepessegek["Summoner_" + player_attack_kepesseg].mennyiseg == 0:
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
                        for i in range(8):
                            printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                            time.sleep(0.25)
                        if kepessegek["Summoner_" + player_attack_kepesseg].mennyiseg == 0:
                            player_turn = False
                        else:
                            player_turn = True

                    elif "Summoner_" + player_attack_kepesseg == "Summoner_2":
                        Summoner_2_dmg = characters[karakter].dmg
                        mob_hp = room.enemy.hp
                        sebzes_p = mob_hp - Summoner_2_dmg
                        room.enemy.hp = sebzes_p
                        kepessegek["Summoner_" + player_attack_kepesseg].mennyiseg -= 1
                        print(f"Sebzésed mértéke az Thrasht képesség használatával: {Summoner_2_dmg} Damage\n"
                              f"Mégegyszer te jössz, mivel Thrasht felhasználva támadtál és 1 körre megbénítottad az ellenségedet!")
                        for i in range(8):
                            printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                            time.sleep(0.25)
                        if kepessegek["Summoner_" + player_attack_kepesseg].mennyiseg == 0:
                            player_turn = True
                        else:
                            player_turn = False

                elif characters[karakter].nev == "Assassin":
                    all_data = [["Assassin képességei", "Leírás", "Felhasználhatóság", "Száma"],
                                ["Rejtett Penge", "Erősebb sebzést ad le az ellenfélnek!", kepessegek["Assassin_1"].mennyiseg, "1"],
                                ["Gyüjtő", "Sebez majd ha a sebzés után az ellenfélnek\nkevesebb mint 50 életereje van akkor instant megöli!", kepessegek["Assassin_2"].mennyiseg, "2"]]

                    print(tabulate(all_data, headers='firstrow', tablefmt='grid'))
                    player_attack_kepesseg = input("Add meg a választott képességed számát:")
                    if player_attack_kepesseg not in ("1", "2"):
                        print("Ez nem választás volt!")
                        time.sleep(2)
                        continue
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
                        print(f"Sebzésed mértéke a Rejtett Penge használatával: {Assassin_1_dmg} Damage")
                        for i in range(8):
                            printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                            time.sleep(0.25)
                        if kepessegek["Assassin_" + player_attack_kepesseg].mennyiseg == 0:
                            player_turn = False
                        else:
                            player_turn = True

                    elif "Assassin_" + player_attack_kepesseg == "Assassin_2":
                        Assassin_2_dmg = kepessegek["Assassin_" + player_attack_kepesseg].dmg
                        mob_hp = room.enemy.hp
                        sebzes_p = mob_hp - Assassin_2_dmg
                        room.enemy.hp = sebzes_p
                        print(f"Sebzésed mértéke a Gyüjtő használatával: {Assassin_2_dmg} Damage")
                        for i in range(8):
                            printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                            time.sleep(0.25)
                        print("\n")
                        if room.enemy.hp <= 50:
                            room.enemy.hp -= 50
                            print("Az ellenséget megölted a Gyüjtő használatával!")
                            for i in range(8):
                                printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                                time.sleep(0.25)
                        if kepessegek["Assassin_" + player_attack_kepesseg].mennyiseg == 0:
                            player_turn = False
                        else:
                            player_turn = True

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
            print("Sima támadáshoz -> 0\nKépesség használatához -> 1\nHealeléshez -> +\n")
            table = [[characters[karakter].nev, characters[karakter].hp], [room.enemy.nev, room.enemy.hp]]
            print(tabulate(table, headers='firstrow', tablefmt='grid'))
            print(f"\nSebezett a szörny rád {mob_dmg} damaget!\n")

            for i in range(8):
                printProgressBar(i, 8, prefix='Progress:', suffix='Complete', length=50)
                time.sleep(0.25)

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
                print("Remélem tetszett!\n")
                if characters[karakter].nev == "Summoner":
                    print("+ Respect, impossible nehézségen vitted végig a játékot! Mehetsz lottózni!")
                time.sleep(5)
                exit()
            room.enemy = None
            time.sleep(2)
            break
