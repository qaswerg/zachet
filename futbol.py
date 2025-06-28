class Player:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nPosition: {self.position}"

class Team:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []

    def add_player(self, player):
        self.players.append(player)
        print(f"Игрок {player.name} Добавлен в команду {self.team_name}")

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)
            print(f"Игрок {player.name} Удален из команды {self.team_name}")
        else:
            print(f"Игрок {player.name} Не найден в команде {self.team_name}")

    def list_players(self):
        print(f"\nКоманда: {self.team_name}")
        print(f"Главный тренер: {self.coach}")
        print("Состав команды:")
        for player in self.players:
            print(player)
            print("-" * 20)

if __name__ == "__main__":
    player1 = Player("Хаков", 18, "Вратарь")
    player2 = Player("Сизов", 80, "Нападающий")
    player3 = Player("Колесников", 20, "Защитник")

    team1 = Team("Трактор", "Пономарев")
    team2 = Team("Рубин", "Сакалин")

    team1.add_player(player1)
    team1.add_player(player2)
    team2.add_player(player3)

    team1.list_players()
    team2.list_players()

    team1.remove_player(player2)

    team1.list_players()
