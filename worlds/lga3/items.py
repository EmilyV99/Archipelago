from typing import NamedTuple
from BaseClasses import MultiWorld, Item, ItemClassification
from .common import *
from .options import LGA3_Options

class LGA3_Item(Item):
    game = 'Link\'s Grand Adventure 3: Remastered'
class ItemInfo(NamedTuple):
    name: str
    desc: str
    flag: ItemClassification
item_table = [
    ItemInfo('Nothing', 'A junk item', ItemClassification.filler),
    ItemInfo('Progressive Sword', 'A sword upgrade', ItemClassification.progression),
    ItemInfo('Progressive Tunic', 'An armor upgrade', ItemClassification.useful),
    ItemInfo('Progressive Bottle', 'An Empty Bottle', ItemClassification.progression),
    ItemInfo('Progressive Jump', 'A jump upgrade', ItemClassification.progression),
    ItemInfo('Hammer', 'The Hammer', ItemClassification.progression),
    ]
item_name_to_id = {name: num for num,(name,_desc,_) in enumerate(item_table,base_number_id)}

def include_item(itm: LGA3_Item, options: LGA3_Options) -> int:
    match itm.name:
        case 'Nothing':
            return 0
        case 'Progressive Sword':
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
    return 1
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
        multiworld.itempool += [itm for _ in range(count)]
    multiworld.itempool += [nothing_item for _ in range(junk)]
def create_item(name: str, player: int) -> LGA3_Item:
    itemid = item_name_to_id[name]
    _,desc,flag = item_table[itemid]
    return LGA3_Item(name, flag, itemid, player)

def create_event_itm(event: str, player: int) -> LGA3_Item:
    return LGA3_Item(event, True, None, player)