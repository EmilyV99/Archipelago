from typing import List

from ..data.bundle_data import BundleItem
from .crop_logic import CropLogic
from ..logic.has_logic import HasLogic
from ..logic.money_logic import MoneyLogic
from ..logic.region_logic import RegionLogic
from ..stardew_rule import StardewRule
from ..strings.region_names import Region


class BundleLogic:
    player: int
    crop: CropLogic
    has: HasLogic
    money: MoneyLogic
    region: RegionLogic

    def __init__(self, player: int, crop: CropLogic, has: HasLogic, region: RegionLogic, money: MoneyLogic):
        self.player = player
        self.crop = crop
        self.has = has
        self.region = region
        self.money = money

    def can_complete_bundle(self, bundle_requirements: List[BundleItem], number_required: int) -> StardewRule:
        item_rules = []
        highest_quality_yet = 0
        can_speak_junimo = self.region.can_reach(Region.wizard_tower)
        for bundle_item in bundle_requirements:
            if bundle_item.item.item_id == -1:
                return can_speak_junimo & self.money.can_spend(bundle_item.amount)
            else:
                item_rules.append(bundle_item.item.name)
                if bundle_item.quality > highest_quality_yet:
                    highest_quality_yet = bundle_item.quality
        return can_speak_junimo & self.has(item_rules, number_required) & self.crop.can_grow_gold_quality(highest_quality_yet)

    def can_complete_community_center(self) -> StardewRule:
        return (self.region.can_reach_location("Complete Crafts Room") &
                self.region.can_reach_location("Complete Pantry") &
                self.region.can_reach_location("Complete Fish Tank") &
                self.region.can_reach_location("Complete Bulletin Board") &
                self.region.can_reach_location("Complete Vault") &
                self.region.can_reach_location("Complete Boiler Room"))