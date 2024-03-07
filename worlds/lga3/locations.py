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
    LocInfo('Starting Sword',                  RID.MENU,           [], 'In your starting inventory'),
    LocInfo('Starting Bomb Bag',               RID.MENU,           [], 'In your starting inventory'),
    LocInfo('Starting Magic Ring',             RID.MENU,           [], 'In your starting inventory'),
    LocInfo('Starting Shield',                 RID.MENU,           [], 'In your starting inventory'),
    LocInfo('Sword Under Block',               RID.GRASSLAND,      ['heavy2'], 'Southwest from start, push a Very Heavy rock'), #1x53
    LocInfo('Sword Under Tree',                RID.GRASSLAND,      ['sword3'], 'On the starting screen, under a tree cuttable with the Magic Sword'), #1x37
    LocInfo('Boomerang Under Rock',            RID.GRASSLAND,      ['bomb'], 'Northwest of start, make the screen symmetrical'), #1x35
    LocInfo('KillAll: HeartC 1',               RID.GRASSLAND,      ['kill','wpn'], 'By level 2, kill all the blue enemies'), #1x1B
    LocInfo('KillAll: MagicC 1',               RID.GRASSLAND,      ['kill','wpn'], 'By level 2, kill all the blue enemies'), #1x0C
    LocInfo('Kak Red Shop 1',                  RID.KAKARIKO,       ['shop'], '1st item in red-roofed shop'), #3x00
    LocInfo('Kak Red Shop 2',                  RID.KAKARIKO,       ['shop'], '2nd item in red-roofed shop'), #3x00
    LocInfo('Kak Red Shop 3',                  RID.KAKARIKO,       ['shop'], '3rd item in red-roofed shop'), #3x00
    LocInfo('Kak Red Shop 4',                  RID.KAKARIKO,       ['shop','pay_1_2'], '4th item in red-roofed shop'), #3x00
    #!TODO Kak Potion Shop? How to handle re-buying potions? Leaving Vanilla for now #3x01
    LocInfo('Kak Purple Shop 1',               RID.KAKARIKO,       ['shop','pay_1_1'], '1st item in purple-roofed shop'), #3x02
    LocInfo('Kak Purple Shop 2',               RID.KAKARIKO,       ['shop','pay_1_3'], '2nd item in purple-roofed shop'), #3x02
    LocInfo('Kak Purple Shop 3',               RID.KAKARIKO,       ['shop','pay_1_2'], '3rd item in purple-roofed shop'), #3x02
    LocInfo('Kak Bombable Cave',               RID.KAKARIKO,       ['bomb'], 'In top-right bombable cave'), #3x47
    LocInfo('Kak Magic Rock Cave',             RID.KAKARIKO,       ['arrow'], 'In bottom-left arrow cave'), #3x70
    LocInfo('Hidden HeartC 1',                 RID.MOUNTAIN,       ['bomb'], 'At the top of the mountain, bombable'), #1x02
    LocInfo('Hidden MagicC 1',                 RID.MOUNTAIN,       ['heavy'], 'At the top-left of the mountain, push heavy block'), #1x11
    LocInfo('KillAll: MagicC 2',               RID.MOUNTAIN,       ['kill','wpn'], 'In the upper-left of the mountain, kill all Moblins'), #1x21
    LocInfo('KillAll: HeartC 2',               RID.MOUNTAIN,       ['kill','wpn'], 'In the mid-left of the mountain, kill all Moblins'), #1x40
    LocInfo('KillAll: MagicC 3',               RID.MOUNTAIN,       ['kill','wpn'], 'In the lower entrance of the mountain, kill all blue Moblins'), #1x42
    LocInfo('24-Headed Dragon',                RID.MOUNTAIN,       ['kill','tough_fight'], 'At the top-right of the mountain'), #1x04
    LocInfo('Cave Shop 1',                     RID.MOUNTAIN,       ['shop','pay_1_3'], 'In a lower-left mountain cave'), #2x50
    LocInfo('Cave Shop 2',                     RID.MOUNTAIN,       ['shop'], 'In a lower-left mountain cave'), #2x50
    LocInfo('Cave Shop 3',                     RID.MOUNTAIN,       ['shop','pay_1_2'], 'In a lower-left mountain cave'), #2x50
    #!TODO Super Bomb shop? How to handle re-buying? #2x70
    LocInfo('KillAll: Cross Beams',            RID.DESERT,         ['kill','wpn'], 'Kill all the fire octos on a screen'), #1x07
    LocInfo('KillAll: MagicC',                 RID.DESERT,         ['kill','wpn'], 'Kill all the fire octos on a screen'), #1x06
    LocInfo('Hidden: MagicC',                  RID.DESERT,         ['bomb'], 'Bomb the mountain wall'), #1x05
    LocInfo('L1: Compass',                     RID.LEVEL_1,        ['compass'], 'In the first room'), #4x73
    LocInfo('L1 KillAll: Map',                 RID.LEVEL_1,        ['kill','wpn','map'], 'Kill all enemies in the upper-left room'), #4x62
    LocInfo('L1 KillAll: LKey',                RID.LEVEL_1,        ['kill','wpn','key'], 'Kill all enemies in the upper room'), #4x63
    LocInfo('L1 KillAll: Wallet',              RID.LEVEL_1_R,      ['kill','wpn'], 'Kill all enemies in a room'), #4x75
    LocInfo('L1 KillAll: Life Ring',           RID.LEVEL_1_R,      ['kill','wpn'], 'Kill all enemies in a room'), #4x66
    LocInfo('L1 KillAll: Bomb Ammo',           RID.LEVEL_1_R,      ['kill','wpn'], 'Kill all enemies in a room'), #4x77
    LocInfo('L1: Bottle',                      RID.LEVEL_1_R,      ['bomb','wpn'], 'Collect hidden item'), #4x67
    LocInfo('L1 KillAll: Quiver',              RID.LEVEL_1_R,      ['kill','wpn'], 'Kill all enemies in a room'), #4x78
    LocInfo('L1 KillAll: Boss Key',            RID.LEVEL_1_R,      ['kill','bkey','wpn_restr','no_arrow','no_fire','no_wand'], 'Kill all enemies in a room'), #4x68
    LocInfo('L1 Boss Reward',                  RID.LEVEL_1_B,      ['wpn_restr','no_fire'], 'Kill the L1 Boss'), #4x64
    LocInfo('L1 Dungeon Reward',               RID.LEVEL_1_B,      ['wpn_restr','no_fire'], 'Beat L1'), #4x65
    LocInfo('L2 KillAll: Map',                 RID.LEVEL_2,        ['kill','wpn','map'], 'Kill all enemies left of start of the level'), #4x7C
    LocInfo('L2 KillAll: Compass',             RID.LEVEL_2,        ['kill','wpn','compass'], 'Kill all enemies right of start of the level'), #4x7#
    LocInfo('L2 KillAll: Sword',               RID.LEVEL_2,        ['kill','wpn'], 'Kill all enemies in the middle-right of the level'), #4x6F
    LocInfo('L2 KillAll: LKey',                RID.LEVEL_2,        ['kill','wpn','key'], 'Kill all enemies in the bottom-right of the level'), #4x7F
    LocInfo('L2: Bottle',                      RID.LEVEL_2,        [], 'Collect loose item'), #4x4F
    LocInfo('L2 KillAll: Heart Ring',          RID.LEVEL_2,        ['kill','wpn'], 'Kill all enemies in the middle-left of the level'), #4x6B
    LocInfo('L2 KillAll: Boss Key',            RID.LEVEL_2,        ['kill','wpn','bkey'], 'Kill all enemies in the bottom-left of the level'), #4x7F
    LocInfo('L2: Coupon',                      RID.LEVEL_2,        [], 'Collect loose item'), #4x4B
    LocInfo('L2 KillAll: Bomb Ammo',           RID.LEVEL_2,        [], 'Kill  all enemies above the boss room'), #4x4D
    LocInfo('L2 Boss Reward',                  RID.LEVEL_2_B,      ['bombs'], 'Kill the L2 Boss'), #4x5D
    LocInfo('L2 Dungeon Reward',               RID.LEVEL_2_B,      ['bombs'], 'Beat L2'), #4x6D
    LocInfo('L3: Roc\'s Feather',              RID.LEVEL_3_F,      [], 'Collect loose item 1st room'), #4x00
    LocInfo('L3 KillAll: Map',                 RID.LEVEL_3,        ['kill','wpn','map'], 'Kill all enemies 2nd room'), #4x01
    LocInfo('L3: LKey',                        RID.LEVEL_3,        ['key'], 'Grab loose item 3rd room'), #4x02
    LocInfo('L3 KillAll: Compass',             RID.LEVEL_3_R,      ['kill','wpn','compass'], 'Kill all enemies 4th room'), #4x03
    LocInfo('L3 KillAll: Bracelet',            RID.LEVEL_3_R,      ['kill','wpn'], 'Kill all enemies left path'), #4x12
    LocInfo('L3 KillAll: Hookshot',            RID.LEVEL_3_R,      ['kill','wpn'], 'Kill all enemies right path'), #4x14
    LocInfo('L3: Boss Key',                    RID.LEVEL_3_R2,     ['bkey'], 'Grab loose item using hookshot'), #4x13
    LocInfo('L3 KillAll: Charge Ring',         RID.LEVEL_3_R2,     ['kill','wpn'], 'Kill all enemies 6th room'), #4x05
    LocInfo('L3 Boss Reward',                  RID.LEVEL_3_B,      ['wpn'], 'Kill the L3 Boss'), #4x06
    LocInfo('L3 Dungeon Reward',               RID.LEVEL_3_B,      ['wpn'], 'Beat L3'), #4x07
    LocInfo('L4: Map',                         RID.LEVEL_4_F,      ['map'], 'Collect loose item'), #4x20
    LocInfo('L4: Roc\'s Cape',                 RID.LEVEL_4_F,      ['jump'], 'Collect loose item'), #4x30
    LocInfo('L4: Bomb Bag',                    RID.LEVEL_4,        [], 'Collect loose item'), #4x21
    LocInfo('L4: Boomerang',                   RID.LEVEL_4,        [], 'Collect loose item on the ledge'), #4x33
    LocInfo('L4: Compass',                     RID.LEVEL_4,        ['kill','wpn','compass'], 'Kill all enemies in the pit'), #4x43
    LocInfo('L4: Longshot',                    RID.LEVEL_4,        ['kill','wpn'], 'Kill all enemies in the pre-boss room'), #4x24
    LocInfo('L4 Boss Reward',                  RID.LEVEL_4,        ['melee'], 'Kill the L4 Boss'), #4x25
    LocInfo('L4 Dungeon Reward',               RID.LEVEL_4,        ['melee'], 'Beat L4'), #4x26
    LocInfo('L5 KillAll: Compass',             RID.LEVEL_5,        ['kill','wpn','compass'], 'Kill all enemies in a room'), #5x6D
    LocInfo('L5 KillAll: Bomb Ammo',           RID.LEVEL_5,        ['kill','wpn'], 'Kill all enemies in a room'), #5x7A
    LocInfo('L5 KillAll: Hidden LKey',         RID.LEVEL_5,        ['kill','wpn','bomb','key'], 'Bomb the wall, and kill the enemies inside'), #5x6A
    LocInfo('L5 KillAll: Map',                 RID.LEVEL_5_U,      ['kill','wpn','map'], 'Kill all enemies in a room'), #5x6B
    LocInfo('L5 KillAll: Escape Spell',        RID.LEVEL_5_U,      ['kill','wpn'], 'Kill all enemies in a room'), #5x6C
    LocInfo('L5 KillAll: Bottle',              RID.LEVEL_5_U,      ['kill','wpn'], 'Kill all enemies in a room'), #5x7B
    LocInfo('L5: Bracelet 2',                  RID.LEVEL_5_U,      ['heavy','wpn'], 'Kill the golden Goriya and push the heavy block to access the bottom room'), #5x7D
    LocInfo('L5 KillAll: Magic Ring',          RID.LEVEL_5_U,      ['kill','wpn'], 'Kill all enemies in a room'), #5x5D
    LocInfo('L5 KillAll: Boss Key',            RID.LEVEL_5_U,      ['kill','bkey','heavy2','wpn_restr','no_arrow','no_fire','no_wand'], 'Push the very heavy heavy block to access the room, and kill the guards'), #5x4C
    LocInfo('L5 Boss Reward',                  RID.LEVEL_5_B,      ['wpn_restr','no_fire'], 'Kill the L5 Boss'), #5x5B
    LocInfo('L5 Dungeon Reward',               RID.LEVEL_5_B,      ['wpn_restr','no_fire'], 'Beat L5'), #5x5A
    LocInfo('L6: Compass',                     RID.LEVEL_6_1F_F,   ['compass'], 'Collect loose item in first room'), #6x56
    LocInfo('L6 KillAll: Map',                 RID.LEVEL_6_1F_F,   ['map'], 'Collect loose item in first room'), #6x46
    LocInfo('L6: Hidden Money',                RID.LEVEL_6_1F_F,   ['bomb','wpn'], 'Bomb the wall'), #6x55
    LocInfo('L6 KillAll: Bottle',              RID.LEVEL_6_1F_F,   ['kill','wpn'], 'Kill all golden goriyas in a room'), #6x47
    LocInfo('L6 KillAll: Money 1',             RID.LEVEL_6_1F_F,   ['kill','wpn_restr','no_arrow','no_fire','no_wand'], 'Kill all red darknuts in a room'), #6x57
    LocInfo('L6: Dragon Miniboss',             RID.LEVEL_6_1F_F,   ['melee'], 'Kill the 6-headed dragon'), #6x58
    LocInfo('L6 KillAll: Wand',                RID.LEVEL_6_1F_F,   ['kill','melee'], 'Kill all golden goriyas in a room'), #6x48
    LocInfo('L6 KillAll: Charge Ring',         RID.LEVEL_6_1F_B,   ['kill','wpn'], 'Kill all leevers in a room'), #6x18
    LocInfo('L6 KillAll: Money 2',             RID.LEVEL_6_1F_B,   ['kill','wpn'], 'Kill all blue moblins in a room'), #6x16
    LocInfo('L6: LKey 1',                      RID.LEVEL_6_1F_L,   ['key'], 'Get to the bottom-left room'), #6x54
    LocInfo('L6 KillAll: LKey 2',              RID.LEVEL_6_2F_F,   ['kill','wpn','key'], 'Kill all the purple leevers in a room'), #6x42
    LocInfo('L6 KillAll: Boss Key',            RID.LEVEL_6_2F_B,   ['kill','wpn','bkey'], 'Kill all the fire octos in a room'), #6x22
    LocInfo('L6 KillAll: Quiver',              RID.LEVEL_6_2F_B,   ['kill','melee'], 'Kill the 3-headed dragon'), #6x23
    LocInfo('L6 Boss Reward',                  RID.LEVEL_6_B,      ['arrow'], 'Kill the L6 Boss'), #6x32
    LocInfo('L6 Dungeon Reward',               RID.LEVEL_6_B,      ['arrow'], 'Beat L6'), #6x30
    LocInfo('L9: Tunic Path',                  RID.LEVEL_9,        [], 'Item after the gold tunic gauntlet'), #3x4A
    ]
location_name_to_id = {loc.name: num for num,loc in enumerate(location_table,base_number_id)}
