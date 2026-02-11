import random


class Monster:
    def __init__(self):
        self.name = ""
        self.origin = ""
        self.description = ""
        self.physical_attack = 0
        self.physical_defence = 0
        self.magical_force = 0
        self.magical_defence = 0
        self.health = 0
        self.generate_monster()

    def generate_monster(self):
        monster_id = random.randint(0, 895)
        with open("Monsters.txt") as f:
            for line in f:
                parts = line.split(",")
                if str(monster_id) == parts[0]:
                    self.name = parts[1]
                    self.origin = parts[2]
                    self.description = parts[3]
                    self.physical_attack = int(parts[4])
                    self.magical_force = int(parts[5])
                    self.magical_defence = int(parts[6])
                    self.physical_defence = int(parts[7])
                    self.health = int(parts[9])
                    break

    def print_monster_card(self):
        print("\nName:            ", self.name)
        print("Origin:          ", self.origin)
        print("Description:     ", self.description)
        print("\nAttack Force:    ", self.physical_attack)
        print("Defence:         ", self.physical_defence)
        print("Magical Force:   ", self.magical_force)
        print("Magical Defence: ", self.magical_defence)
        print("Health:          ", self.health)

    def attack(self):
        return self.physical_attack

    def defence(self):
        return self.physical_defence

    def magic_attack(self):
        return self.magical_force

    def magic_defence(self):
        return self.magical_defence


class Champion:
    def __init__(self):
        self.physical_attack = 0
        self.physical_defence = 0
        self.magical_force = 0
        self.magical_defence = 0
        self.health = 0

    def print_champion_card(self):
        print("\nAttack Force:    ", self.physical_attack)
        print("Defence:         ", self.physical_defence)
        print("Magical Force:   ", self.magical_force)
        print("Magical Defence: ", self.magical_defence)
        print("Health:          ", self.health)

    def generate_champion(self):
        raise NotImplementedError("This method is not implemented yet!")

    def attack(self):
        return self.physical_attack

    def defence(self):
        return self.physical_defence

    def magic_attack(self):
        return self.magical_force

    def magic_defence(self):
        return self.magical_defence


# define Warrior class here


# define Mage class here


# define BattleMage class here
