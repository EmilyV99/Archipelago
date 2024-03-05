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


@dataclass
class LGA3_Options(PerGameCommonOptions):
    sword_sanity: SwordSanity

options_presets = {
    "Basic Rando": {
        "progression_balancing":    0,
        "sword_sanity":             2,
    },
    "Easy Start": {
        "progression_balancing":    0,
        "sword_sanity":             1,
    }
}
