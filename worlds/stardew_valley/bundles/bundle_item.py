from dataclasses import dataclass

from ..options import StardewValleyOptions, ExcludeGingerIsland, FestivalLocations
from ..strings.crop_names import Fruit
from ..strings.currency_names import Currency
from ..strings.quality_names import CropQuality, FishQuality, ForageQuality


@dataclass(frozen=True, order=True)
class BundleItem:
    item_name: str
    amount: int = 1
    quality: str = CropQuality.basic

    @staticmethod
    def money_bundle(amount: int):
        return BundleItem(Currency.money, amount)

    def create(self, item_name: str, amount: int, quality: str):
        return BundleItem(item_name, amount, quality)

    def as_amount(self, amount: int):
        return self.create(self.item_name, amount, self.quality)

    def as_quality(self, quality: str):
        return self.create(self.item_name, self.amount, quality)

    def as_quality_crop(self):
        amount = 5
        difficult_crops = [Fruit.sweet_gem_berry, Fruit.ancient_fruit]
        if self.item_name in difficult_crops:
            amount = 1
        return self.as_quality(CropQuality.gold).as_amount(amount)

    def as_quality_fish(self):
        return self.as_quality(FishQuality.gold)

    def as_quality_forage(self):
        return self.as_quality(ForageQuality.gold)

    def __repr__(self):
        quality = "" if self.quality == CropQuality.basic else self.quality
        return f"{self.amount} {quality} {self.item_name}"

    def can_appear(self, options: StardewValleyOptions) -> bool:
        return True


class IslandBundleItem(BundleItem):

    def create(self, item_name: str, amount: int, quality: str):
        return IslandBundleItem(item_name, amount, quality)

    def can_appear(self, options: StardewValleyOptions) -> bool:
        return options.exclude_ginger_island == ExcludeGingerIsland.option_false


class FestivalBundleItem(BundleItem):

    def create(self, item_name: str, amount: int, quality: str):
        return FestivalBundleItem(item_name, amount, quality)

    def can_appear(self, options: StardewValleyOptions) -> bool:
        return options.festival_locations != FestivalLocations.option_disabled
