from typing import Iterable

from Utils import cache_self1
from .base_logic import BaseLogic
from .received_logic import ReceivedLogicMixin
from .time_logic import TimeLogicMixin
from ..options import SeasonRandomization
from ..stardew_rule import StardewRule, True_, And, Or
from ..strings.generic_names import Generic
from ..strings.season_names import Season


class SeasonLogicMixin(BaseLogic):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = SeasonLogic(*args, **kwargs)


class SeasonLogic(TimeLogicMixin, ReceivedLogicMixin):

    @cache_self1
    def has(self, season: str) -> StardewRule:
        if season == Generic.any:
            return True_()
        seasons_order = [Season.spring, Season.summer, Season.fall, Season.winter]
        if self.options.season_randomization == SeasonRandomization.option_progressive:
            return self.received(Season.progressive, seasons_order.index(season))
        if self.options.season_randomization == SeasonRandomization.option_disabled:
            if season == Season.spring:
                return True_()
            return self.time.has_lived_months(1)
        return self.received(season)

    def has_any(self, seasons: Iterable[str]):
        if not seasons:
            return True_()
        return Or(*(self.has(season) for season in seasons))

    def has_any_not_winter(self):
        return self.has_any([Season.spring, Season.summer, Season.fall])

    def has_all(self, seasons: Iterable[str]):
        if not seasons:
            return True_()
        return And(*(self.has(season) for season in seasons))
