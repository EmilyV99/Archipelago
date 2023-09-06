from typing import Iterable, Union, List


class RecipeSource:

    def __repr__(self):
        return f"RecipeSource"


class StarterSource(RecipeSource):

    def __repr__(self):
        return f"StarterSource"


class ArchipelagoSource(RecipeSource):
    ap_item: List[str]

    def __init__(self, ap_item: Union[str, List[str]]):
        if isinstance(ap_item, str):
            ap_item = [ap_item]
        self.ap_item = ap_item

    def __repr__(self):
        return f"ArchipelagoSource {ap_item}"


class LogicSource(RecipeSource):
    logic_rule: str

    def __init__(self, logic_rule: str):
        self.logic_rule = logic_rule

    def __repr__(self):
        return f"LogicSource {logic_rule}"


class QueenOfSauceSource(RecipeSource):
    year: int
    season: str
    day: int

    def __init__(self, year: int, season: str, day: int):
        self.year = year
        self.season = season
        self.day = day

    def __repr__(self):
        return f"QueenOfSauceSource at year {self.year} {self.season} {self.day}"


class FriendshipSource(RecipeSource):
    friend: str
    hearts: int

    def __init__(self, friend: str, hearts: int):
        self.friend = friend
        self.hearts = hearts

    def __repr__(self):
        return f"FriendshipSource at {self.friend} {self.hearts} <3"


class CutsceneSource(FriendshipSource):
    region: str

    def __init__(self, region: str, friend: str, hearts: int):
        super().__init__(friend, hearts)
        self.region = region

    def __repr__(self):
        return f"CutsceneSource at {region}"


class SkillSource(RecipeSource):
    skill: str
    level: int

    def __init__(self, skill: str, level: int):
        self.skill = skill
        self.level = level

    def __repr__(self):
        return f"SkillSource at level {self.level} {self.skill}"


class ShopSource(RecipeSource):
    region: str
    price: int

    def __init__(self, region: str, price: int):
        self.region = region
        self.price = price

    def __repr__(self):
        return f"ShopSource at {self.region} costing {self.price}g"


class ShopTradeSource(ShopSource):
    currency: str

    def __init__(self, region: str, currency: str, price: int):
        super().__init__(region, price)
        self.currency = currency

    def __repr__(self):
        return f"ShopTradeSource at {self.region} costing {self.price} {self.currency}"
