# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, room='outside'):
        self.room = room
    
    def __str__(self):
        return f'The player is currently located: {self.room}'

jon = Player()
print(jon)