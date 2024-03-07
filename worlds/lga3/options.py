from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, Range, Choice, PerGameCommonOptions
from .common import *

class SwordSanity(Choice):
    """Randomize swords?"""
    display_name = "SwordSanity"
    option_vanilla = 0
    option_vanilla_start = 1
    option_rando_all = 2
    default = 2

class MagicRock(DefaultOnToggle):
    """Require the 'Magic Rock' logically for kill-all-enemies rooms?"""
    display_name = "Magic Rock for Kill All"

class KeySanity(Choice):
    """Randomize keys?"""
    display_name = "KeySanity"
    option_vanilla = 0
    option_only_big = 1
    option_all = 2
    default = 0
class DungeonItemSanity(Choice):
    """Randomize level-based items?"""
    display_name = "DungeonItemSanity"
    option_vanilla = 0
    option_map = 1
    option_compass = 2
    option_both = 3
    default = 3

@dataclass
class LGA3_Options(PerGameCommonOptions):
    sword_sanity: SwordSanity
    key_sanity: KeySanity
    dungeon_item_sanity: DungeonItemSanity
    magic_rock_for_kill_all: MagicRock

options_presets = {
    "Basic Rando": {
        "progression_balancing":        0,
        "sword_sanity":                 2,
        "key_sanity":                   0,
        "dungeon_item_sanity":          3,
        "magic_rock_for_kill_all":   True,
    },
    "Easy Start": {
        "progression_balancing":        0,
        "sword_sanity":                 1,
        "key_sanity":                   0,
        "dungeon_item_sanity":          0,
        "magic_rock_for_kill_all":   True,
    },
    "Max Rando": {
        "progression_balancing":        0,
        "sword_sanity":                 2,
        "key_sanity":                   0,
        "dungeon_item_sanity":          3,
        "magic_rock_for_kill_all":  False,
    },
}
