from typing import List, Optional
from BaseClasses import MultiWorld, Item, ItemClassification
from ..generic.Rules import set_rule, add_rule, CollectionRule
from .common import *
from .items import create_event_item, create_item, include_item_name
from .locations import LGA3_Location, LocInfo, location_table
from .options import LGA3_Options
from .regions import region_map

def set_rules(multiworld: MultiWorld, player: int, options: LGA3_Options) -> None:
    bomb_rule = lambda state: state.has('Progressive Bomb Bag', player)
    jump_1_rule = lambda state: state.has('Progressive Jump', player)
    arrow_rule = lambda state: state.has('Progressive Quiver', player) and state.has('Bow', player)
    arrow_2_rule = lambda state: arrow_rule(state) and state.has('Progressive Arrows', player)
    rock_rule = lambda state: state.has('Magic Rock', player)
    sword_rule = lambda state,count=1: state.has('Progressive Sword', player, count)
    tunic_rule = lambda state,count=1: state.has('Progressive Tunic', player, count)
    weapon_rule = lambda state: bomb_rule(state) or arrow_rule(state) or sword_rule(state)
    basic_fighter_rule = lambda state: sword_rule(state) or arrow_rule(state)
    fighter_rule = lambda state: sword_rule(state,2) or (sword_rule(state) and arrow_rule(state))
    heavy_1_rule = lambda state: state.has('Progressive Bracelet',player)
    heavy_2_rule = lambda state: state.has('Progressive Bracelet',player,2)
    flipper_rule = lambda state: state.has('Flippers',player)
    hook_rule = lambda state: state.has('Progressive Hookshot',player)
    
    key_rule = lambda state,lvl,count=1: state.has(f'LKey {lvl}', player, count)
    bkey_rule = lambda state,lvl: state.has(f'Boss Key {lvl}', player)
    
    pay_1_1 = lambda state: state.has('Progressive Wallet', player) or state.has('Progressive Coupon', player)
    pay_1_2 = lambda state: state.has('Progressive Wallet', player) or state.has('Progressive Coupon', player, 2)
    pay_1_3 = lambda state: state.has('Progressive Wallet', player) or state.has('Progressive Coupon', player, 3)
    
    region_map[RID.MENU].connect(connecting_region=region_map[RID.GRASSLAND])
    
    region_map[RID.GRASSLAND].connect(connecting_region=region_map[RID.KAKARIKO])
    region_map[RID.GRASSLAND].connect(connecting_region=region_map[RID.MOUNTAIN],
        rule = basic_fighter_rule)
    region_map[RID.GRASSLAND].connect(connecting_region=region_map[RID.DESERT],
        rule = fighter_rule)
    region_map[RID.GRASSLAND].connect(connecting_region=region_map[RID.GRAVEYARD],
        rule = fighter_rule)
    region_map[RID.GRASSLAND].connect(connecting_region=region_map[RID.ICE],
        rule = fighter_rule)
    
    region_map[RID.KAKARIKO].connect(connecting_region=region_map[RID.LEVEL_1])
    
    region_map[RID.LEVEL_1].connect(connecting_region=region_map[RID.LEVEL_1_R],
        rule = lambda state: key_rule(state,1))
    region_map[RID.LEVEL_1_R].connect(connecting_region=region_map[RID.LEVEL_1_B],
        rule = lambda state: bkey_rule(state,1))
    
    region_map[RID.GRASSLAND].connect(connecting_region=region_map[RID.LEVEL_2],
        rule = basic_fighter_rule)
    region_map[RID.LEVEL_2].connect(connecting_region=region_map[RID.LEVEL_2_B],
        rule = lambda state: key_rule(state,2) and bkey_rule(state,2))
    
    region_map[RID.MOUNTAIN].connect(connecting_region=region_map[RID.LEVEL_3_F])
    region_map[RID.LEVEL_3_F].connect(connecting_region=region_map[RID.LEVEL_3],
        rule = jump_1_rule)
    region_map[RID.LEVEL_3].connect(connecting_region=region_map[RID.LEVEL_3_R],
        rule = lambda state: key_rule(state,3))
    region_map[RID.LEVEL_3_R].connect(connecting_region=region_map[RID.LEVEL_3_R2],
        rule = hook_rule)
    region_map[RID.LEVEL_3_R2].connect(connecting_region=region_map[RID.LEVEL_3_B],
        rule = lambda state: bkey_rule(state,3))
    region_map[RID.MOUNTAIN].connect(connecting_region=region_map[RID.LEVEL_4],
        rule = hook_rule)
    
    region_map[RID.GRASSLAND].connect(connecting_region=region_map[RID.LEVEL_5],
        rule = flipper_rule)
    
    region_map[RID.DESERT].connect(connecting_region=region_map[RID.LEVEL_6])
    region_map[RID.GRAVEYARD].connect(connecting_region=region_map[RID.LEVEL_7],
        rule = lambda state: True) # Needs Lens
    region_map[RID.ICE].connect(connecting_region=region_map[RID.LEVEL_8],
        rule = lambda state: True) # Needs Lens
    tri_count = include_item_name('Triforce Fragment', options)
    region_map[RID.DESERT].connect(connecting_region=region_map[RID.LEVEL_9],
        rule = lambda state: state.has('Triforce Fragment', player, tri_count))
    
    _set_rule = lambda name, rule: set_rule(multiworld.get_location(name, player), rule)
    
    _set_rule('Sword Under Tree', lambda state: sword_rule(state,3))
    _set_rule('L4: Roc\'s Cape', jump_1_rule)
    _set_rule('24-Headed Dragon', lambda state: (sword_rule(state,3) and tunic_rule(state)) or (sword_rule(state,2) and (state.has('Divine Protection',player) or tunic_rule(state,2))))
    
    locs_list: List[(LGA3_Location,LocInfo)] = []
    for locinfo in location_table:
        locs_list.append((multiworld.get_location(locinfo.name,player),locinfo))
    
    for loc,locinfo in locs_list:
        if 'kill' in locinfo.tags:
            if options.magic_rock_for_kill_all:
                add_rule(loc, rock_rule)
            add_rule(loc, weapon_rule)
        elif 'wpn' in locinfo.tags:
            add_rule(loc, weapon_rule)
        else: #these are contained inside weapon_rule
            if 'bomb' in locinfo.tags:
                add_rule(loc, bomb_rule)
            if 'arrow' in locinfo.tags:
                add_rule(loc, arrow_rule)
        
        if 'shop' in locinfo.tags:
            if 'pay_1_1' in locinfo.tags:
                add_rule(loc, pay_1_1)
            elif 'pay_1_2' in locinfo.tags:
                add_rule(loc, pay_1_2)
            elif 'pay_1_3' in locinfo.tags:
                add_rule(loc, pay_1_3)
        
        if 'heavy2' in locinfo.tags:
            add_rule(loc, heavy_2_rule)
        elif 'heavy' in locinfo.tags:
            add_rule(loc, heavy_1_rule)
        
        if 'key' in locinfo.tags:
            if options.key_sanity < 2:
                assert loc.name[0] == 'L' and loc.name[1].isnumeric(), 'Key loc name must start in "L#" where # = 1-9'
                itmname = 'LKey ' + loc.name[1]
                loc.place_locked_item(create_item(itmname, player))
        elif 'bkey' in locinfo.tags:
            if options.key_sanity < 1:
                assert loc.name[0] == 'L' and loc.name[1].isnumeric(), 'BKey loc name must start in "L#" where # = 1-9'
                itmname = 'Boss Key ' + loc.name[1]
                loc.place_locked_item(create_item(itmname, player))
        elif 'map' in locinfo.tags:
            if (options.dungeon_item_sanity & 0b01) == 0:
                assert loc.name[0] == 'L' and loc.name[1].isnumeric(), 'Map loc name must start in "L#" where # = 1-9'
                itmname = 'Map ' + loc.name[1]
                loc.place_locked_item(create_item(itmname, player))
        elif 'compass' in locinfo.tags:
            if (options.dungeon_item_sanity & 0b10) == 0:
                assert loc.name[0] == 'L' and loc.name[1].isnumeric(), 'Compass loc name must start in "L#" where # = 1-9'
                itmname = 'Compass ' + loc.name[1]
                loc.place_locked_item(create_item(itmname, player))
        
        if options.sword_sanity < 2 and loc.name == 'Starting Sword':
            loc.place_locked_item(create_item('Progressive Sword', player))
        if options.sword_sanity == 0 and loc.name in ['L2 KillAll: Sword','Sword Under Block','Sword Under Tree']:
            loc.place_locked_item(create_item('Progressive Sword', player))
        
    ganon_loc = multiworld.get_location('Ganon', player)
    set_rule(ganon_loc, lambda state: sword_rule(state,2) and arrow_rule(state)) #!TODO arrow_2_rule
    ganon_loc.place_locked_item(create_event_item('Victory', player))
    multiworld.completion_condition[player] = lambda state: state.has('Victory', player)

