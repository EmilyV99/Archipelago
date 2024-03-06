from dataclasses import dataclass
from Options import Toggle, Range, Choice, PerGameCommonOptions
from .common import *

class SwordSanity(Choice):
    """Randomize swords?"""
    display_name = "SwordSanity"
    option_vanilla = 0
    option_vanilla_start = 1
    option_rando_all = 2
    default = 2

class KeySanity(Choice):
    """Randomize keys?"""
    display_name = "KeySanity"
    option_vanilla = 0 #!TODO KeySanity
    #option_only_big = 1
    #option_all = 2
    default = 0

@dataclass
class LGA3_Options(PerGameCommonOptions):
    sword_sanity: SwordSanity
    key_sanity: KeySanity

options_presets = {
    "Basic Rando": {
        "progression_balancing":    0,
        "sword_sanity":             2,
        "key_sanity":               0,
    },
    "Easy Start": {
        "progression_balancing":    0,
        "sword_sanity":             1,
        "key_sanity":               0,
    }
}
