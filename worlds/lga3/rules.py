import typing
from BaseClasses import MultiWorld, Item, ItemClassification
from ..generic.Rules import set_rule, CollectionRule
from .common import *
from .items import create_event_item
from .locations import include_location_name
from .options import LGA3_Options
from .regions import region_map

def try_set_rule(name: str, player: int, multiworld: MultiWorld, options: LGA3_Options, rule: CollectionRule):
    if include_location_name(name,options):
        set_rule(multiworld.get_location(name, player), rule)
    

def set_rules(multiworld: MultiWorld, player: int, options: LGA3_Options) -> None:
    region_map[RegionID.MENU].connect(connecting_region=region_map[RegionID.OVERWORLD], rule = lambda state: True)
    region_map[RegionID.OVERWORLD].connect(connecting_region=region_map[RegionID.LEVEL_1])
    region_map[RegionID.OVERWORLD].connect(connecting_region=region_map[RegionID.LEVEL_2])
    region_map[RegionID.OVERWORLD].connect(connecting_region=region_map[RegionID.LEVEL_3])
    region_map[RegionID.OVERWORLD].connect(connecting_region=region_map[RegionID.LEVEL_4], rule = lambda state: True) # Needs Hookshot
    region_map[RegionID.OVERWORLD].connect(connecting_region=region_map[RegionID.LEVEL_5], rule = lambda state: True) # Needs Flippers
    region_map[RegionID.OVERWORLD].connect(connecting_region=region_map[RegionID.LEVEL_6])
    region_map[RegionID.OVERWORLD].connect(connecting_region=region_map[RegionID.LEVEL_7], rule = lambda state: True) # Needs Lens
    region_map[RegionID.OVERWORLD].connect(connecting_region=region_map[RegionID.LEVEL_8])
    region_map[RegionID.OVERWORLD].connect(connecting_region=region_map[RegionID.LEVEL_9], rule = lambda state: True) # Needs All Triforce
    
    try_set_rule('Sword Under Tree', player, multiworld, options,
        lambda state: state.has('Progressive Sword', player, 3))
    
    multiworld.get_location('Ganon', player).place_locked_item(create_event_item('Victory', player))
    multiworld.completion_condition[player] = lambda state: state.has('Victory', player)

