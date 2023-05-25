kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}
class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
# Pass in all the values from the dictionary by their keys
player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
print(player_kevin.position) # prints small forward

customer = {"name": "Jason Johnson", "age":34, "cabin": "C", "flight": "BA027"}
print(customer["flight"])
class Passenger:
    def __init__(self, name, age, cabin, flight):
        self.name = name
        self.age = age
        self.cabin = cabin
        self.flight = flight


