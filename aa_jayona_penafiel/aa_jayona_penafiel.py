class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, zombie):
        if self.health > 0:
            print(f"[{self.name}] attacks the Zombie dealing {self.damage} damage.")
            zombie.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"[{self.name}] takes {amount} damage. Current Health: {self.health}")


class Zombie:
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def move(self):
        if self.distance > 0:
            self.distance -= 1
            print(f"[{self.name}] moves 1 step closer. Current Distance: {self.distance}")

    def attack(self, plant):
        print(f"[{self.name}] attacks {plant.name} dealing {self.damage} damage.")
        plant.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"[{self.name}] takes {amount} damage. Current Health: {self.health}")

while True:

 def gameplay():
    plant1= Plant("Peashooter", health=85, damage=15)
    plant2= Plant("SnowPea", health=90, damage=10)
    zombie = Zombie("Klaiiiire", health=60, damage=10, distance=3)

    plants=[plant1, plant2]

    print("--mini pvz--")
    print(f"{plant1.name} (health: {plant1.health}, dmg: {plant1.damage})")
    print(f"{plant2.name} (health: {plant2.health}, dmg: {plant2.damage})")
    print(f"{zombie.name} (health: {zombie.health}, dmg: {zombie.damage}, dst: {zombie.distance})")

    for plant in plants:
        if plant.health > 0:
            plant.attack(zombie)

            print(f"{zombie.name}, Health: zombie.health")

        if zombie.health <=0:
            print("n/The zombie has been defeated")
            print("The plants win")
            break

    if zombie.health <= 0:
        break
    if zombie.distance > 0:
        zombie.move()

    if zombie.distance == 0:
        target = None

        for plant in plants:
            if plant.health > 0:
                target = 0
                break

            if plant1.health == 0 and plant2.health == 0:
                print("Zombie wins")
                break