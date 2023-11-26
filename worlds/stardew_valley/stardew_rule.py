from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from functools import cached_property
from itertools import chain
from typing import Iterable, Dict, List, Union, Sized, Hashable, Callable, Tuple, Set, Optional

from frozendict import frozendict

from BaseClasses import CollectionState, ItemClassification
from .items import item_table

MISSING_ITEM = "THIS ITEM IS MISSING"


@dataclass
class StardewRuleExplanation:
    rule: StardewRule
    state: CollectionState
    expected: bool
    sub_rules: Iterable[StardewRule] = field(default_factory=set)

    def summary(self, depth=0):
        return "  " * depth + f"{str(self.rule)} -> {self.result}"

    def __str__(self, depth=0):
        if not self.sub_rules:
            return self.summary(depth)

        return self.summary(depth) + "\n" + "\n".join(StardewRuleExplanation.__str__(i, depth + 1)
                                                      if i.result is not self.expected else i.summary(depth + 1)
                                                      for i in sorted(self.explained_sub_rules, key=lambda x: x.result))

    def __repr__(self, depth=0):
        if not self.sub_rules:
            return self.summary(depth)

        return self.summary(depth) + "\n" + "\n".join(StardewRuleExplanation.__repr__(i, depth + 1)
                                                      for i in sorted(self.explained_sub_rules, key=lambda x: x.result))

    @cached_property
    def result(self):
        return self.rule(self.state)

    @cached_property
    def explained_sub_rules(self):
        return [i.explain(self.state) for i in self.sub_rules]


class StardewRule(ABC):

    @abstractmethod
    def __call__(self, state: CollectionState) -> bool:
        raise NotImplementedError

    def evaluate_while_simplifying(self, state: CollectionState) -> Tuple[StardewRule, bool]:
        return self.simplify(), self(state)

    def __or__(self, other) -> StardewRule:
        if other is true_ or other is false_ or type(other) is Or:
            return other | self

        return Or(self, other)

    def __and__(self, other) -> StardewRule:
        if other is true_ or other is false_ or type(other) is And:
            return other & self

        return And(self, other)

    @abstractmethod
    def get_difficulty(self):
        raise NotImplementedError

    def simplify(self) -> StardewRule:
        return self

    def explain(self, state: CollectionState, expected=True) -> StardewRuleExplanation:
        return StardewRuleExplanation(self, state, expected)


class LiteralStardewRule(StardewRule, ABC):
    value: bool

    def __call__(self, state: CollectionState) -> bool:
        return self.value

    def __repr__(self):
        return str(self.value)


class True_(LiteralStardewRule):  # noqa
    value = True

    def __new__(cls, _cache=[]):  # noqa
        # Only one single instance will be ever created.
        if not _cache:
            _cache.append(super(True_, cls).__new__(cls))
        return _cache[0]

    def __or__(self, other) -> StardewRule:
        return self

    def __and__(self, other) -> StardewRule:
        return other

    def get_difficulty(self):
        return 0


class False_(LiteralStardewRule):  # noqa
    value = False

    def __new__(cls, _cache=[]):  # noqa
        # Only one single instance will be ever created.
        if not _cache:
            _cache.append(super(False_, cls).__new__(cls))
        return _cache[0]

    def __or__(self, other) -> StardewRule:
        return other

    def __and__(self, other) -> StardewRule:
        return self

    def get_difficulty(self):
        return 999999999


false_ = False_()
true_ = True_()
assert false_ is False_()
assert true_ is True_()


class CombinableStardewRule(StardewRule, ABC):

    @property
    @abstractmethod
    def combination_key(self) -> Hashable:
        raise NotImplementedError

    @property
    @abstractmethod
    def value(self):
        raise NotImplementedError

    def is_same_rule(self, other: CombinableStardewRule):
        return self.combination_key == other.combination_key

    @staticmethod
    def split_rules(rules: Union[Iterable[StardewRule]],
                    reducer: Callable[[CombinableStardewRule, CombinableStardewRule], CombinableStardewRule]) \
            -> Tuple[Tuple[StardewRule, ...], frozendict[Hashable, CombinableStardewRule]]:
        other_rules = []
        reduced_rules = {}
        for rule in rules:
            if isinstance(rule, CombinableStardewRule):
                key = rule.combination_key
                if key not in reduced_rules:
                    reduced_rules[key] = rule
                    continue

                reduced_rules[key] = reducer(reduced_rules[key], rule)
            else:
                other_rules.append(rule)

        return tuple(other_rules), frozendict(reduced_rules)

    @staticmethod
    def merge(left: frozendict[Hashable, CombinableStardewRule],
              right: frozendict[Hashable, CombinableStardewRule],
              reducer: Callable[[CombinableStardewRule, CombinableStardewRule], CombinableStardewRule]) \
            -> frozendict[Hashable, CombinableStardewRule]:
        reduced_rules = dict(left)
        for key, rule in right.items():
            if key not in reduced_rules:
                reduced_rules[key] = rule
                continue

            reduced_rules[key] = reducer(reduced_rules[key], rule)

        return frozendict(reduced_rules)

    def add_into(self, rules: frozendict[Hashable, CombinableStardewRule],
                 reducer: Callable[[CombinableStardewRule, CombinableStardewRule], CombinableStardewRule]) \
            -> frozendict[Hashable, CombinableStardewRule]:
        if self.combination_key not in rules:
            return rules | {self.combination_key: self}

        other = rules[self.combination_key]
        return rules | {self.combination_key: reducer(self, other)}

    def __and__(self, other):
        if isinstance(other, CombinableStardewRule) and self.is_same_rule(other):
            return And.combine(self, other)
        return super().__and__(other)

    def __or__(self, other):
        if isinstance(other, CombinableStardewRule) and self.is_same_rule(other):
            return Or.combine(self, other)
        return super().__or__(other)


class AggregatingStardewRule(StardewRule, ABC):
    identity: LiteralStardewRule
    complement: LiteralStardewRule
    symbol: str

    combinable_rules: frozendict[Hashable, CombinableStardewRule]
    other_rules: Union[Iterable[StardewRule], Sized]

    detailed_unique_rules: Union[Iterable[StardewRule], Sized]

    _simplified: bool
    _simplified_rules: Set[StardewRule]
    _left_to_simplify_rules: Optional[Iterable[StardewRule]]

    def __init__(self, *rules: StardewRule, _combinable_rules=None):
        self._simplified = False
        self._simplified_rules = set()

        if _combinable_rules is None:
            assert rules, f"Can't create an aggregating condition without rules"
            rules, _combinable_rules = CombinableStardewRule.split_rules(rules, self.combine)

        self.other_rules = tuple(rules)
        self.combinable_rules = _combinable_rules

        self.detailed_unique_rules = self.other_rules
        self._left_to_simplify_rules = None

    @property
    def rules_iterable(self):
        return chain(self.other_rules, self.combinable_rules.values())

    @property
    def detailed_rules_iterable(self):
        return chain(self.detailed_unique_rules, self.combinable_rules.values())

    @staticmethod
    @abstractmethod
    def combine(left: CombinableStardewRule, right: CombinableStardewRule) -> CombinableStardewRule:
        raise NotImplementedError

    def evaluate_while_simplifying(self, state: CollectionState) -> Tuple[StardewRule, bool]:
        # TODO test if inverting would speed up
        for rule in chain(self.combinable_rules.values()):
            if rule(state) is self.complement.value:
                return self, self.complement.value

        if not self.other_rules:
            return self, self.identity.value

        if self._simplified:
            for rule in self.other_rules:
                if rule(state) is self.complement.value:
                    return self, self.complement.value
            return self, self.identity.value
        elif self._simplified_rules:
            for rule in self._simplified_rules:
                if rule(state) is self.complement.value:
                    return self, self.complement.value

        # for rule in self._left_to_simplify_rules:
        #     simplified = rule.simplify()
        #
        #     if simplified is self.identity or simplified in self._simplified_rules:
        #         continue
        #     self._simplified_rules.add(simplified)
        #
        #     if simplified(state) is self.complement.value:
        #         return self.complement.value
        #
        # self._simplified = True
        # return self.identity.value

        if self._left_to_simplify_rules is None:
            self.other_rules = frozenset(self.other_rules)
            if self.complement in self.other_rules:
                self._simplified = True
                self.other_rules = (self.complement,)
                return self.complement, self.complement.value

            self._left_to_simplify_rules = iter(self.other_rules)

        for rule in self._left_to_simplify_rules:
            simplified, value = rule.evaluate_while_simplifying(state)

            if simplified is self.identity or simplified in self._simplified_rules:
                continue

            if simplified is self.complement:
                self._simplified = True
                self.other_rules = (self.complement,)
                return self.complement, self.complement.value

            self._simplified_rules.add(simplified)

            if value is self.complement.value:
                return self, self.complement.value

        self._simplified = True
        self.other_rules = frozenset(self._simplified_rules)

        return self, self.identity.value

    def __str__(self):
        return f"({self.symbol.join(str(rule) for rule in self.detailed_rules_iterable)})"

    def __repr__(self):
        return f"({self.symbol.join(repr(rule) for rule in self.detailed_rules_iterable)})"

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.combinable_rules == other.combinable_rules and self.other_rules == self.other_rules

    def __hash__(self):
        return hash((self.combinable_rules, self.other_rules))

    def simplify(self) -> StardewRule:
        # TODO is this needed now that we're using an iterator ?
        if self._simplified:
            return self

        if self._left_to_simplify_rules is None:
            self.other_rules = frozenset(self.other_rules)
            if self.complement in self.other_rules:
                self._simplified = True
                self.other_rules = (self.complement,)
                return self.complement

            self._left_to_simplify_rules = iter(self.other_rules)

        for rule in self._left_to_simplify_rules:
            simplified = rule.simplify()

            if simplified is self.identity or simplified in self._simplified_rules:
                continue

            if simplified is self.complement:
                self._simplified = True
                self._simplified_rules = {self.complement}
                return self.complement

            self._simplified_rules.add(simplified)

        self._simplified = True
        self.other_rules = frozenset(self._simplified_rules)

        if not self.other_rules and not self.combinable_rules:
            return self.identity

        if len(self.other_rules) == 1 and not self.combinable_rules:
            return next(iter(self.other_rules))

        if not self.other_rules and len(self.combinable_rules) == 1:
            return next(iter(self.combinable_rules.values()))

        return self

    def explain(self, state: CollectionState, expected=True) -> StardewRuleExplanation:
        return StardewRuleExplanation(self, state, expected, frozenset(self.detailed_unique_rules).union(self.combinable_rules.values()))


class Or(AggregatingStardewRule):
    identity = false_
    complement = true_
    symbol = " | "

    def __call__(self, state: CollectionState) -> bool:
        return self.evaluate_while_simplifying(state)[1]

    def __or__(self, other):
        if other is true_ or other is false_:
            return other | self

        if isinstance(other, CombinableStardewRule):
            return Or(*self.other_rules, _combinable_rules=other.add_into(self.combinable_rules, self.combine))

        if type(other) is Or:
            return Or(*self.other_rules, *other.other_rules,
                      _combinable_rules=CombinableStardewRule.merge(self.combinable_rules, other.combinable_rules, self.combine))

        return Or(*self.other_rules, other, _combinable_rules=self.combinable_rules)

    @staticmethod
    def combine(left: CombinableStardewRule, right: CombinableStardewRule) -> CombinableStardewRule:
        return min(left, right, key=lambda x: x.value)

    def get_difficulty(self):
        return min(rule.get_difficulty() for rule in self.rules_iterable)


class And(AggregatingStardewRule):
    identity = true_
    complement = false_
    symbol = " & "

    def __call__(self, state: CollectionState) -> bool:
        return self.evaluate_while_simplifying(state)[1]

    def __and__(self, other):
        if other is true_ or other is false_:
            return other & self

        if isinstance(other, CombinableStardewRule):
            return And(*self.other_rules, _combinable_rules=other.add_into(self.combinable_rules, self.combine))

        if type(other) is And:
            return And(*self.other_rules, *other.other_rules,
                       _combinable_rules=CombinableStardewRule.merge(self.combinable_rules, other.combinable_rules, self.combine))

        return And(*self.other_rules, other, _combinable_rules=self.combinable_rules)

    @staticmethod
    def combine(left: CombinableStardewRule, right: CombinableStardewRule) -> CombinableStardewRule:
        return max(left, right, key=lambda x: x.value)

    def get_difficulty(self):
        return max(rule.get_difficulty() for rule in self.rules_iterable)


class Count(StardewRule):
    count: int
    rules: List[StardewRule]
    _simplified: bool

    def __init__(self, count: int, rule: Union[StardewRule, Iterable[StardewRule]], *rules: StardewRule):
        rules_list: List[StardewRule]

        if isinstance(rule, Iterable):
            rules_list = [*rule]
        else:
            rules_list = [rule]

        if rules is not None:
            rules_list.extend(rules)

        assert rules_list, "Can't create a Count conditions without rules"
        assert len(rules_list) >= count, "Count need at least as many rules at the count"

        self.rules = rules_list
        self.count = count
        self._simplified = False

    def __call__(self, state: CollectionState) -> bool:
        self.simplify()
        c = 0
        for r in self.rules:
            if r(state):
                c += 1
            if c >= self.count:
                return True
        return False

    # TODO implement evaluate while simplifying

    def simplify(self):
        if self._simplified:
            return self

        simplified_rules = [rule.simplify() for rule in self.rules]
        self.rules = simplified_rules
        self._simplified = True
        return self

    def explain(self, state: CollectionState, expected=True) -> StardewRuleExplanation:
        return StardewRuleExplanation(self, state, expected, self.rules)

    def get_difficulty(self):
        rules_sorted_by_difficulty = sorted(self.rules, key=lambda x: x.get_difficulty())
        easiest_n_rules = rules_sorted_by_difficulty[0:self.count]
        return max(rule.get_difficulty() for rule in easiest_n_rules)

    def __repr__(self):
        return f"Received {self.count} {repr(self.rules)}"


class TotalReceived(StardewRule):
    count: int
    items: Iterable[str]
    player: int

    def __init__(self, count: int, items: Union[str, Iterable[str]], player: int):
        items_list: List[str]

        if isinstance(items, Iterable):
            items_list = [*items]
        else:
            items_list = [items]

        assert items_list, "Can't create a Total Received conditions without items"
        for item in items_list:
            assert item_table[item].classification & ItemClassification.progression, \
                f"Item [{item_table[item].name}] has to be progression to be used in logic"

        self.player = player
        self.items = items_list
        self.count = count

    def __call__(self, state: CollectionState) -> bool:
        c = 0
        for item in self.items:
            c += state.count(item, self.player)
            if c >= self.count:
                return True
        return False

    def explain(self, state: CollectionState, expected=True) -> StardewRuleExplanation:
        return StardewRuleExplanation(self, state, expected, [Received(i, self.player, 1) for i in self.items])

    def get_difficulty(self):
        return self.count

    def __repr__(self):
        return f"Received {self.count} {self.items}"


@dataclass(frozen=True)
class Received(CombinableStardewRule):
    item: str
    player: int
    count: int

    def __post_init__(self):
        assert item_table[self.item].classification & ItemClassification.progression, \
            f"Item [{item_table[self.item].name}] has to be progression to be used in logic"

    @property
    def combination_key(self) -> Hashable:
        return self.item

    @property
    def value(self):
        return self.count

    def __call__(self, state: CollectionState) -> bool:
        return state.has(self.item, self.player, self.count)

    def __repr__(self):
        if self.count == 1:
            return f"Received {self.item}"
        return f"Received {self.count} {self.item}"

    def get_difficulty(self):
        return self.count


@dataclass(frozen=True)
class Reach(StardewRule):
    spot: str
    resolution_hint: str
    player: int

    def __call__(self, state: CollectionState) -> bool:
        return state.can_reach(self.spot, self.resolution_hint, self.player)

    def __repr__(self):
        return f"Reach {self.resolution_hint} {self.spot}"

    def get_difficulty(self):
        return 1

    def explain(self, state: CollectionState, expected=True) -> StardewRuleExplanation:
        # FIXME this should be in core
        if self.resolution_hint == 'Location':
            spot = state.multiworld.get_location(self.spot, self.player)
            # TODO explain virtual reach for room
            access_rule = spot.access_rule
        elif self.resolution_hint == 'Entrance':
            spot = state.multiworld.get_entrance(self.spot, self.player)
            access_rule = spot.access_rule
        else:
            spot = state.multiworld.get_region(self.spot, self.player)
            access_rule = Or(*(Reach(e.name, "Entrance", self.player) for e in spot.entrances))

        if not isinstance(access_rule, StardewRule):
            return StardewRuleExplanation(self, state, expected)

        return StardewRuleExplanation(self, state, expected, [access_rule])


class Has(StardewRule):
    item: str
    # For sure there is a better way than just passing all the rules everytime
    other_rules: Dict[str, StardewRule]

    def __init__(self, item: str, other_rules: Dict[str, StardewRule]):
        self.item = item
        self.other_rules = other_rules

    def __call__(self, state: CollectionState) -> bool:
        # TODO eval & simplify
        self.simplify()
        return self.other_rules[self.item](state)

    def evaluate_while_simplifying(self, state: CollectionState) -> Tuple[StardewRule, bool]:
        return self.other_rules[self.item].evaluate_while_simplifying(state)

    def simplify(self) -> StardewRule:
        return self.other_rules[self.item].simplify()

    def explain(self, state: CollectionState, expected=True) -> StardewRuleExplanation:
        return StardewRuleExplanation(self, state, expected, [self.other_rules[self.item]])

    def get_difficulty(self):
        return self.other_rules[self.item].get_difficulty() + 1

    def __str__(self):
        if self.item not in self.other_rules:
            return f"Has {self.item} -> {MISSING_ITEM}"
        return f"Has {self.item}"

    def __repr__(self):
        if self.item not in self.other_rules:
            return f"Has {self.item} -> {MISSING_ITEM}"
        return f"Has {self.item} -> {repr(self.other_rules[self.item])}"

    def __hash__(self):
        return hash(self.item)


@dataclass(frozen=True)
class HasProgressionPercent(CombinableStardewRule):
    player: int
    percent: int

    def __post_init__(self):
        assert self.percent > 0, "HasProgressionPercent rule must be above 0%"
        assert self.percent <= 100, "HasProgressionPercent rule can't require more than 100% of items"

    @property
    def combination_key(self) -> Hashable:
        return HasProgressionPercent.__name__

    @property
    def value(self):
        return self.percent

    def __call__(self, state: CollectionState) -> bool:
        stardew_world = state.multiworld.worlds[self.player]
        total_count = stardew_world.total_progression_items
        needed_count = (total_count * self.percent) // 100
        total_count = 0
        for item in state.prog_items[self.player]:
            item_count = state.prog_items[self.player][item]
            total_count += item_count
            if total_count >= needed_count:
                return True
        return False

    def __repr__(self):
        return f"HasProgressionPercent {self.percent}"

    def get_difficulty(self):
        return self.percent
