# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, player_room):
        self.name = name
        self.player_room = player_room

    def move(self, command):
        if str(command) == 'n':
            if self.player_room.n_to == None:
                print("You can't go that way, try a different direction.")
            else:
                self.player_room = self.player_room.n_to
        elif str(command) == 's':
            if self.player_room.s_to == None:
                print("You can't go that way, try a different direction.")
            else:
                self.player_room = self.player_room.s_to
        elif str(command) == 'e':
            if self.player_room.e_to == None:
                print("You can't go that way, try a different direction.")
            else:
                self.player_room = self.player_room.e_to
        elif str(command) == 'w':
            if self.player_room.w_to == None:
                print("You can't go that way, try a different direction.")
            else:
                self.player_room = self.player_room.w_to

    def __str__(self):
        return f'{self.name}'
