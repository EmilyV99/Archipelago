import settings
import typing
from BaseClasses import Region, Location, Item, ItemClassification, Tutorial
from worlds.AutoWorld import World, WebWorld
from .options import LGA3_Options, options_presets
from .locations import location_table, location_name_to_id
from .items import item_table, LGA3_Item, item_name_to_id
from .regions import create_regions
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
    
    game = 'Link\'s Grand Adventure 3: Remastered'
    topology_present = False
    web = LGA3_Web()
    options_dataclass = LGA3_Options
    options: LGA3_Options
    location_descriptions = {name: desc for name,desc,_ in location_table}
    item_descriptions = {name: desc for name,desc,_ in item_table}
    location_name_to_id = location_name_to_id
    item_name_to_id = item_name_to_id

    def create_regions(self) -> None:
        create_regions(self.multiworld, self.player, self.options)

    def create_items(self) -> None:
        create_items(self.multiworld, self.player, self.options)
    
    def set_rules(self) -> None:
        set_rules(self.multiworld, self.player, self.options)

