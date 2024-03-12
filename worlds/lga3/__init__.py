import settings
from typing import Any
from BaseClasses import Region, Location, Item, ItemClassification, Tutorial, MultiWorld
from worlds.AutoWorld import World, WebWorld
from .options import LGA3_Options, options_presets
from .locations import *
from .items import *
from .regions import *
from .rules import *
from .common import *

class LGA3_Web(WebWorld):
    options_presets = options_presets
    setup_en = Tutorial(
        "LGA3 Setup",
        "How to set up Link's Grand Adventure 3: Remastered for Archipelago",
        "English",
        "setup_en.md",
        "setup/en",
        ["Emily"]
    )
    tutorials = [setup_en]


class LGA3_World(World):
    """
    Link's Grand Adventure 3 is a Zelda-Like game in the ZQuest Classic game engine
    """
    
    game = gamename
    topology_present = False
    web = LGA3_Web()
    options_dataclass = LGA3_Options
    options: LGA3_Options
    location_descriptions = {loc.name: loc.desc for loc in location_table}
    item_descriptions = {itm.name: itm.desc for itm in item_table}
    location_name_to_id = location_name_to_id
    item_name_to_id = item_name_to_id
    #item_name_groups = item_name_groups
    
    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
    
    def create_regions(self) -> None:
        create_regions(self)

    def create_items(self) -> None:
        create_items(self)
    
    def create_item(self, name: str) -> LGA3_Item:
        return create_item(name, self.player)
    
    def set_rules(self) -> None:
        set_rules(self)
        
    def generate_output(self, output_directory: str) -> None:
        from Utils import visualize_regions
        visualize_regions(self.get_region(RID.MENU), f"output/lga3_world.puml")
    
    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            'base_id': base_number_id,
            'num_items': len(item_table),
            'num_locs': len(location_table)
            };
    def get_region(self, region_name: str) -> Region:
        return self.multiworld.get_region(region_name, self.player)

