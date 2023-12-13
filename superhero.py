import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(0, self.max_damage)

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)

class Weapon:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        return random.randint(0, self.max_damage)

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        total_damage = sum(ability.attack() for ability in self.abilities)
        return total_damage

    def defend(self):
        total_block = sum(armor.block() for armor in self.armors)
        return total_block

    def take_damage(self, damage):
        defense = self.defend()
        damage_taken = damage - defense
        self.current_health -= damage_taken

    def is_alive(self):
        return self.current_health > 0

    def fight(self, opponent):
        if not self.abilities and not opponent.abilities:
            print("Draw - Both heroes have no abilities.")
        else:
            while self.is_alive() and opponent.is_alive():
                self_damage = self.attack()
                opponent_damage = opponent.attack()
                opponent.take_damage(self_damage)
                self.take_damage(opponent_damage)

            if self.is_alive():
                self.add_kill(1)
                opponent.add_death(1)
                print(f"{self.name} wins the fight with {self.current_health} health remaining!")
            elif opponent.is_alive():
                self.add_death(1)
                opponent.add_kill(1)
                print(f"{opponent.name} wins the fight with {opponent.current_health} health remaining!")
            else:
                print("It's a draw!")

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths

    def stats(self):
        if self.deaths == 0:
            kd = self.kills
        else:
            kd = self.kills / self.deaths
        print(f"Hero: {self.name}, K/D: {kd}")

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        self.heroes = [hero for hero in self.heroes if hero.name != name]

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def team_attack(self, other_team):
        while self.is_team_alive() and other_team.is_team_alive():
            hero_1 = random.choice(self.heroes)
            hero_2 = random.choice(other_team.heroes)
            hero_1.fight(hero_2)

    def is_team_alive(self):
        return any(hero.is_alive() for hero in self.heroes)

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("Enter ability name: ")
        max_damage = int(input("Enter max damage: "))
        return Ability(name, max_damage)

    def create_armor(self):
        name = input("Enter armor name: ")
        max_block = int(input("Enter max block: "))
        return Armor(name, max_block)

    def create_weapon(self):
        name = input("Enter weapon name: ")
        max_damage = int(input("Enter max damage: "))
        return Weapon(name, max_damage)

    def create_hero(self):
        name = input("Enter hero name: ")
        starting_health = int(input("Enter starting health: "))
        hero = Hero(name, starting_health)
        num_abilities = int(input("How many abilities do you want to add? "))
        for _ in range(num_abilities):
            ability = self.create_ability()
            hero.add_ability(ability)
        num_armors = int(input("How many armors do you want to add? "))
        for _ in range(num_armors):
            armor = self.create_armor()
            hero.add_armor(armor)
        num_weapons = int(input("How many weapons do you want to add? "))
        for _ in range(num_weapons):
            weapon = self.create_weapon()
            hero.add_ability(weapon)
        return hero

    def build_team(self):
        team_name = input("Enter team name: ")
        num_heroes = int(input("How many heroes in the team? "))
        team = Team(team_name)
        for _ in range(num_heroes):
            hero = self.create_hero()
            team.add_hero(hero)
        return team

    def team_battle(self):
        self.team_one.team_attack(self.team_two)

    def show_stats(self):
        print("\nTeam One Statistics:")
        self.team_one.view_all_heroes()
        self.team_one.stats()

        print("\nTeam Two Statistics:")
        self.team_two.view_all_heroes()
        self.team_two.stats()

        if self.team_one.is_team_alive():
            print(f"{self.team_one.name} wins!")
        else:
            print(f"{self.team_two.name} wins!")

if __name__ == "__main__":
    arena = Arena()
    arena.team_one = arena.build_team()
    arena.team_two = arena.build_team()
    arena.team_battle()
    arena.show_stats()

