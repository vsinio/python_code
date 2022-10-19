class Player:
    def player_method(self):
        print("Родительский метод класса Player")


class Navigator:
    def navigator_method(self):
        print("Родительский метод класса Navigator")


class MobilePhone(Player, Navigator):
    def mobile_phone_method(self):
        print("Дочерний метод класса MobilePhone")


m_p = MobilePhone()
m_p.player_method()
m_p.navigator_method()

"""
Родительский метод класса Player
Родительский метод класса Navigator
"""
