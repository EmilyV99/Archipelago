from typing import NamedTuple, Set
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
    region_id: RID
    tags: Set[str]
    desc: str
location_table = [
    LocInfo('Starting Sword',          RID.MENU,           [], 'In your starting inventory'),
    LocInfo('Starting Bomb Bag',       RID.MENU,           [], 'In your starting inventory'),
    LocInfo('Starting Magic Ring',     RID.MENU,           [], 'In your starting inventory'),
    LocInfo('Starting Shield',         RID.MENU,           [], 'In your starting inventory'),
    LocInfo('Sword Under Block',       RID.GRASSLAND,      ['heavy2'], 'Southwest from start, push a Very Heavy rock'), #1x53
    LocInfo('Sword Under Tree',        RID.GRASSLAND,      [], 'On the starting screen, under a tree cuttable with the Magic Sword'), #1x37
    LocInfo('Boomerang Under Rock',    RID.GRASSLAND,      ['bomb'], 'Northwest of start, make the screen symmetrical'), #1x35
    LocInfo('KillAll: HeartC 1',       RID.GRASSLAND,      ['kill'], 'By level 2, kill all the blue enemies'), #1x1B
    LocInfo('KillAll: MagicC 1',       RID.GRASSLAND,      ['kill'], 'By level 2, kill all the blue enemies'), #1x0C
    LocInfo('Kak Red Shop 1',          RID.KAKARIKO,       ['shop'], '1st item in red-roofed shop'), #3x00
    LocInfo('Kak Red Shop 2',          RID.KAKARIKO,       ['shop'], '2nd item in red-roofed shop'), #3x00
    LocInfo('Kak Red Shop 3',          RID.KAKARIKO,       ['shop'], '3rd item in red-roofed shop'), #3x00
    LocInfo('Kak Red Shop 4',          RID.KAKARIKO,       ['shop','pay_1_2'], '4th item in red-roofed shop'), #3x00
    #!TODO Kak Potion Shop? How to handle re-buying potions? Leaving Vanilla for now
    LocInfo('Kak Purple Shop 1',       RID.KAKARIKO,       ['shop','pay_1_1'], '1st item in purple-roofed shop'), #3x02
    LocInfo('Kak Purple Shop 2',       RID.KAKARIKO,       ['shop','pay_1_3'], '2nd item in purple-roofed shop'), #3x02
    LocInfo('Kak Purple Shop 3',       RID.KAKARIKO,       ['shop','pay_1_2'], '3rd item in purple-roofed shop'), #3x02
    LocInfo('Kak Bombable Cave',       RID.KAKARIKO,       ['bomb'], 'Item in top-right bombable cave'), #3x47
    LocInfo('Kak Magic Rock Cave',     RID.KAKARIKO,       ['arrow'], 'Item in bottom-left arrow cave'), #3x70
    LocInfo('Hidden HeartC 1',         RID.MOUNTAIN,       ['bomb'], 'At the top of the mountain, bombable'), #1x02
    LocInfo('Hidden MagicC 1',         RID.MOUNTAIN,       ['heavy'], 'At the top-left of the mountain, push heavy block'), #1x11
    LocInfo('KillAll: MagicC 2',       RID.MOUNTAIN,       ['kill'], 'In the upper-left of the mountain, kill all Moblins'), #1x21
    LocInfo('KillAll: HeartC 2',       RID.MOUNTAIN,       ['kill'], 'In the mid-left of the mountain, kill all Moblins'), #1x40
    LocInfo('KillAll: MagicC 3',       RID.MOUNTAIN,       ['kill'], 'In the lower entrance of the mountain, kill all blue Moblins'), #1x42
    LocInfo('24-Headed Dragon',        RID.MOUNTAIN,       ['kill'], 'At the top-right of the mountain'), #1x04
    LocInfo('Cave Shop 1',             RID.MOUNTAIN,       ['shop','pay_1_3'], 'In a lower-left mountain cave'), #2x50
    LocInfo('Cave Shop 2',             RID.MOUNTAIN,       ['shop'], 'In a lower-left mountain cave'), #2x50
    LocInfo('Cave Shop 3',             RID.MOUNTAIN,       ['shop','pay_1_2'], 'In a lower-left mountain cave'), #2x50
    LocInfo('L1: Compass',             RID.LEVEL_1,        ['compass'], 'In the first room'), #4x73
    LocInfo('L1 KillAll: Map',         RID.LEVEL_1,        ['kill','map'], 'Kill all enemies in the upper-left room'), #4x62
    LocInfo('L1 KillAll: LKey',        RID.LEVEL_1,        ['kill','key'], 'Kill all enemies in the upper room'), #4x63
    LocInfo('L1 KillAll: Wallet',      RID.LEVEL_1_R,      ['kill'], 'Kill all enemies in a room in Level 1'), #4x75
    LocInfo('L1 KillAll: Life Ring',   RID.LEVEL_1_R,      ['kill'], 'Kill all enemies in a room in Level 1'), #4x66
    LocInfo('L1 KillAll: BombAmmo',    RID.LEVEL_1_R,      ['kill'], 'Kill all enemies in a room in Level 1'), #4x77
    LocInfo('L1: Bottle',              RID.LEVEL_1_R,      ['bomb'], 'Collect hidden item in Level 1'), #4x67
    LocInfo('L1 KillAll: Quiver',      RID.LEVEL_1_R,      ['kill'], 'Kill all enemies in a room in Level 1'), #4x78
    LocInfo('L1 KillAll: Boss Key',    RID.LEVEL_1_R,      ['kill','bkey'], 'Kill all enemies in a room in Level 1'), #4x68
    LocInfo('L1 Boss Reward',          RID.LEVEL_1_B,      ['wpn'], 'Kill the L1 Boss'), #4x64
    LocInfo('L1 Dungeon Reward',       RID.LEVEL_1_B,      ['wpn'], 'Beat L1'), #4x65
    LocInfo('L2 KillAll: Map',         RID.LEVEL_2,        ['kill','map'], 'Kill all enemies left of start of Level 2'), #4x7C
    LocInfo('L2 KillAll: Compass',     RID.LEVEL_2,        ['kill','compass'], 'Kill all enemies right of start of Level 2'), #4x7#
    LocInfo('L2 KillAll: Sword',       RID.LEVEL_2,        ['kill'], 'Kill all enemies in the middle-right of Level 2'), #4x6F
    LocInfo('L2 KillAll: LKey',        RID.LEVEL_2,        ['kill','key'], 'Kill all enemies in the bottom-right of Level 2'), #4x7F
    LocInfo('L2: Bottle',              RID.LEVEL_2,        [], 'Collect loose item in Level 2'), #4x4F
    LocInfo('L2 KillAll: Heart Ring',  RID.LEVEL_2,        ['kill'], 'Kill all enemies in the middle-left of Level 2'), #4x6B
    LocInfo('L2 KillAll: Boss Key',    RID.LEVEL_2,        ['kill','bkey'], 'Kill all enemies in the bottom-left of Level 2'), #4x7F
    LocInfo('L2: Coupon',              RID.LEVEL_2,        [], 'Collect loose item in Level 2'), #4x4B
    LocInfo('L2 KillAll: Bomb Ammo',   RID.LEVEL_2,        [], 'Kill  all enemies above the boss room in Level 2'), #4x4D
    LocInfo('L2 Boss Reward',          RID.LEVEL_2_B,      ['bombs'], 'Kill the L2 Boss'), #4x5D
    LocInfo('L2 Dungeon Reward',       RID.LEVEL_2_B,      ['bombs'], 'Beat L2'), #4x6D
    LocInfo('L3: Roc\'s Feather',      RID.LEVEL_3,        [], 'Collect loose item in Level 3'), #4x00
    LocInfo('L4: Roc\'s Cape',         RID.LEVEL_4,        [], 'Collect loose item in Level 4'), #4x30
    LocInfo('L5 KillAll: Bottle',      RID.LEVEL_5,        ['kill'], 'Kill all enemies in a room in Level 5'), #5x6D
    LocInfo('L6 KillAll: Bottle',      RID.LEVEL_6,        ['kill'], 'Kill all enemies in a room in Level 6'), #6x47
    LocInfo('L6 KillAll: Tunic',       RID.LEVEL_6,        ['kill'], 'Kill all enemies in a room in Level 6'), #6x58
    LocInfo('L9: Tunic Path',          RID.LEVEL_9,        [], 'Item after the gold tunic gauntlet'), #3x4A
    ]
location_name_to_id = {loc.name: num for num,loc in enumerate(location_table,base_number_id)}
