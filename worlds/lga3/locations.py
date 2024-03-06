from typing import NamedTuple
from BaseClasses import Location
from .common import *
from .options import LGA3_Options

class LGA3_Location(Location):
    game = game_disp_name
    
    # override constructor to automatically mark event locations as such
    def __init__(self, player: int, name="", code=None, parent=None) -> None:
        super(LGA3_Location, self).__init__(player, name, code, parent)
        self.event = code is None

class LocInfo(NamedTuple):
    name: str
    desc: str
    region_id: int
location_table = [
    LocInfo('Starting Sword', 'In your starting inventory', RegionID.MENU),
    LocInfo('Sword Under Rock', 'Southwest from start, push a Very Heavy rock', RegionID.OVERWORLD),
    LocInfo('Sword Under Tree', 'On the starting screen, under a tree cuttable with the Magic Sword', RegionID.OVERWORLD),
    LocInfo('Kak Red Shop 4', '4th item in red-roofed shop', RegionID.OVERWORLD),
    LocInfo('Kak Purple Shop 2', '2nd item in purple-roofed shop', RegionID.OVERWORLD),
    LocInfo('L1: Bottle', 'Collect hidden item in Level 1', RegionID.LEVEL_1),
    LocInfo('L2 KillAll: Sword', 'Kill all enemies in a room in Level 2', RegionID.LEVEL_2),
    LocInfo('L2: Bottle', 'Collect loose item in Level 2', RegionID.LEVEL_2),
    LocInfo('L3: Roc\'s Feather', 'Collect loose item in Level 3', RegionID.LEVEL_3),
    LocInfo('L4: Roc\'s Cape', 'Collect loose item in Level 4', RegionID.LEVEL_4),
    LocInfo('L5 KillAll: Bottle', 'Kill all enemies in a room in Level 5', RegionID.LEVEL_5),
    LocInfo('L6 KillAll: Bottle', 'Kill all enemies in a room in Level 6', RegionID.LEVEL_6),
    LocInfo('L6 KillAll: Tunic', 'Kill all enemies in a room in Level 6', RegionID.LEVEL_6),
    LocInfo('L9: Tunic Path', 'Item after the gold tunic gauntlet', RegionID.LEVEL_9),
    ]
location_name_to_id = {name: num for num,(name,_desc,_) in enumerate(location_table,base_number_id)}

def include_location_name(name: str, options: LGA3_Options) -> bool:
    match name:
        case 'Starting Sword':
            return options.sword_sanity == 2
        case 'L2 KillAll: Sword' | 'Sword Under Rock' | 'Sword Under Tree':
            return options.sword_sanity > 0
    return True
def include_location(loc: LGA3_Location, options: LGA3_Options) -> bool:
    return include_location_name(loc.name, options)

