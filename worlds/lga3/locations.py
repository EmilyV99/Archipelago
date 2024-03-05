from typing import NamedTuple
from BaseClasses import Location
from .common import *
from .options import LGA3_Options

class LGA3_Location(Location):
    game = 'Link\'s Grand Adventure 3: Remastered'
    
    # override constructor to automatically mark event locations as such
    def __init__(self, player: int, name="", code=None, parent=None) -> None:
        super(LGA3_Location, self).__init__(player, name, code, parent)
        self.event = code is None

class LocInfo(NamedTuple):
    name: str
    desc: str
    region_id: int
location_table = [
    LocInfo('Starting Sword', 'In your starting inventory', -1),
    LocInfo('Sword Under Rock', 'Southwest from start, push a Very Heavy rock', 0),
    LocInfo('Sword Under Tree', 'On the starting screen, under a tree cuttable with the Magic Sword', 0),
    LocInfo('Kak Red Shop 4', '4th item in red-roofed shop', 0),
    LocInfo('Kak Purple Shop 2', '2nd item in purple-roofed shop', 0),
    LocInfo('L1: Bottle', 'Collect hidden item in Level 1', 1),
    LocInfo('L2 KillAll: Sword', 'Kill all enemies in a room in Level 2', 2),
    LocInfo('L2: Bottle', 'Collect loose item in Level 2', 2),
    LocInfo('L3: Roc\'s Feather', 'Collect loose item in Level 3', 3),
    LocInfo('L4: Roc\'s Cape', 'Collect loose item in Level 4', 4),
    LocInfo('L5 KillAll: Bottle', 'Kill all enemies in a room in Level 5', 5),
    LocInfo('L6 KillAll: Bottle', 'Kill all enemies in a room in Level 6', 6),
    LocInfo('L6 KillAll: Tunic', 'Kill all enemies in a room in Level 6', 6),
    LocInfo('L9: Tunic Path', 'Item after the gold tunic gauntlet', 9),
    ]
location_name_to_id = {name: num for num,(name,_desc,_) in enumerate(location_table,base_number_id)}


def include_location(loc: LGA3_Location, options: LGA3_Options) -> bool:
    match loc.name:
        case 'Starting Sword':
            return options.sword_sanity == 2
        case 'L2 KillAll: Sword' | 'Sword Under Rock' | 'Sword Under Tree':
            return options.sword_sanity > 0
    return True

