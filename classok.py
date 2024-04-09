class_v = None
def picker():
    print("Válassz karaktert:")
    print("1. Warrior:  Nagyon erős támadás és 150 egységnyi életerő! (Nehézség: Easy)\n"
          "2. Assassin: Erős támadás és 110 egységnyi életerő! (Nehézség: Medium)")
    print("3. Mage:     Közepesen erős támadás és 105 egységnyi életerő! (Nehézség: Hard)")
    print("4. Summoner: Gyenge támadás és 100 egységnyi életerő! (Nehézség: Impossible)")
    class_i = input("\nÍrd be a választott karaktered számát:")
    global class_v
    if class_i not in ('1', '2', '3', '1.', '2.', '3.', '4', '4.'):
        print("Ez nem választás volt!")
        exit("Próbáld újra!")
    if class_i in ('1', '1.'):
        class_v = "Warrior"
    elif class_i in ('2', '2.'):
        class_v = "Assassin"
    elif class_i in ('3', '3.'):
        class_v = "Mage"
    elif class_i in ('4', '4.'):
        class_v = "Summoner"
    return class_v

