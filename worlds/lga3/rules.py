import typing
from BaseClasses import MultiWorld, Item, ItemClassification
from ..generic.Rules import set_rule
from .common import *
from .options import LGA3_Options
from .regions import region_map

def set_rules(multiworld: MultiWorld, player: int, options: LGA3_Options) -> None:
    region_map[-1].connect(connecting_region=region_map[0], rule = lambda state: True)
    region_map[0].connect(connecting_region=region_map[1], rule = lambda state: True)
    region_map[0].connect(connecting_region=region_map[2], rule = lambda state: True)
    region_map[0].connect(connecting_region=region_map[3], rule = lambda state: True)
    region_map[0].connect(connecting_region=region_map[4], rule = lambda state: True) # Needs Hookshot
    region_map[0].connect(connecting_region=region_map[5], rule = lambda state: True) # Needs Flippers
    region_map[0].connect(connecting_region=region_map[6], rule = lambda state: True)
    region_map[0].connect(connecting_region=region_map[7], rule = lambda state: True) # Needs Lens
    region_map[0].connect(connecting_region=region_map[8], rule = lambda state: True)
    region_map[0].connect(connecting_region=region_map[9], rule = lambda state: True) # Needs All Triforce
    
    set_rule(multiworld.get_location('Sword Under Tree', player),
        lambda state: state.has('Progressive Sword',3))
    
    multiworld.get_location('Ganon', player).place_locked_item(create_event_itm('Victory', player))
    multiworld.completion_condition[player] = lambda state: state.has('Victory', player)

