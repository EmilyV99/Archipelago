from typing import List, Optional, Dict, Set, Callable, Union, Iterable
from worlds.AutoWorld import World
from BaseClasses import Location, Entrance
from ..generic.Rules import set_rule, add_rule
from .common import *
from .items import create_event_item, create_item, include_item_name
from .locations import LGA3_Location, LocInfo, location_table
from .options import Goal

def set_rules(world: World) -> None:
    multiworld = world.multiworld
    player = world.player
    options = world.options
    all_rules: Set[Callable] = set()
    def use_rule(rule: Callable) -> Callable:
        all_rules.add(rule)
        return rule
    
    def _set_rule_name(name: str, rule: Callable) -> None:
        set_rule(multiworld.get_location(name,player), use_rule(rule))
    def _add_rule_name(name: str, rule: Callable) -> None:
        add_rule(multiworld.get_location(name,player), use_rule(rule))
    def _set_rule(spot: Union[Location, Entrance], rule: Callable) -> None:
        set_rule(spot, use_rule(rule))
    def _add_rule(spot: Union[Location, Entrance], rule: Callable) -> None:
        add_rule(spot, use_rule(rule))
    def _set_rules_name(name: str, rules: Iterable[Callable]) -> None:
        loc = multiworld.get_location(name,player)
        first = True
        for rule in rules:
            if first:
                first = False
                _set_rule(loc, rule)
            else:
                _add_rule(loc, rule)
    
    grind_rule = lambda state: sword_1_rule(state) or state.has('Progressive Boomerang',player) or candle_2_rule(state)
    magic_grind_rule = lambda state: grind_rule(state) or state.has('Progressive Magic Ring',player)
    bomb_rule = lambda state: state.has('Progressive Bomb Bag',player) and grind_rule(state)
    arrow_rule = lambda state: state.has('Progressive Quiver',player) and state.has('Bow',player) and state.has('Progressive Arrows',player) and grind_rule(state)
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
    wand_rule = lambda state: state.has('Wand',player) and magic_grind_rule(state)
    
    divine_prot_rule = lambda state: state.has('Divine Protection',player) and state.has('Magic Container',player,2) and magic_grind_rule(state)
    basic_fighter_rule = lambda state: sword_1_rule(state) or arrow_rule(state) or hammer_rule(state)
    fighter_rule = lambda state: sword_2_rule(state) or (sword_1_rule(state) and arrow_rule(state)) or hammer_rule(state)
    tough_fight_rule = lambda state: (sword_3_rule(state) and tunic_1_rule(state)) or ((sword_2_rule(state) or hammer_rule(state)) and (divine_prot_rule(state) or tunic_2_rule(state)))
    
    #weapon_rules = [('no_arrow',arrow_rule),('no_bomb',bomb_rule),('no_sword',sword_1_rule),('no_hammer',hammer_rule),('no_fire',candle_2_rule),('no_wand',wand_rule)]
    weapon_nofire_rule = lambda state: bomb_rule(state) or arrow_rule(state) or melee_rule(state) or wand_rule(state)
    weapon_rule = lambda state: weapon_nofire_rule(state) or candle_2_rule(state)
    bombmelee_rule = lambda state: bomb_rule(state) or melee_rule(state)
    
    jump_1_rule = lambda state: state.has('Progressive Jump',player)
    jump_2_rule = lambda state: state.has('Progressive Jump',player,2)
    distant_fire_rule = lambda state: state.has('Progressive Boomerang',player,3) or (magic_grind_rule(state) and (state.has('Divine Fire',player) or state.has_all(['Wand','Magic Book'],player)))
    
    heavy_1_rule = lambda state: state.has('Progressive Bracelet',player)
    heavy_2_rule = lambda state: state.has('Progressive Bracelet',player,2)
    flipper_rule = lambda state: state.has('Flippers',player)
    hook_rule = lambda state: state.has('Progressive Hookshot',player)
    lens_rule = lambda state: state.has('Lens of Truth',player) and magic_grind_rule(state)
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
        def connect_region(r1: RID, r2: RID, rule: Optional[Callable] = None) -> None:
            if rule:
                world.get_region(r1).connect(connecting_region = world.get_region(r2), rule = use_rule(rule))
            else:
                world.get_region(r1).connect(connecting_region = world.get_region(r2))
        connect_region(RID.MENU, RID.GRASSLAND)
        
        connect_region(RID.GRASSLAND, RID.KAKARIKO)
        connect_region(RID.GRASSLAND, RID.MOUNTAIN, basic_fighter_rule)
        connect_region(RID.GRASSLAND, RID.DESERT, fighter_rule)
        connect_region(RID.GRASSLAND, RID.GRAVEYARD, fighter_rule)
        connect_region(RID.GRASSLAND, RID.ICE, fighter_rule)
        
        connect_region(RID.KAKARIKO, RID.LEVEL_1)
        
        connect_region(RID.LEVEL_1, RID.LEVEL_1_R, lambda state: key_rule(state,1))
        connect_region(RID.LEVEL_1_R, RID.LEVEL_1_B, lambda state: bkey_rule(state,1))
        
        connect_region(RID.GRASSLAND, RID.LEVEL_2, basic_fighter_rule)
        connect_region(RID.LEVEL_2, RID.LEVEL_2_B, lambda state: key_rule(state,2) and bkey_rule(state,2))
        
        connect_region(RID.MOUNTAIN, RID.LEVEL_3_F)
        connect_region(RID.LEVEL_3_F, RID.LEVEL_3, jump_1_rule)
        connect_region(RID.LEVEL_3, RID.LEVEL_3_R, lambda state: key_rule(state,3))
        connect_region(RID.LEVEL_3_R, RID.LEVEL_3_R2, hook_rule)
        connect_region(RID.LEVEL_3_R2, RID.LEVEL_3_B, lambda state: bkey_rule(state,3))
        
        connect_region(RID.MOUNTAIN, RID.LEVEL_4_F, hook_rule)
        connect_region(RID.LEVEL_4_F, RID.LEVEL_4, jump_2_rule)
        
        connect_region(RID.GRASSLAND, RID.LEVEL_5, flipper_rule)
        connect_region(RID.LEVEL_5, RID.LEVEL_5_U, lambda state: key_rule(state,5))
        connect_region(RID.LEVEL_5_U, RID.LEVEL_5_B, lambda state: bkey_rule(state,5))
        
        connect_region(RID.DESERT, RID.LEVEL_6_1F_F)
        connect_region(RID.LEVEL_6_1F_F, RID.LEVEL_6_1F_B, wand_rule)
        connect_region(RID.LEVEL_6_1F_F, RID.LEVEL_6_B, lambda state: bkey_rule(state,6) and weapon_rule(state))
        connect_region(RID.LEVEL_6_1F_B, RID.LEVEL_6_1F_L)
        connect_region(RID.LEVEL_6_1F_F, RID.LEVEL_6_2F_F, lambda state: key_rule(state,6) and weapon_rule(state))
        connect_region(RID.LEVEL_6_2F_F, RID.LEVEL_6_2F_B, lambda state: key_rule(state,6,2) and melee_rule(state) and distant_fire_rule(state))
        connect_region(RID.LEVEL_6_2F_F, RID.LEVEL_6_1F_L, lambda state: key_rule(state,6,2) and melee_rule(state))
        
        connect_region(RID.GRAVEYARD, RID.THE_WELL)
        connect_region(RID.GRAVEYARD, RID.LEVEL_7, lens_rule)
        connect_region(RID.LEVEL_7, RID.LEVEL_7_O, melee_rule)
        connect_region(RID.LEVEL_7, RID.LEVEL_7_C, lambda state: key_rule(state,7) and shield_3_rule(state))
        connect_region(RID.LEVEL_7_C, RID.LEVEL_7_B, lambda state: key_rule(state,7,2) and bkey_rule(state,7))
        
        connect_region(RID.ICE, RID.LEVEL_8, lambda state: lens_rule(state) and tunic_1_rule(state) and state.has('Progressive Traction',player,2))
        connect_region(RID.LEVEL_8, RID.LEVEL_8_G, lambda state: bomb_rule(state) and melee_rule(state))
        connect_region(RID.LEVEL_8_G, RID.LEVEL_8_U, arrow_rule)
        connect_region(RID.LEVEL_8_U, RID.LEVEL_8_B, lambda state: bkey_rule(state,8))
        
        tri_count = include_item_name('Triforce Fragment', options)
        connect_region(RID.DESERT, RID.LEVEL_9, lambda state: state.has('Triforce Fragment', player, tri_count) and bomb_rule(state) and tough_fight_rule(state))
        connect_region(RID.LEVEL_9, RID.LEVEL_9_B, lambda state: bkey_rule(state,9))
    
    locs_list: List[LGA3_Location] = multiworld.get_locations(player)
    
    # Apply uncommon rules directly
    _set_rule_name('Well: Bomb Bag', bomb_rule)
    _set_rules_name('Well: Lens', [lambda state: state.has('Progressive Bomb Bag',player,3), grind_rule, lambda state: state.has('Cheese',player)])
    _set_rules_name('Well: Green Potion', [grind_rule, lambda state: state.has('Progressive Quiver',player)])
    _set_rules_name('Well: Cheese', [grind_rule, pay_1_2, lambda state: state.has_all(['Progressive Quiver','Progressive Bottle','Potion (Red)','Potion (Green)','Potion (Blue)'],player)])
    _set_rule_name('L7 KillAll: Money', lambda state: key_rule(state,7,2))
    _set_rules_name('Divine Protection', [magic_grind_rule, lambda state: state.has('Divine Fire',player)])
    _set_rules_name('L9: Magic Path', [magic_grind_rule, lambda state: state.has_all(['Divine Fire','Divine Protection','Divine Escape'],player)])
    _set_rule_name('L9: Arrow Path', lambda state: state.has('Progressive Quiver',player,2))
    _set_rules_name('24-Headed Dragon', [divine_prot_rule, lambda state: (state.has('Magic Container',player,6) or state.has('Half Magic',player) or state.has('Progressive Magic Ring',player,3))])
    # Apply common rules via tags
    for loc in locs_list:
        if loc.info is None:
            continue
        tags = loc.info.tags
        
        if options.magic_rock_for_kill_all:
            if 'kill' in tags:
                _add_rule(loc, magic_rock_rule)
                
        if 'wpn_bomb_melee' in tags:
            _add_rule(loc, bombmelee_rule)
        elif 'wpn_no_fire' in tags:
            _add_rule(loc, weapon_nofire_rule)
        elif 'wpn' in tags:
            _add_rule(loc, weapon_rule)
        
        if 'melee' in tags:
            _add_rule(loc, melee_rule)
        
        if 'bomb' in tags:
            _add_rule(loc, bomb_rule)
        
        if 'arrow2' in tags:
            _add_rule(loc, arrow_2_rule)
        elif 'arrow' in tags:
            _add_rule(loc, arrow_rule)
        
        if 'jump2' in tags:
            _add_rule(loc, jump_2_rule)
        elif 'jump' in tags:
            _add_rule(loc, jump_1_rule)
        
        if 'sword4' in tags:
            _add_rule(loc, sword_4_rule)
        elif 'sword3' in tags:
            _add_rule(loc, sword_3_rule)
        elif 'sword2' in tags:
            _add_rule(loc, sword_2_rule)
        elif 'sword' in tags:
            _add_rule(loc, sword_1_rule)
        
        if 'shield3' in tags:
            _add_rule(loc, shield_3_rule)
        
        if 'tough_fight' in tags:
            _add_rule(loc, tough_fight_rule)
        
        if 'hidden' in tags:
            _add_rule(loc, hidden_rule)
        
        if 'shop' in tags:
            _add_rule(loc, grind_rule)
            if 'pay_1_1' in tags:
                _add_rule(loc, pay_1_1)
            elif 'pay_1_2' in tags:
                _add_rule(loc, pay_1_2)
            elif 'pay_1_3' in tags:
                _add_rule(loc, pay_1_3)
        
        if 'heavy2' in tags:
            _add_rule(loc, heavy_2_rule)
        elif 'heavy' in tags:
            _add_rule(loc, heavy_1_rule)
        
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
    victory_name: str
    hundred_percent = True
    kill_ganon = True
    if options.goal == Goal.option_ganon:
        victory_name = 'Beat Ganon'
        hundred_percent = False
    elif options.goal == Goal.option_hundred_percent:
        victory_name = '100% The Game'
        kill_ganon = False
    elif options.goal == Goal.option_hundred_percent_ganon:
        victory_name = '100% The Game And Beat Ganon'
    from_region: Region
    if kill_ganon:
        from_region = world.get_region(RID.LEVEL_9_B)
    else:
        from_region = world.get_region(RID.MENU)
    goal_region = world.get_region(RID.GOAL)
    victory = from_region.create_exit(f'{from_region.name} -> {goal_region.name}')
    if kill_ganon:
        add_rule(victory, sword_2_rule)
        add_rule(victory, arrow_2_rule)
    if hundred_percent:
        add_rule(victory, lambda state: all(rule(state) for rule in all_rules))
    multiworld.get_location('Goal', player).place_locked_item(create_event_item(victory_name, player))
    multiworld.completion_condition[player] = lambda state: state.has(victory_name, player)
    victory.connect(goal_region)

