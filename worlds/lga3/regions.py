import typing
from BaseClasses import MultiWorld, Region, Entrance, Location
from .locations import location_table, LGA3_Location
from .common import *
from .options import LGA3_Options

region_map: typing.Dict[RID, Region] = {}
def create_regions(multiworld: MultiWorld, player: int, options: LGA3_Options):
    region_map[RID.MENU] = Region('Menu', player, multiworld);
    region_map[RID.GRASSLAND] = Region('Grassland', player, multiworld)
    region_map[RID.KAKARIKO] = Region('Kakariko', player, multiworld)
    region_map[RID.MOUNTAIN] = Region('Mountain', player, multiworld)
    region_map[RID.DESERT] = Region('Desert', player, multiworld)
    region_map[RID.GRAVEYARD] = Region('Graveyard', player, multiworld)
    region_map[RID.ICE] = Region('Ice', player, multiworld)
    region_map[RID.LEVEL_1] = Region('Level 1', player, multiworld)
    region_map[RID.LEVEL_1_R] = Region('Level 1 Right', player, multiworld)
    region_map[RID.LEVEL_1_B] = Region('Level 1 Boss', player, multiworld)
    region_map[RID.LEVEL_2] = Region('Level 2', player, multiworld)
    region_map[RID.LEVEL_2_B] = Region('Level 2 Boss', player, multiworld)
    region_map[RID.LEVEL_3] = Region('Level 3', player, multiworld)
    region_map[RID.LEVEL_3_F] = Region('Level 3 Front', player, multiworld)
    region_map[RID.LEVEL_3_R] = Region('Level 3 Right', player, multiworld)
    region_map[RID.LEVEL_3_R2] = Region('Level 3 Right 2', player, multiworld)
    region_map[RID.LEVEL_3_B] = Region('Level 3 Boss', player, multiworld)
    region_map[RID.LEVEL_4_F] = Region('Level 4 Front', player, multiworld)
    region_map[RID.LEVEL_4] = Region('Level 4', player, multiworld)
    region_map[RID.LEVEL_5] = Region('Level 5', player, multiworld)
    region_map[RID.LEVEL_6] = Region('Level 6', player, multiworld)
    region_map[RID.LEVEL_7] = Region('Level 7', player, multiworld)
    region_map[RID.LEVEL_8] = Region('Level 8', player, multiworld)
    region_map[RID.LEVEL_9] = Region('Level 9', player, multiworld)
    
    for locid,locinfo in enumerate(location_table, base_number_id):
        region = region_map[locinfo.region_id]
        if region:
            region.locations.append(LGA3_Location(player, locinfo.name, locid, region))
    region_map[RID.LEVEL_9].locations.append(LGA3_Location(player, 'Ganon', None, region_map[RID.LEVEL_9]));
    for i,reg in region_map.items():
        multiworld.regions.append(reg)
    