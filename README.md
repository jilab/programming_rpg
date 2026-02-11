# The Eternal Colosseum
In this assignment, you will apply your knowledge of Object-Oriented Programming (OOP) (specifically Inheritance, Multiple Inheritance, and Attribute Management) to define the three hero classes in `characters.py`.
You are provided with a base class called `Champion`. You must not modify the base class. Instead, you will create three subclasses that inherit its properties define the three roles below.

**The `Warrior` Class (Single Inheritance)**

The Warrior is a master of physical combat and heavy armor.
- Inheritance: Must inherit from the `Champion` class.
- Constructor: The `__init__` method must call the parent constructor and then trigger `self.generate_champion()`.
- Constraints: You must override `generate_champion()` with the following stats:
  + `health`: A random integer between 10 and 20.
  + `physical_attack`: A random integer between 10 and 20.
  + `physical_defence`: A random integer between 12 and 19.
  + `magical_force` and `magical_defence`: Both must be set to 0.

**The `Mage` Class (Single Inheritance)**

The Mage wields arcane energy but is physically fragile.
- Inheritance: Must inherit from the `Champion` class.
- Constructor: The `__init__` method must call the parent constructor and then trigger `self.generate_champion()`.
- Constraints: You must override `generate_champion()` with the following stats:
  + `health`: A random integer between 5 and 12.
  + `physical_attack` and `physical_defence`: Both must be set to 0.
  + `magical_attack`: A random integer between 10 and 20.
  + `magical_defence`: A random integer between 12 and 19.

**The `BattleMage` Class (Multiple Inheritance)**

The ultimate hybrid. This class must demonstrate Multiple Inheritance.
- Inheritance: Must inherit from both `Warrior` and `Mage`.
- Constructor: The `__init__` method must call the parent constructor and then trigger `self.generate_champion()`.
- Constraints: You must override `generate_champion()` with the following stats:
  + `health`: A random integer between 8 and 16.
  + `physical_attack`: A random integer between 8 and 17.
  + `physical_defence`: A random integer between 11 and 16.
  + `magical_attack`: A random integer between 9 and 15.
  + `magical_defence`: A random integer between 8 and 18.
 
Once your implementation is complete, test your work by entering the Colosseum and running the game:

```bash
python play_game.py
```
