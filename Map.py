from SecretBattle import *

class Map:

    def __init__(self):

        self.beginningLocation = 'Tomb Entrance'#Player's start location

        #Map is set up in a dictionary.
        #Each Location and Item is a key, and the rooms and items are the values
        self.location = {

            'Tomb Entrance': {
                                'north': 'Great Hall',

                                'east': 'War Room',

                                'west': 'Library',
            },

            'Great Hall': {
                                'north': 'Treasure Room',

                                'south': 'Tomb Entrance',

            },

            'War Room': {
                                'west': 'Tomb Entrance',

                                'specialItem': 'orb'

            },

            'Library': {
                                'east': 'Tomb Entrance',

                                'badRaider': 'Evil Raider'

            },

            'Treasure Room': {
                                'south': 'Great Hall',

                                'specialItem': 'ruby'
            }

        }

