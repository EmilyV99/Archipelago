from typing import List, Optional, Dict
from worlds.AutoWorld import World
from ..generic.Rules import set_rule, add_rule
from .common import *
from .items import create_event_item, create_item, include_item_name
from .locations import LGA3_Location, LocInfo, location_table

def set_rules(world: World) -> None:
    multiworld = world.multiworld
    player = world.player
    options = world.options
    
    bomb_rule = lambda state: state.has('Progressive Bomb Bag', player)
    jump_1_rule = lambda state: state.has('Progressive Jump', player)
    jump_2_rule = lambda state: state.has('Progressive Jump', player, 2)
    arrow_rule = lambda state: state.has('Progressive Quiver', player) and state.has('Bow', player)
    arrow_2_rule = lambda state: arrow_rule(state) and state.has('Progressive Arrows', player)
    candle_2_rule = lambda state: state.has('Progressive Lantern',player,2)
    wand_rule = lambda state: state.has('Wand',player)
    rock_rule = lambda state: state.has('Magic Rock', player)
    tunic_1_rule = lambda state: state.has('Progressive Tunic',player,1)
    tunic_2_rule = lambda state: state.has('Progressive Tunic',player,2)
    tunic_3_rule = lambda state: state.has('Progressive Tunic',player,3)
    sword_1_rule = lambda state: state.has('Progressive Sword',player,1)
    sword_2_rule = lambda state: state.has('Progressive Sword',player,2)
    sword_3_rule = lambda state: state.has('Progressive Sword',player,3)
    sword_4_rule = lambda state: state.has('Progressive Sword',player,4)
    hammer_rule = lambda state: state.has('Hammer',player)
    melee_rule = lambda state: sword_1_rule(state) or hammer_rule(state)
    
    basic_fighter_rule = lambda state: sword_1_rule(state) or arrow_rule(state)
    fighter_rule = lambda state: sword_2_rule(state) or (sword_1_rule(state) and arrow_rule(state))
    heavy_1_rule = lambda state: state.has('Progressive Bracelet',player)
    heavy_2_rule = lambda state: state.has('Progressive Bracelet',player,2)
    flipper_rule = lambda state: state.has('Flippers',player)
    hook_rule = lambda state: state.has('Progressive Hookshot',player)
    
    key_rule = lambda state,lvl,count=1: state.has(f'LKey {lvl}', player, count)
    bkey_rule = lambda state,lvl: state.has(f'Boss Key {lvl}', player)
    
    pay_1_1 = lambda state: state.has('Progressive Wallet', player) or state.has('Progressive Coupon', player)
    pay_1_2 = lambda state: state.has('Progressive Wallet', player) or state.has('Progressive Coupon', player, 2)
    pay_1_3 = lambda state: state.has('Progressive Wallet', player) or state.has('Progressive Coupon', player, 3)
    
    divine_prot_rule = lambda state: state.has('Divine Protection',player) and state.has('Magic Container',player,2)
    tough_fight_rule = lambda state: (sword_3_rule(state) and tunic_1_rule(state)) or (sword_2_rule(state) and (divine_prot_rule(state) or tunic_2_rule(state)))
    
    weapon_rules = [('no_arrow',arrow_rule),('no_bomb',bomb_rule),('no_sword',sword_1_rule),('no_hammer',hammer_rule),('no_fire',candle_2_rule),('no_wand',wand_rule)]
    weapon_rule = lambda state: bomb_rule(state) or arrow_rule(state) or sword_1_rule(state) or hammer_rule(state)
    
    def make_wpn_rule(tags: List[str]):
        if 'wpn_restr' in tags:
            used_wpn_rules = [rule for (bantag,rule) in weapon_rules if not bantag in tags]
            def wpn_restr_rule(state):
                for rule in used_wpn_rules:
                    if rule(state):
                        return True
                return False
            return wpn_restr_rule
        else:
            return weapon_rule
    
    if True: # Region connecting
        world.get_region(RID.MENU).connect(connecting_region = world.get_region(RID.GRASSLAND))
        
        world.get_region(RID.GRASSLAND).connect(connecting_region = world.get_region(RID.KAKARIKO))
        world.get_region(RID.GRASSLAND).connect(connecting_region = world.get_region(RID.MOUNTAIN),
            rule = basic_fighter_rule)
        world.get_region(RID.GRASSLAND).connect(connecting_region = world.get_region(RID.DESERT),
            rule = fighter_rule)
        world.get_region(RID.GRASSLAND).connect(connecting_region = world.get_region(RID.GRAVEYARD),
            rule = fighter_rule)
        world.get_region(RID.GRASSLAND).connect(connecting_region = world.get_region(RID.ICE),
            rule = fighter_rule)
        
        world.get_region(RID.KAKARIKO).connect(connecting_region = world.get_region(RID.LEVEL_1))
        
        world.get_region(RID.LEVEL_1).connect(connecting_region = world.get_region(RID.LEVEL_1_R),
            rule = lambda state: key_rule(state,1))
        world.get_region(RID.LEVEL_1_R).connect(connecting_region = world.get_region(RID.LEVEL_1_B),
            rule = lambda state: bkey_rule(state,1))
        
        world.get_region(RID.GRASSLAND).connect(connecting_region = world.get_region(RID.LEVEL_2),
            rule = basic_fighter_rule)
        world.get_region(RID.LEVEL_2).connect(connecting_region = world.get_region(RID.LEVEL_2_B),
            rule = lambda state: key_rule(state,2) and bkey_rule(state,2))
        
        world.get_region(RID.MOUNTAIN).connect(connecting_region = world.get_region(RID.LEVEL_3_F))
        world.get_region(RID.LEVEL_3_F).connect(connecting_region = world.get_region(RID.LEVEL_3),
            rule = jump_1_rule)
        world.get_region(RID.LEVEL_3).connect(connecting_region = world.get_region(RID.LEVEL_3_R),
            rule = lambda state: key_rule(state,3))
        world.get_region(RID.LEVEL_3_R).connect(connecting_region = world.get_region(RID.LEVEL_3_R2),
            rule = hook_rule)
        world.get_region(RID.LEVEL_3_R2).connect(connecting_region = world.get_region(RID.LEVEL_3_B),
            rule = lambda state: bkey_rule(state,3))
        
        world.get_region(RID.MOUNTAIN).connect(connecting_region = world.get_region(RID.LEVEL_4_F),
            rule = hook_rule)
        world.get_region(RID.LEVEL_4_F).connect(connecting_region = world.get_region(RID.LEVEL_4),
            rule = jump_2_rule)
        
        world.get_region(RID.GRASSLAND).connect(connecting_region = world.get_region(RID.LEVEL_5),
            rule = flipper_rule)
        world.get_region(RID.LEVEL_5).connect(connecting_region = world.get_region(RID.LEVEL_5_U),
            rule = lambda state: key_rule(state,5))
        world.get_region(RID.LEVEL_5_U).connect(connecting_region = world.get_region(RID.LEVEL_5_B),
            rule = lambda state: bkey_rule(state,5))
        
        world.get_region(RID.DESERT).connect(connecting_region = world.get_region(RID.LEVEL_6))
        world.get_region(RID.GRAVEYARD).connect(connecting_region = world.get_region(RID.LEVEL_7),
            rule = lambda state: True) # Needs Lens
        world.get_region(RID.ICE).connect(connecting_region = world.get_region(RID.LEVEL_8),
            rule = lambda state: True) # Needs Lens
        tri_count = include_item_name('Triforce Fragment', options)
        world.get_region(RID.DESERT).connect(connecting_region = world.get_region(RID.LEVEL_9),
            rule = lambda state: state.has('Triforce Fragment', player, tri_count) and bomb_rule(state))
    
    #_set_rule = lambda name, rule: set_rule(multiworld.get_location(name, player), rule)
    
    locs_list: List[(LGA3_Location,LocInfo)] = []
    for locinfo in location_table:
        locs_list.append((multiworld.get_location(locinfo.name,player),locinfo))
    
    for loc,locinfo in locs_list:
        need_wpn = False
        if 'kill' in locinfo.tags:
            if options.magic_rock_for_kill_all:
                add_rule(loc, rock_rule)
            need_wpn = True
        elif 'wpn' in locinfo.tags:
            need_wpn = True
        
        if need_wpn:
            add_rule(loc, make_wpn_rule(locinfo.tags))
        
        if 'melee' in locinfo.tags:
            add_rule(loc, melee_rule)
        
        if 'bomb' in locinfo.tags:
            add_rule(loc, bomb_rule)
        
        if 'arrow2' in locinfo.tags:
            add_rule(loc, arrow_2_rule)
        elif 'arrow' in locinfo.tags:
            add_rule(loc, arrow_rule)
        
        if 'jump2' in locinfo.tags:
            add_rule(loc, jump_2_rule)
        elif 'jump' in locinfo.tags:
            add_rule(loc, jump_1_rule)
        
        if 'sword4' in locinfo.tags:
            add_rule(loc, sword_4_rule)
        elif 'sword3' in locinfo.tags:
            add_rule(loc, sword_3_rule)
        elif 'sword2' in locinfo.tags:
            add_rule(loc, sword_2_rule)
        elif 'sword' in locinfo.tags:
            add_rule(loc, sword_1_rule)
        
        if 'tough_fight' in locinfo.tags:
            add_rule(loc, tough_fight_rule)
        
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
    set_rule(ganon_loc, lambda state: sword_2_rule(state) and arrow_rule(state)) #!TODO arrow_2_rule
    ganon_loc.place_locked_item(create_event_item('Victory', player))
    multiworld.completion_condition[player] = lambda state: state.has('Victory', player)

