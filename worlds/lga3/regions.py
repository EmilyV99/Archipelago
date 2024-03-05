import typing
from BaseClasses import MultiWorld, Region, Entrance, Location
from .locations import location_table, LGA3_Location, include_location
from .common import *
from .options import LGA3_Options

region_map: typing.Dict[int, Region]
def create_regions(multiworld: MultiWorld, player: int, options: LGA3_Options):
    region_map[-1] = Region('Menu', player, multiworld);
    region_map[0] = Region('Overworld', player, multiworld)
    region_map[1] = Region('Level 1', player, multiworld)
    region_map[2] = Region('Level 2', player, multiworld)
    region_map[3] = Region('Level 3', player, multiworld)
    region_map[4] = Region('Level 4', player, multiworld)
    region_map[5] = Region('Level 5', player, multiworld)
    region_map[6] = Region('Level 6', player, multiworld)
    region_map[7] = Region('Level 7', player, multiworld)
    region_map[8] = Region('Level 8', player, multiworld)
    region_map[9] = Region('Level 9', player, multiworld)
    
    for locid,(name,desc,regid) in enumerate(location_table, base_number_id):
        region = region_map[regid]
        if region:
            location = LGA3_Location(player, name, locid, region)
            if include_location(location, options):
                region.locations.append(location)
    region_map[9].locations.append(LGA3_Location(player, 'Ganon', None, region_map[9]));
    for i,reg in region_map:
        world.regions.append(reg)
    