from typing import Dict
from BaseClasses import Region
from worlds.AutoWorld import World
from .locations import location_table, LGA3_Location
from .common import *

def create_regions(world: World) -> None:
    multiworld = world.multiworld
    player = world.player
    
    for rid in RID:
        multiworld.regions.append(Region(rid, player, multiworld))
    
    for locid,locinfo in enumerate(location_table, base_number_id):
        region = world.get_region(locinfo.region_id)
        if region:
            region.locations.append(LGA3_Location(player, locinfo.name, locid, region, locinfo))
    l9boss = world.get_region(RID.LEVEL_9_B)
    l9boss.locations.append(LGA3_Location(player, 'Ganon', None, l9boss));

