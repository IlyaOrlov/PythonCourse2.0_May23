class Tank:
    def __init__(self, name, health, damage):
        """
        Конструктор класса Tank.

        Args:
            name (str): Имя танка.
            health (int): Здоровье танка.
            damage (int): Урон, наносимый танком.
        """
        self.name = name
        self.health = health
        self.damage = damage

    def shoot(self, target):
        """
        Метод для выстрела танка в цель.

        Args:
            target (Tank): Цель для атаки.
        """
        target.health -= self.damage
        print(f"{self.name} нанес {self.damage} урона по {target.name}. {target.name} имеет {target.health} здоровья.")


# Создание экземпляров танков
tank1 = Tank("Танк 1", 100, 20)
tank2 = Tank("Танк 2", 120, 15)

# Пример использования метода shoot()
tank1.shoot(tank2)
