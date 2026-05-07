from __future__ import annotations

from dataclasses import dataclass
from math import floor
from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from rule_builder.rules import Has, True_, Rule
from .common import *
from .locations import BKSim_Location
import typing
from typing import TYPE_CHECKING, override

if TYPE_CHECKING:
    from .world import BKSimWorld


@dataclass()
class OutOfLogic(Rule["BKSimWorld"], game=game_name):
    description: str = "Out Of Logic"

    @override
    def _instantiate(self, world: BKSimWorld) -> Rule.Resolved:
        return self.Resolved(
            description=self.description if self.description else f"Has {world.glitches_item_name} enabled",
            glitches_item_name=world.glitches_item_name,
            player=world.player,
            caching_enabled=getattr(world, "rule_caching_enabled", False),
        )

    class Resolved(Rule.Resolved):
        description: str
        glitches_item_name: str
        skip_cache = True

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            return {self.glitches_item_name: {id(self)}}

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            return state.has(self.glitches_item_name, self.player)

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            messages: list[JSONMessagePart] = [
                {"type": "color", "color": "magenta", "text": self.description}
            ]
            return messages

        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            return self.description

        @override
        def __str__(self) -> str:
            return f"OutOfLogic({self.description})"


def set_rules(world: BKSimWorld) -> None:
    options = world.options

    world.create_entrance(world.get_region(RID.HOME), world.get_region(RID.SUNNY))
    world.create_entrance(world.get_region(RID.HOME), world.get_region(RID.RAINY))
    world.create_entrance(world.get_region(RID.HOME), world.get_region(RID.SNOWY))

    locs_list: typing.Iterable[BKSim_Location] = typing.cast(typing.Iterable[BKSim_Location], world.get_locations())
    loc_count = options.locs_per_weather.value
    max_rule = True_()
    for loc in locs_list:
        if loc.info is None:
            continue
        if loc.info.region_id == RID.SUNNY:
            if loc.info.index == 0:
                continue
            req_count: int = floor(loc.info.index / 2)
            tmp_rule = Has(ITEM.SHOES, req_count)
            if loc.info.index == loc_count - 1:  # Append the strictest requirement to a 'max rule'
                max_rule &= tmp_rule
            if req_count > 0:
                glitch_rule = OutOfLogic("Slight Logic Break")
                if req_count > 2:
                    glitch_rule &= Has(ITEM.SHOES, req_count - 2)
                tmp_rule |= glitch_rule
            world.set_rule(loc, tmp_rule)
        elif loc.info.region_id == RID.RAINY:
            req_count: int = loc.info.index
            req_count_2: int = floor(loc.info.index / 2) + 1
            no_newloc = Has(ITEM.SHOES, req_count)
            newloc = (Has(ITEM.NEWLOC) & Has(ITEM.SHOES, req_count_2))
            tmp_rule = no_newloc
            if req_count_2 < req_count:
                tmp_rule |= newloc
            if loc.info.index == loc_count - 1:  # Append the strictest requirement to a 'max rule'
                max_rule &= tmp_rule
            if req_count > 0:
                glitch_rule = OutOfLogic("Slight Logic Break")
                if req_count > 2:
                    glitch_no_newloc = Has(ITEM.SHOES, req_count - 2)
                    glitch_newloc = Has(ITEM.NEWLOC)
                    if req_count_2 > 2:
                        glitch_newloc &= Has(ITEM.SHOES, req_count_2 - 2)
                    if max(0, req_count_2) < max(0, req_count):
                        glitch_rule &= (glitch_no_newloc | glitch_newloc)
                    else:
                        glitch_rule &= glitch_no_newloc
                tmp_rule = tmp_rule | glitch_rule
            world.set_rule(loc, tmp_rule)
        elif loc.info.region_id == RID.SNOWY:
            req_count: int = floor(loc.info.index / 2) + 1
            tmp_rule = Has(ITEM.BOOTS, req_count)
            if loc.info.index == loc_count - 1:  # Append the strictest requirement to a 'max rule'
                max_rule &= tmp_rule
            if req_count > 0:
                glitch_rule = OutOfLogic("Slight Logic Break")
                if req_count > 2:
                    glitch_rule &= Has(ITEM.BOOTS, req_count - 2)
                tmp_rule |= glitch_rule
            world.set_rule(loc, tmp_rule)

    world.set_completion_rule(max_rule)  # Require all the strictest requirements, as goal requires completing all locations.
