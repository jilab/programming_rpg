import random

import characters


def show_welcome():

    banner = """
    /=========================================================\\
    ||             --- THE ETERNAL COLOSSEUM ---             ||
    |=========================================================|
    ||                                                       ||
    ||   "Gladiators of the Old World, the gates open!       ||
    ||    Steel shall clash and the earth shall tremble."    ||
    ||                                                       ||
    \\=========================================================/
    """

    print(banner)


def select_champion():
    if hasattr(characters, "Warrior"):
        w_status = "SUMMONED ✨"
    else:
        w_status = "STILL IN THE VOID 🌑"

    if hasattr(characters, "Mage"):
        m_status = "SUMMONED ✨"
    else:
        m_status = "STILL IN THE VOID 🌑"

    if hasattr(characters, "BattleMage"):
        bm_status = "SUMMONED ✨"
    else:
        bm_status = "STILL IN THE VOID 🌑"

    prompt = f"""
    /=========================================================\\
    ||  Choose your destiny, Hero...                         ||
    |=========================================================|
    ||  THE SUMMONING CIRCLE:                                ||
    ||                                                       ||
    ||  [1] THE WARRIOR   ::  {w_status.ljust(22)}        ||
    ||  [2] THE MAGE      ::  {m_status.ljust(22)}        ||
    ||  [3] THE BATTLEMAGE::  {bm_status.ljust(22)}        ||
    ||                                                       ||
    \\=========================================================/
    """

    while True:
        choice = input(prompt + "\n").strip()

        if choice == "1":
            try:
                champion = characters.Warrior()
                print(">>> Warrior selected. Steel yourself!\n")
                break
            except AttributeError:
                print("WARRIOR IS STILL IN THE VOID 🌑\n")
                exit()
        elif choice == "2":
            try:
                champion = characters.Mage()
                print(">>> Mage selected. Focus your mana!\n")
                break
            except AttributeError:
                print("MAGE IS STILL IN THE VOID 🌑\n")
                exit()
        elif choice == "3":
            try:
                champion = characters.BattleMage()
                print(">>> BattleMage selected. The hybrid power awakens!\n")
                break
            except AttributeError:
                print("BATTLEMAGE IS STILL IN THE VOID 🌑\n")
                exit()
        else:
            print("Think again!\n")
    return champion


def main_game():
    show_welcome()
    print("Analyze enemy vitals and prepare for combat.")
    monster = characters.Monster()
    monster.print_monster_card()

    champion = select_champion()
    print("Your status:")
    champion.print_champion_card()

    while True:
        action = input(
            "COMMAND: [A] Attack with Steel | [M] Cast Arcane Spell\n>>> "
        ).upper()
        if action.upper() == "A":
            damage = max(int(champion.attack()) - int(monster.defence()), 0)
            monster.health -= damage
            print(
                f"\n⚔️  You lunge forward! Your blade bites deep for {damage} damage.\n"
            )
        elif action.upper() == "M":
            damage = max(int(champion.magic_attack()) - int(monster.magic_defence()), 0)
            monster.health -= damage
            print(
                f"\n🔮 You weave the winds of magic! A blast hits for {damage} damage.\n"
            )
        else:
            print("You panicked!\n")

        print(f"Monster's Health: {monster.health}")

        if int(monster.health) <= 0:
            print(
                f"\n🏆 VICTORY! The {monster.name} collapses into dust."
                "The realm is safe!"
            )
            break

        monster_action = random.randint(0, 1)
        if monster_action == 0:
            damage = max(int(monster.attack()) - int(champion.defence()), 0)
            champion.health -= damage
            print(f"\n☄️ The beast lunges with claws bared! You take {damage} damage.\n")
        else:
            damage = max(int(monster.magic_attack()) - int(champion.magic_defence()), 0)
            champion.health -= damage
            print(
                f"\n🔥 The beast exhales dragon-fire! You take {damage} magic damage.\n"
            )

        print(f"Your health: {champion.health}\n")

        if int(champion.health) <= 0:
            print(
                "💀 DEFEAT: Your vision fades to black."
                " Another soul claimed by the Arena."
            )
            break


if __name__ == "__main__":
    main_game()
