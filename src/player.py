# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, player_room):
        self.name = name
        self.player_room = player_room

    def move(self, command):
        if str(command) == 'n':
            print(f"I'm currently in {self.player_room} but trying to move.")
            self.player_room = self.player_room.n_to
            print(f"I'm currently in {self.player_room} now.")
        

    def __str__(self):
        return f'{self.name}'
