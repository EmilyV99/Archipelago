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
    
    def _set_rule(name: str, rule):
        set_rule(multiworld.get_location(name,player), rule)
    def _add_rule(name: str, rule):
        add_rule(multiworld.get_location(name,player), rule)
    
    bomb_rule = lambda state: state.has('Progressive Bomb Bag',player)
    arrow_rule = lambda state: state.has('Progressive Quiver',player) and state.has('Bow',player) and state.has('Progressive Arrows',player)
    arrow_2_rule = lambda state: arrow_rule(state) and state.has('Progressive Arrows',player,2)
    candle_2_rule = lambda state: state.has('Progressive Lantern',player,2)
    magic_rock_rule = lambda state: state.has('Magic Rock',player)
    tunic_1_rule = lambda state: state.has('Progressive Tunic',player,1)
    tunic_2_rule = lambda state: state.has('Progressive Tunic',player,2)
    tunic_3_rule = lambda state: state.has('Progressive Tunic',player,3)
    sword_1_rule = lambda state: state.has('Progressive Sword',player,1)
    sword_2_rule = lambda state: state.has('Progressive Sword',player,2)
    sword_3_rule = lambda state: state.has('Progressive Sword',player,3)
    sword_4_rule = lambda state: state.has('Progressive Sword',player,4)
    hammer_rule = lambda state: state.has('Hammer',player)
    melee_rule = lambda state: sword_1_rule(state) or hammer_rule(state)
    wand_rule = lambda state: state.has('Wand',player)
    
    divine_prot_rule = lambda state: state.has('Divine Protection',player) and state.has('Magic Container',player,2)
    basic_fighter_rule = lambda state: sword_1_rule(state) or arrow_rule(state)
    fighter_rule = lambda state: sword_2_rule(state) or (sword_1_rule(state) and arrow_rule(state))
    tough_fight_rule = lambda state: (sword_3_rule(state) and tunic_1_rule(state)) or (sword_2_rule(state) and (divine_prot_rule(state) or tunic_2_rule(state)))
    
    #weapon_rules = [('no_arrow',arrow_rule),('no_bomb',bomb_rule),('no_sword',sword_1_rule),('no_hammer',hammer_rule),('no_fire',candle_2_rule),('no_wand',wand_rule)]
    weapon_nofire_rule = lambda state: bomb_rule(state) or arrow_rule(state) or melee_rule(state) or wand_rule(state)
    weapon_rule = lambda state: weapon_nofire_rule(state) or candle_2_rule(state)
    bombmelee_rule = lambda state: bomb_rule(state) or melee_rule(state)
    
    jump_1_rule = lambda state: state.has('Progressive Jump',player)
    jump_2_rule = lambda state: state.has('Progressive Jump',player,2)
    distant_fire_rule = lambda state: state.has('Divine Fire',player) or state.has('Progressive Boomerang',player,3) or state.has_all(['Wand','Magic Book'],player)
    
    heavy_1_rule = lambda state: state.has('Progressive Bracelet',player)
    heavy_2_rule = lambda state: state.has('Progressive Bracelet',player,2)
    flipper_rule = lambda state: state.has('Flippers',player)
    hook_rule = lambda state: state.has('Progressive Hookshot',player)
    lens_rule = lambda state: state.has('Lens of Truth',player)
    hidden_rule = lambda state: lens_rule(state) or magic_rock_rule(state)
    shield_3_rule = lambda state: state.has('Progressive Shield',player,3)
    
    key_rule = lambda state,lvl,count=1: state.has(f'LKey {lvl}',player,count)
    bkey_rule = lambda state,lvl: state.has(f'Boss Key {lvl}',player)
    
    pay_1_1 = lambda state: state.has('Progressive Wallet',player) or state.has('Progressive Coupon',player)
    pay_1_2 = lambda state: state.has('Progressive Wallet',player) or state.has('Progressive Coupon',player,2)
    pay_1_3 = lambda state: state.has('Progressive Wallet',player) or state.has('Progressive Coupon',player,3)
    
    
    #def make_wpn_rule(tags: List[str]):
        #used_wpn_rules = [rule for (bantag,rule) in weapon_rules if not bantag in tags]
        #def wpn_restr_rule(state):
            #for rule in used_wpn_rules:
                #if rule(state):
                    #return True
            #return False
        #return wpn_restr_rule
    
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
        
        world.get_region(RID.DESERT).connect(connecting_region = world.get_region(RID.LEVEL_6_1F_F))
        world.get_region(RID.LEVEL_6_1F_F).connect(connecting_region = world.get_region(RID.LEVEL_6_1F_B),
            rule = wand_rule)
        world.get_region(RID.LEVEL_6_1F_F).connect(connecting_region = world.get_region(RID.LEVEL_6_B),
            rule = lambda state: bkey_rule(state,6) and weapon_rule(state))
        world.get_region(RID.LEVEL_6_1F_B).connect(connecting_region = world.get_region(RID.LEVEL_6_1F_L))
        world.get_region(RID.LEVEL_6_1F_F).connect(connecting_region = world.get_region(RID.LEVEL_6_2F_F),
            rule = lambda state: key_rule(state,6) and weapon_rule(state))
        world.get_region(RID.LEVEL_6_2F_F).connect(connecting_region = world.get_region(RID.LEVEL_6_2F_B),
            rule = lambda state: key_rule(state,6,2) and melee_rule(state) and distant_fire_rule(state))
        world.get_region(RID.LEVEL_6_2F_F).connect(connecting_region = world.get_region(RID.LEVEL_6_1F_L),
            rule = lambda state: key_rule(state,6,2) and melee_rule(state))
        
        world.get_region(RID.GRAVEYARD).connect(connecting_region = world.get_region(RID.THE_WELL))
        world.get_region(RID.GRAVEYARD).connect(connecting_region = world.get_region(RID.LEVEL_7),
            rule = lens_rule)
        world.get_region(RID.LEVEL_7).connect(connecting_region = world.get_region(RID.LEVEL_7_O),
            rule = melee_rule)
        world.get_region(RID.LEVEL_7).connect(connecting_region = world.get_region(RID.LEVEL_7_C),
            rule = lambda state: key_rule(state,7) and shield_3_rule(state))
        world.get_region(RID.LEVEL_7_C).connect(connecting_region = world.get_region(RID.LEVEL_7_B),
            rule = lambda state: key_rule(state,7,2) and bkey_rule(state,7))
        
        world.get_region(RID.ICE).connect(connecting_region = world.get_region(RID.LEVEL_8),
            rule = lens_rule)
        world.get_region(RID.LEVEL_8).connect(connecting_region = world.get_region(RID.LEVEL_8_G),
            rule = lambda state: bomb_rule(state) and melee_rule(state))
        world.get_region(RID.LEVEL_8_G).connect(connecting_region = world.get_region(RID.LEVEL_8_U),
            rule = arrow_rule)
        world.get_region(RID.LEVEL_8_U).connect(connecting_region = world.get_region(RID.LEVEL_8_B),
            rule = lambda state: bkey_rule(state,8))
        
        
        tri_count = include_item_name('Triforce Fragment', options)
        world.get_region(RID.DESERT).connect(connecting_region = world.get_region(RID.LEVEL_9),
            rule = lambda state: state.has('Triforce Fragment', player, tri_count) and bomb_rule(state))
    
    locs_list: List[LGA3_Location] = multiworld.get_locations(player)
    
    # Apply uncommon rules directly
    _set_rule('Well: Bomb Bag', bomb_rule)
    _set_rule('Well: Lens', lambda state: state.has('Progressive Bomb Bag',player,3) and state.has('Cheese',player))
    _set_rule('Well: Green Potion', lambda state: state.has('Progressive Quiver',player))
    _set_rule('Well: Cheese', lambda state: state.has('Progressive Quiver',player) and state.has('Progressive Bottle',player)) #!TODO potion logic
    _set_rule('L7 KillAll: Money', lambda state: key_rule(state,7,2))
    _set_rule('Divine Protection', lambda state: state.has('Divine Fire',player))
    # Apply common rules via tags
    for loc in locs_list:
        if loc.info is None:
            continue
        tags = loc.info.tags
        
        if options.magic_rock_for_kill_all:
            if 'kill' in tags:
                add_rule(loc, magic_rock_rule)
                
        if 'wpn_bomb_melee' in tags:
            add_rule(loc, bombmelee_rule)
        elif 'wpn_no_fire' in tags:
            add_rule(loc, weapon_nofire_rule)
        elif 'wpn' in tags:
            add_rule(loc, weapon_rule)
        
        if 'melee' in tags:
            add_rule(loc, melee_rule)
        
        if 'bomb' in tags:
            add_rule(loc, bomb_rule)
        
        if 'arrow2' in tags:
            add_rule(loc, arrow_2_rule)
        elif 'arrow' in tags:
            add_rule(loc, arrow_rule)
        
        if 'jump2' in tags:
            add_rule(loc, jump_2_rule)
        elif 'jump' in tags:
            add_rule(loc, jump_1_rule)
        
        if 'sword4' in tags:
            add_rule(loc, sword_4_rule)
        elif 'sword3' in tags:
            add_rule(loc, sword_3_rule)
        elif 'sword2' in tags:
            add_rule(loc, sword_2_rule)
        elif 'sword' in tags:
            add_rule(loc, sword_1_rule)
        
        if 'shield3' in tags:
            add_rule(loc, shield_3_rule)
        
        if 'tough_fight' in tags:
            add_rule(loc, tough_fight_rule)
        
        if 'hidden' in tags:
            add_rule(loc, hidden_rule)
        
        if 'shop' in tags:
            if 'pay_1_1' in tags:
                add_rule(loc, pay_1_1)
            elif 'pay_1_2' in tags:
                add_rule(loc, pay_1_2)
            elif 'pay_1_3' in tags:
                add_rule(loc, pay_1_3)
        
        if 'heavy2' in tags:
            add_rule(loc, heavy_2_rule)
        elif 'heavy' in tags:
            add_rule(loc, heavy_1_rule)
        
        if 'key' in tags:
            if options.key_sanity < 2:
                assert loc.name[0] == 'L' and loc.name[1].isnumeric(), 'Key loc name must start in "L#" where # = 1-9'
                itmname = 'LKey ' + loc.name[1]
                loc.place_locked_item(create_item(itmname, player))
        elif 'bkey' in tags:
            if options.key_sanity < 1:
                assert loc.name[0] == 'L' and loc.name[1].isnumeric(), 'BKey loc name must start in "L#" where # = 1-9'
                itmname = 'Boss Key ' + loc.name[1]
                loc.place_locked_item(create_item(itmname, player))
        elif 'map' in tags:
            if (options.dungeon_item_sanity & 0b01) == 0:
                assert loc.name[0] == 'L' and loc.name[1].isnumeric(), 'Map loc name must start in "L#" where # = 1-9'
                itmname = 'Map ' + loc.name[1]
                loc.place_locked_item(create_item(itmname, player))
        elif 'compass' in tags:
            if (options.dungeon_item_sanity & 0b10) == 0:
                assert loc.name[0] == 'L' and loc.name[1].isnumeric(), 'Compass loc name must start in "L#" where # = 1-9'
                itmname = 'Compass ' + loc.name[1]
                loc.place_locked_item(create_item(itmname, player))
        
        if options.sword_sanity < 2 and loc.name == 'Starting Sword':
            loc.place_locked_item(create_item('Progressive Sword', player))
        if options.sword_sanity == 0 and loc.name in ['L2 KillAll: Sword','Sword Under Block','Sword Under Tree']:
            loc.place_locked_item(create_item('Progressive Sword', player))
    
    # Set up the victory condition event
    ganon_loc = multiworld.get_location('Ganon', player)
    set_rule(ganon_loc, lambda state: sword_2_rule(state) and arrow_2_rule(state))
    ganon_loc.place_locked_item(create_event_item('Victory', player))
    multiworld.completion_condition[player] = lambda state: state.has('Victory', player)

