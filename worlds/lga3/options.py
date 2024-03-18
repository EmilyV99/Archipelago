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

class DeathLinkEnabled(Toggle):
    """Share deaths with other players?"""
    display_name = "Death Link"
class DeathLinkAmnesty(Range):
    """With Death Link enabled, die this many times without sending a DeathLink"""
    display_name = "Death Link Amnesty"
    range_start = 0
    range_end = 10
    default = 0

class EasierGrinding(DefaultOnToggle):
    """Improve drop rates and drop tables"""
    display_name = "Easier Grinding"

@dataclass
class LGA3_Options(PerGameCommonOptions):
    sword_sanity: SwordSanity
    key_sanity: KeySanity
    dungeon_item_sanity: DungeonItemSanity
    magic_rock_for_kill_all: MagicRock
    death_link: DeathLinkEnabled
    death_link_amnesty: DeathLinkAmnesty
    easier_grinding: EasierGrinding

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
