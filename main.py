from classok import *
import fighting
from dialog import Dialog
from szobak import rooms
import os
import time

map = [
    [20, 25, 25, 25, 25, 25, 25, 25, 20],
    [20, 1, 0, 1, 0, 1, 0, 1, 20],
    [20, 1, 0, 1, 0, 1, 0, 1, 20],
    [20, 1, 0, 1, 0, 1, 0, 1, 20],
    [20, 26, 26, 26, 26, 26, 26, 26, 20]
]

#                             y, x
player_position: list[int] = [3, 2]

def move_down():
    global unlocked_rooms
    if map[player_position[0] + 1][player_position[1]] == 0:
        player_position[0] += 1
        for r in rooms.values():
            if r.is_this(player_position[0], player_position[1]):
                r.is_unlocked = True
                break

def move_up():
    global unlocked_rooms
    if map[player_position[0] - 1][player_position[1]] == 0:
        player_position[0] -= 1
        for r in rooms.values():
            if r.is_this(player_position[0], player_position[1]):
                r.is_unlocked = True
                break

def move_right():
    global unlocked_rooms
    if map[player_position[0]][player_position[1] + 2] == 0:
        player_position[1] += 2
        for r in rooms.values():
            if r.is_this(player_position[0], player_position[1]):
                r.is_unlocked = True
                break

def move_left():
    global unlocked_rooms
    if map[player_position[0]][player_position[1] - 2] == 0:
        player_position[1] -= 2
        for r in rooms.values():
            if r.is_this(player_position[0], player_position[1]):
                r.is_unlocked = True
                break

def clear_screen():
    os.system('cls')

def redraw_map() -> str:
    global unlocked_rooms
    output: str = ""
    #print(unlocked_rooms)
    for y, oszlop in enumerate(map):
        for x, value in enumerate(oszlop):
            if y == player_position[0] and x == player_position[1]:
                output += "¤"
                continue

            should_cont = False
            for r in rooms.values():
                if r.is_this(y, x):
                    if r.is_unlocked:
                        output += "x"
                        should_cont = True
                        break
            if should_cont:
                continue

            match value:
                case 20:
                    output += "█"
                case 26:
                    output += "▄"
                case 25:
                    output += "▀"
                case 1:
                    output += " "
                case 0:
                    output += "■"

        output += "\n"
    return output

def mozgas():
    kezdo_szoveg = Dialog("","Üdvözöllek a játékban!","Alapvetően egy szerencsére alapuló játékot játszol,","szóval sok szerencsét hozzá!","Vágjunk is mindennek a közepébe és add meg a nevedet amin hívhatunk!")
    kezdo_szoveg.print()
    time.sleep(3.5)#3.5
    clear_screen()
    username = input("Add meg a nevedet: ")
    koszonto_1 = Dialog(f"Üdvözöllek {username}!")
    koszonto_2 = Dialog("Jöhet is a karakter választás!")
    koszonto_1.print()
    koszonto_2.print()
    time.sleep(3.5)
    clear_screen()
    pickelt_class = picker()
    while True:
        clear_screen()
        print(f"\n--------------INFORMÁCIÓK--------------\n-mozágsok: w a s d\n-A kód bármely részén kilépéshez-> exit\n-A választott karaktered a(z) {pickelt_class}\n---------------------------------------")
        refresh = False
        for k, v in rooms.items():
            if v.y == player_position[0] and v.x == player_position[1]:
                print(v.story_t)
                v.message.print()
                print(v.story_a)
                if v.enemy is None:
                    break
                fighting.fighting(pickelt_class, v, "Hp")
                refresh = True
                break
        if refresh:
            continue

        print(redraw_map(), end="")
        direction: str = input("Console >")

        match direction:
            case "exit":
                clear_screen()
                exit()
            case "s":
                move_down()
            case "w":
                move_up()
            case "a":
                move_left()
            case "d":
                move_right()

mozgas()