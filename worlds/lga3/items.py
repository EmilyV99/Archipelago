from typing import NamedTuple, Self
from BaseClasses import MultiWorld, Item, ItemClassification
from .common import *
from .options import LGA3_Options

class LGA3_Item(Item):
    game = game_disp_name
    def copy(self) -> Self:
        return LGA3_Item(self.name, self.classification, self.code, self.player)
class ItemInfo(NamedTuple):
    name: str
    desc: str
    flag: ItemClassification
item_table = [
    ItemInfo('Nothing', 'A junk item', ItemClassification.filler),
    ItemInfo('Progressive Sword', 'A sword upgrade', ItemClassification.progression),
    ItemInfo('Progressive Tunic', 'An armor upgrade', ItemClassification.progression),
    ItemInfo('Progressive Bottle', 'An Empty Bottle', ItemClassification.progression),
    ItemInfo('Progressive Jump', 'A jump upgrade', ItemClassification.progression),
    ItemInfo('Progressive Bomb Bag', 'A bomb capacity upgrade', ItemClassification.progression),
    ItemInfo('Progressive Quiver', 'An arrow capacity upgrade', ItemClassification.progression),
    ItemInfo('Progressive Magic Ring', 'A magic regen upgrade', ItemClassification.useful),
    ItemInfo('Progressive Life Ring', 'A life regen upgrade', ItemClassification.useful),
    ItemInfo('Progressive Charge Ring', 'A weapon charge speed upgrade', ItemClassification.useful),
    ItemInfo('Progressive Shield', 'A shield upgrade', ItemClassification.progression),
    ItemInfo('Progressive Boomerang', 'A boomerang upgrade', ItemClassification.useful),
    ItemInfo('Progressive Lantern', 'A lantern upgrade', ItemClassification.useful),
    ItemInfo('Progressive Wallet', 'Increases max money', ItemClassification.progression),
    ItemInfo('Progressive Coupon', 'Decreases shop prices', ItemClassification.progression),
    ItemInfo('Progressive Bracelet', 'Increase pushing strength', ItemClassification.progression),
    ItemInfo('Progressive Hookshot', 'Hook to far targets', ItemClassification.progression),
    ItemInfo('Bow', 'The Bow, to shoot arrows with', ItemClassification.progression),
    ItemInfo('Magic Book', 'The Magic Book, powers up the Wand', ItemClassification.progression),
    ItemInfo('Hammer', 'The Hammer', ItemClassification.progression),
    ItemInfo('Magic Rock', 'Hints towards nearby secrets', ItemClassification.progression),
    ItemInfo('Divine Fire', 'Blasts the whole screen in Divine Fire', ItemClassification.progression),
    ItemInfo('Flippers', 'Lets you swim/dive', ItemClassification.progression),
    ItemInfo('Ocarina', 'Lets you fast-travel', ItemClassification.useful),
    ItemInfo('Heart Container', 'Extra max life', ItemClassification.useful),
    ItemInfo('Magic Container', 'Extra max magic', ItemClassification.progression),
    ItemInfo('Triforce Fragment', 'MacGuffin', ItemClassification.progression),
    ItemInfo('Bomb Ammo x4', '4 Bombs', ItemClassification.filler),
    ItemInfo('Bomb Ammo x30', '30 Bombs', ItemClassification.filler),
    ItemInfo('Compass 1', 'Dungeon Compass for Level 1', ItemClassification.filler),
    ItemInfo('Compass 2', 'Dungeon Compass for Level 2', ItemClassification.filler),
    ItemInfo('Compass 3', 'Dungeon Compass for Level 3', ItemClassification.filler),
    ItemInfo('Compass 4', 'Dungeon Compass for Level 4', ItemClassification.filler),
    #ItemInfo('Compass 5', 'Dungeon Compass for Level 5', ItemClassification.filler),
    #ItemInfo('Compass 6', 'Dungeon Compass for Level 6', ItemClassification.filler),
    #ItemInfo('Compass 7', 'Dungeon Compass for Level 7', ItemClassification.filler),
    #ItemInfo('Compass 8', 'Dungeon Compass for Level 8', ItemClassification.filler),
    ItemInfo('Map 1', 'Dungeon Map for Level 1', ItemClassification.filler),
    ItemInfo('Map 2', 'Dungeon Map for Level 2', ItemClassification.filler),
    ItemInfo('Map 3', 'Dungeon Map for Level 3', ItemClassification.filler),
    ItemInfo('Map 4', 'Dungeon Map for Level 4', ItemClassification.filler),
    #ItemInfo('Map 5', 'Dungeon Map for Level 5', ItemClassification.filler),
    #ItemInfo('Map 6', 'Dungeon Map for Level 6', ItemClassification.filler),
    #ItemInfo('Map 7', 'Dungeon Map for Level 7', ItemClassification.filler),
    #ItemInfo('Map 8', 'Dungeon Map for Level 8', ItemClassification.filler),
    ItemInfo('LKey 1', 'Level Key for Level 1', ItemClassification.progression),
    ItemInfo('LKey 2', 'Level Key for Level 2', ItemClassification.progression),
    ItemInfo('LKey 3', 'Level Key for Level 3', ItemClassification.progression),
    #Non-existent #ItemInfo('LKey 4', 'Level Key for Level 4', ItemClassification.progression),
    #ItemInfo('LKey 5', 'Level Key for Level 5', ItemClassification.progression),
    #ItemInfo('LKey 6', 'Level Key for Level 6', ItemClassification.progression),
    #ItemInfo('LKey 7', 'Level Key for Level 7', ItemClassification.progression),
    #ItemInfo('LKey 8', 'Level Key for Level 8', ItemClassification.progression),
    ItemInfo('Boss Key 1', 'Boss Key for Level 1', ItemClassification.progression),
    ItemInfo('Boss Key 2', 'Boss Key for Level 2', ItemClassification.progression),
    ItemInfo('Boss Key 3', 'Boss Key for Level 3', ItemClassification.progression),
    #Non-existent #ItemInfo('Boss Key 4', 'Boss Key for Level 4', ItemClassification.progression),
    #ItemInfo('Boss Key 5', 'Boss Key for Level 5', ItemClassification.progression),
    #ItemInfo('Boss Key 6', 'Boss Key for Level 6', ItemClassification.progression),
    #ItemInfo('Boss Key 7', 'Boss Key for Level 7', ItemClassification.progression),
    #ItemInfo('Boss Key 8', 'Boss Key for Level 8', ItemClassification.progression),
    ]
item_name_to_id = {name: num for num,(name,_desc,_) in enumerate(item_table,base_number_id)}
key_counts = [0,1,1,0,0,0,0,0,0,0] #levels 0-9

def include_item_name(name: str, options: LGA3_Options) -> int:
    match name:
        case 'Nothing':
            return 0
        
        # Ammo / Collectables
        case 'Triforce Fragment':
            return 4 #!TODO more
        case 'Heart Container':
            return 7 #!TODO more
        case 'Magic Container':
            return 4 #!TODO more
        case 'Bomb Ammo x4':
            return 1
        case 'Bomb Ammo x30':
            return 1
        
        # 'Progressive' items
        case 'Progressive Sword': #SwordSanity settings
            if options.sword_sanity == 2:
                return 4
            if options.sword_sanity == 1:
                return 3
            return 0
        case 'Progressive Tunic':
            return 3
        case 'Progressive Bottle':
            return 4
        case 'Progressive Jump':
            return 2
        case 'Progressive Wallet':
            return 1 #!TODO more
        case 'Progressive Lantern':
            return 2
        case 'Progressive Boomerang':
            return 3
        case 'Progressive Bomb Bag':
            return 2 #!TODO more
        case 'Progressive Quiver':
            return 1 #!TODO more
        case 'Progressive Shield':
            return 2 #!TODO more
        case 'Progressive Coupon':
            return 1 #!TODO more
        case 'Progressive Bracelet':
            return 1 #!TODO more
        case 'Progressive Hookshot':
            return 2
        
        case 'Progressive Life Ring':
            return 2 #!TODO more
        case 'Progressive Magic Ring':
            return 2 #!TODO more
        case 'Progressive Charge Ring':
            return 1 #!TODO more
        
        # Other stuff
        case name if 'Compass' in name:
            return 1 if options.dungeon_item_sanity & 0b10 else 0
        case name if 'Map' in name:
            return 1 if options.dungeon_item_sanity & 0b01 else 0
        case name if 'LKey' in name:
            assert name[-1].isnumeric(), 'LKey item names must end in a level number'
            return key_counts[int(name[-1])] if options.key_sanity > 1 else 0
        case name if 'Boss Key' in name:
            return 1 if options.key_sanity > 0 else 0
    return 1
def include_item(itm: LGA3_Item, options: LGA3_Options) -> int:
    return include_item_name(itm.name, options)
def create_items(multiworld: MultiWorld, player: int, options: LGA3_Options) -> None:
    exclude = [item for item in multiworld.precollected_items[player]]
    
    nothing_item = LGA3_Item(item_table[0].name, item_table[0].flag, 0, player)
    junk = 0
    for itemid,(name,desc,flag) in enumerate(item_table,base_number_id):
        itm = LGA3_Item(name, flag, itemid, player)
        count = include_item(itm, options)
        while itm in exclude and count > 0:
            exclude.remove(itm)
            junk += 1
            count -= 1
        multiworld.itempool += [itm.copy() for _ in range(count)]
    multiworld.itempool += [nothing_item.copy() for _ in range(junk)]
def create_item(name: str, player: int) -> LGA3_Item:
    itemid = item_name_to_id[name]-base_number_id
    _,desc,flag = item_table[itemid]
    return LGA3_Item(name, flag, itemid, player)

def create_event_item(event: str, player: int) -> LGA3_Item:
    return LGA3_Item(event, ItemClassification.progression, None, player)