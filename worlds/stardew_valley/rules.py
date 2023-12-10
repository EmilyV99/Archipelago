import itertools
from typing import List

from BaseClasses import MultiWorld
from worlds.generic import Rules as MultiWorldRules
from . import locations
from .bundles.bundle_room import BundleRoom
from .data.craftable_data import all_crafting_recipes_by_name
from .data.monster_data import all_monsters_by_category, all_monsters_by_name
from .data.museum_data import all_museum_items, dwarf_scrolls, skeleton_front, skeleton_middle, skeleton_back, all_museum_items_by_name, all_museum_minerals, \
    all_museum_artifacts, Artifact
from .data.recipe_data import all_cooking_recipes_by_name
from .locations import LocationTags
from .logic.logic import StardewLogic
from .logic.tool_logic import tool_upgrade_prices
from .mods.mod_data import ModNames
from .options import StardewValleyOptions, Friendsanity
from .options import ToolProgression, BuildingProgression, ExcludeGingerIsland, SpecialOrderLocations, Museumsanity, BackpackProgression, Shipsanity, \
    Monstersanity, Chefsanity, Craftsanity, ArcadeMachineLocations, Cooksanity, Cropsanity, SkillProgression
from .stardew_rule import And
from .strings.ap_names.event_names import Event
from .strings.ap_names.mods.mod_items import SVEQuestItem
from .strings.ap_names.transport_names import Transportation
from .strings.ap_names.mods.mod_items import SVELocation
from .strings.artisan_good_names import ArtisanGood
from .strings.building_names import Building
from .strings.bundle_names import CCRoom
from .strings.calendar_names import Weekday
from .strings.craftable_names import Bomb
from .strings.crop_names import Fruit
from .strings.entrance_names import dig_to_mines_floor, dig_to_skull_floor, Entrance, move_to_woods_depth, DeepWoodsEntrance, AlecEntrance, MagicEntrance, \
    SVEEntrance
from .strings.generic_names import Generic
from .strings.material_names import Material
from .strings.metal_names import MetalBar
from .strings.quest_names import Quest, ModQuest
from .strings.region_names import Region, SVERegion
from .strings.season_names import Season
from .strings.skill_names import ModSkill, Skill
from .strings.tool_names import Tool, ToolMaterial
from .strings.tv_channel_names import Channel
from .strings.villager_names import NPC, ModNPC
from .strings.wallet_item_names import Wallet


def set_rules(world):
    multiworld = world.multiworld
    world_options = world.options
    player = world.player
    logic = world.logic
    bundle_rooms: List[BundleRoom] = world.modified_bundles

    all_location_names = list(location.name for location in multiworld.get_locations(player))

    set_entrance_rules(logic, multiworld, player, world_options)
    set_ginger_island_rules(logic, multiworld, player, world_options)

    set_tool_rules(logic, multiworld, player, world_options)
    set_skills_rules(logic, multiworld, player, world_options)
    set_bundle_rules(bundle_rooms, logic, multiworld, player)
    set_building_rules(logic, multiworld, player, world_options)
    set_cropsanity_rules(all_location_names, logic, multiworld, player, world_options)
    set_story_quests_rules(all_location_names, logic, multiworld, player, world_options)
    set_special_order_rules(all_location_names, logic, multiworld, player, world_options)
    set_help_wanted_quests_rules(logic, multiworld, player, world_options)
    set_fishsanity_rules(all_location_names, logic, multiworld, player)
    set_museumsanity_rules(all_location_names, logic, multiworld, player, world_options)

    set_friendsanity_rules(all_location_names, logic, multiworld, player, world_options)
    set_backpack_rules(logic, multiworld, player, world_options)
    set_festival_rules(all_location_names, logic, multiworld, player)
    set_monstersanity_rules(all_location_names, logic, multiworld, player, world_options)
    set_shipsanity_rules(all_location_names, logic, multiworld, player, world_options)
    set_cooksanity_rules(all_location_names, logic, multiworld, player, world_options)
    set_chefsanity_rules(all_location_names, logic, multiworld, player, world_options)
    set_craftsanity_rules(all_location_names, logic, multiworld, player, world_options)
    set_isolated_locations_rules(logic, multiworld, player)
    set_traveling_merchant_day_rules(logic, multiworld, player)
    set_arcade_machine_rules(logic, multiworld, player, world_options)

    set_deepwoods_rules(logic, multiworld, player, world_options)
    set_magic_spell_rules(logic, multiworld, player, world_options)
    set_sve_rules(logic, multiworld, player, world_options)


def set_isolated_locations_rules(logic: StardewLogic, multiworld, player):
    MultiWorldRules.add_rule(multiworld.get_location("Old Master Cannoli", player),
                             logic.has(Fruit.sweet_gem_berry))
    MultiWorldRules.add_rule(multiworld.get_location("Galaxy Sword Shrine", player),
                             logic.has("Prismatic Shard"))
    MultiWorldRules.add_rule(multiworld.get_location("Krobus Stardrop", player),
                             logic.money.can_spend(20000))
    MultiWorldRules.add_rule(multiworld.get_location("Demetrius's Breakthrough", player),
                             logic.money.can_have_earned_total(25000))


def set_tool_rules(logic: StardewLogic, multiworld, player, world_options: StardewValleyOptions):
    if not world_options.tool_progression & ToolProgression.option_progressive:
        return

    MultiWorldRules.add_rule(multiworld.get_location("Purchase Fiberglass Rod", player),
                             (logic.skill.has_level(Skill.fishing, 2) & logic.money.can_spend(1800)))
    MultiWorldRules.add_rule(multiworld.get_location("Purchase Iridium Rod", player),
                             (logic.skill.has_level(Skill.fishing, 6) & logic.money.can_spend(7500)))

    materials = [None, "Copper", "Iron", "Gold", "Iridium"]
    tool = [Tool.hoe, Tool.pickaxe, Tool.axe, Tool.watering_can, Tool.watering_can, Tool.trash_can]
    for (previous, material), tool in itertools.product(zip(materials[:4], materials[1:]), tool):
        if previous is None:
            continue
        tool_upgrade_location = multiworld.get_location(f"{material} {tool} Upgrade", player)
        MultiWorldRules.set_rule(tool_upgrade_location, logic.tool.has_tool(tool, previous))


def set_building_rules(logic: StardewLogic, multiworld, player, world_options: StardewValleyOptions):
    if not world_options.building_progression & BuildingProgression.option_progressive:
        return

    for building in locations.locations_by_tag[LocationTags.BUILDING_BLUEPRINT]:
        if building.mod_name is not None and building.mod_name not in world_options.mods:
            continue
        MultiWorldRules.set_rule(multiworld.get_location(building.name, player),
                                 logic.registry.building_rules[building.name.replace(" Blueprint", "")])


def set_bundle_rules(bundle_rooms: List[BundleRoom], logic: StardewLogic, multiworld, player):
    for bundle_room in bundle_rooms:
        room_rules = []
        for bundle in bundle_room.bundles:
            location = multiworld.get_location(bundle.name, player)
            bundle_rules = logic.bundle.can_complete_bundle(bundle)
            room_rules.append(bundle_rules)
            MultiWorldRules.set_rule(location, bundle_rules)
        if bundle_room.name == CCRoom.abandoned_joja_mart:
            continue
        room_location = f"Complete {bundle_room.name}"
        MultiWorldRules.add_rule(multiworld.get_location(room_location, player), And(*room_rules))


def set_skills_rules(logic: StardewLogic, multiworld, player, world_options: StardewValleyOptions):
    mods = world_options.mods
    if world_options.skill_progression == SkillProgression.option_vanilla:
        return
    for i in range(1, 11):
        set_vanilla_skill_rule_for_level(logic, multiworld, player, i)
        set_modded_skill_rule_for_level(logic, multiworld, player, mods, i)


def set_vanilla_skill_rule_for_level(logic: StardewLogic, multiworld, player, level: int):
    set_vanilla_skill_rule(logic, multiworld, player, Skill.farming, level)
    set_vanilla_skill_rule(logic, multiworld, player, Skill.fishing, level)
    set_vanilla_skill_rule(logic, multiworld, player, Skill.foraging, level)
    set_vanilla_skill_rule(logic, multiworld, player, Skill.mining, level)
    set_vanilla_skill_rule(logic, multiworld, player, Skill.combat, level)


def set_modded_skill_rule_for_level(logic: StardewLogic, multiworld, player, mods, level: int):
    if ModNames.luck_skill in mods:
        set_modded_skill_rule(logic, multiworld, player, ModSkill.luck, level)
    if ModNames.magic in mods:
        set_modded_skill_rule(logic, multiworld, player, ModSkill.magic, level)
    if ModNames.binning_skill in mods:
        set_modded_skill_rule(logic, multiworld, player, ModSkill.binning, level)
    if ModNames.cooking_skill in mods:
        set_modded_skill_rule(logic, multiworld, player, ModSkill.cooking, level)
    if ModNames.socializing_skill in mods:
        set_modded_skill_rule(logic, multiworld, player, ModSkill.socializing, level)
    if ModNames.archaeology in mods:
        set_modded_skill_rule(logic, multiworld, player, ModSkill.archaeology, level)


def get_skill_level_location(multiworld, player, skill: str, level: int):
    location_name = f"Level {level} {skill}"
    return multiworld.get_location(location_name, player)


def set_vanilla_skill_rule(logic: StardewLogic, multiworld, player, skill: str, level: int):
    rule = logic.skill.can_earn_level(skill, level)
    MultiWorldRules.set_rule(get_skill_level_location(multiworld, player, skill, level), rule)


def set_modded_skill_rule(logic: StardewLogic, multiworld, player, skill: str, level: int):
    rule = logic.mod.skill.can_earn_mod_skill_level(skill, level)
    MultiWorldRules.set_rule(get_skill_level_location(multiworld, player, skill, level), rule)


def set_entrance_rules(logic: StardewLogic, multiworld, player, world_options: StardewValleyOptions):
    set_mines_floor_entrance_rules(logic, multiworld, player)
    set_skull_cavern_floor_entrance_rules(logic, multiworld, player)
    set_blacksmith_entrance_rules(logic, multiworld, player)
    set_skill_entrance_rules(logic, multiworld, player)
    set_traveling_merchant_day_rules(logic, multiworld, player)

    dangerous_mine_rule = logic.mine.has_mine_elevator_to_floor(120) & logic.region.can_reach(Region.qi_walnut_room)
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.dig_to_dangerous_mines_20, player),
                             dangerous_mine_rule)
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.dig_to_dangerous_mines_60, player),
                             dangerous_mine_rule)
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.dig_to_dangerous_mines_100, player),
                             dangerous_mine_rule)

    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_tide_pools, player),
                             logic.received("Beach Bridge") | (logic.mod.magic.can_blink()))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_quarry, player),
                             logic.received("Bridge Repair") | (logic.mod.magic.can_blink()))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_secret_woods, player),
                             logic.tool.has_tool(Tool.axe, "Iron") | (logic.mod.magic.can_blink()))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.forest_to_sewer, player),
                             logic.wallet.has_rusty_key())
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.town_to_sewer, player),
                             logic.wallet.has_rusty_key())
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_abandoned_jojamart, player),
                             logic.has_abandoned_jojamart())
    movie_theater_rule = logic.has_movie_theater()
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_movie_theater, player),
                             movie_theater_rule)
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.purchase_movie_ticket, player),
                             movie_theater_rule)
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.take_bus_to_desert, player),
                             logic.received("Bus Repair"))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_skull_cavern, player),
                             logic.received(Wallet.skull_key))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_dangerous_skull_cavern, player),
                             (logic.received(Wallet.skull_key) & logic.region.can_reach(Region.qi_walnut_room)))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.talk_to_mines_dwarf, player),
                             logic.wallet.can_speak_dwarf() & logic.tool.has_tool(Tool.pickaxe, ToolMaterial.iron))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.buy_from_traveling_merchant, player),
                             logic.traveling_merchant.has_days())

    set_farm_buildings_entrance_rules(logic, multiworld, player)

    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.mountain_to_railroad, player),
                             logic.received("Railroad Boulder Removed"))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_witch_warp_cave, player),
                             logic.quest.has_dark_talisman() | (logic.mod.magic.can_blink()))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_witch_hut, player),
                             (logic.has(ArtisanGood.void_mayonnaise) | logic.mod.magic.can_blink()))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_mutant_bug_lair, player),
                             (logic.received(Event.start_dark_talisman_quest) & logic.relationship.can_meet(NPC.krobus)) | logic.mod.magic.can_blink())
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_casino, player),
                             logic.quest.has_club_card())

    set_bedroom_entrance_rules(logic, multiworld, player, world_options)
    set_festival_entrance_rules(logic, multiworld, player)
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.island_cooking, player), logic.cooking.can_cook_in_kitchen)
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.farmhouse_cooking, player), logic.cooking.can_cook_in_kitchen)
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.shipping, player), logic.shipping.can_use_shipping_bin)
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.watch_queen_of_sauce, player), logic.action.can_watch(Channel.queen_of_sauce))


def set_farm_buildings_entrance_rules(logic, multiworld, player):
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.use_desert_obelisk, player), logic.can_use_obelisk(Transportation.desert_obelisk))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.use_island_obelisk, player), logic.can_use_obelisk(Transportation.island_obelisk))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.use_farm_obelisk, player), logic.can_use_obelisk(Transportation.farm_obelisk))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_greenhouse, player), logic.received("Greenhouse"))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_coop, player), logic.building.has_building(Building.coop))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_barn, player), logic.building.has_building(Building.barn))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_shed, player), logic.building.has_building(Building.shed))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_slime_hutch, player), logic.building.has_building(Building.slime_hutch))


def set_bedroom_entrance_rules(logic, multiworld, player, world_options: StardewValleyOptions):
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_harvey_room, player), logic.relationship.has_hearts(NPC.harvey, 2))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.mountain_to_maru_room, player), logic.relationship.has_hearts(NPC.maru, 2))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_sebastian_room, player),
                             (logic.relationship.has_hearts(NPC.sebastian, 2) | logic.mod.magic.can_blink()))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.forest_to_leah_cottage, player), logic.relationship.has_hearts(NPC.leah, 2))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_elliott_house, player), logic.relationship.has_hearts(NPC.elliott, 2))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_sunroom, player), logic.relationship.has_hearts(NPC.caroline, 2))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.enter_wizard_basement, player), logic.relationship.has_hearts(NPC.wizard, 4))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.mountain_to_leo_treehouse, player), logic.received("Treehouse"))
    if ModNames.alec in world_options.mods:
        MultiWorldRules.set_rule(multiworld.get_entrance(AlecEntrance.petshop_to_bedroom, player),
                                 (logic.relationship.has_hearts(ModNPC.alec, 2) | logic.mod.magic.can_blink()))


def set_mines_floor_entrance_rules(logic, multiworld, player):
    for floor in range(5, 120 + 5, 5):
        rule = logic.mine.has_mine_elevator_to_floor(floor - 10)
        if floor == 5 or floor == 45 or floor == 85:
            rule = rule & logic.mine.can_progress_in_the_mines_from_floor(floor)
        entrance = multiworld.get_entrance(dig_to_mines_floor(floor), player)
        MultiWorldRules.set_rule(entrance, rule)


def set_skull_cavern_floor_entrance_rules(logic, multiworld, player):
    for floor in range(25, 200 + 25, 25):
        rule = logic.mod.elevator.has_skull_cavern_elevator_to_floor(floor - 25)
        if floor == 25 or floor == 75 or floor == 125:
            rule = rule & logic.mine.can_progress_in_the_skull_cavern_from_floor(floor)
        entrance = multiworld.get_entrance(dig_to_skull_floor(floor), player)
        MultiWorldRules.set_rule(entrance, rule)


def set_blacksmith_entrance_rules(logic, multiworld, player):
    set_blacksmith_upgrade_rule(logic, multiworld, player, Entrance.blacksmith_copper, MetalBar.copper, ToolMaterial.copper)
    set_blacksmith_upgrade_rule(logic, multiworld, player, Entrance.blacksmith_iron, MetalBar.iron, ToolMaterial.iron)
    set_blacksmith_upgrade_rule(logic, multiworld, player, Entrance.blacksmith_gold, MetalBar.gold, ToolMaterial.gold)
    set_blacksmith_upgrade_rule(logic, multiworld, player, Entrance.blacksmith_iridium, MetalBar.iridium, ToolMaterial.iridium)


def set_skill_entrance_rules(logic, multiworld, player):
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.farming, player),
                             logic.skill.can_get_farming_xp)
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.fishing, player),
                             logic.skill.can_get_fishing_xp)


def set_blacksmith_upgrade_rule(logic, multiworld, player, entrance_name: str, item_name: str, tool_material: str):
    material_entrance = multiworld.get_entrance(entrance_name, player)
    upgrade_rule = logic.has(item_name) & logic.money.can_spend(tool_upgrade_prices[tool_material])
    MultiWorldRules.set_rule(material_entrance, upgrade_rule)


def set_festival_entrance_rules(logic, multiworld, player):
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.attend_egg_festival, player), logic.season.has(Season.spring))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.attend_flower_dance, player), logic.season.has(Season.spring))

    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.attend_luau, player), logic.season.has(Season.summer))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.attend_moonlight_jellies, player), logic.season.has(Season.summer))

    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.attend_fair, player), logic.season.has(Season.fall))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.attend_spirit_eve, player), logic.season.has(Season.fall))

    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.attend_festival_of_ice, player), logic.season.has(Season.winter))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.attend_night_market, player), logic.season.has(Season.winter))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.attend_winter_star, player), logic.season.has(Season.winter))


def set_ginger_island_rules(logic: StardewLogic, multiworld, player, world_options: StardewValleyOptions):
    set_island_entrances_rules(logic, multiworld, player)
    if world_options.exclude_ginger_island == ExcludeGingerIsland.option_true:
        return

    set_boat_repair_rules(logic, multiworld, player)
    set_island_parrot_rules(logic, multiworld, player)
    MultiWorldRules.add_rule(multiworld.get_location("Open Professor Snail Cave", player),
                             logic.has(Bomb.cherry_bomb))
    MultiWorldRules.add_rule(multiworld.get_location("Complete Island Field Office", player),
                             logic.can_complete_field_office())


def set_boat_repair_rules(logic: StardewLogic, multiworld, player):
    MultiWorldRules.add_rule(multiworld.get_location("Repair Boat Hull", player),
                             logic.has(Material.hardwood))
    MultiWorldRules.add_rule(multiworld.get_location("Repair Boat Anchor", player),
                             logic.has(MetalBar.iridium))
    MultiWorldRules.add_rule(multiworld.get_location("Repair Ticket Machine", player),
                             logic.has(ArtisanGood.battery_pack))


def set_island_entrances_rules(logic: StardewLogic, multiworld, player):
    boat_repaired = logic.received(Transportation.boat_repair)
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.fish_shop_to_boat_tunnel, player),
                             boat_repaired)
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.boat_to_ginger_island, player),
                             boat_repaired)
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.island_south_to_west, player),
                             logic.received("Island West Turtle"))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.island_south_to_north, player),
                             logic.received("Island North Turtle"))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.island_west_to_islandfarmhouse, player),
                             logic.received("Island Farmhouse"))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.island_west_to_gourmand_cave, player),
                             logic.received("Island Farmhouse"))
    dig_site_rule = logic.received("Dig Site Bridge")
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.island_north_to_dig_site, player), dig_site_rule)
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.dig_site_to_professor_snail_cave, player),
                             logic.received("Open Professor Snail Cave"))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.talk_to_island_trader, player),
                             logic.received("Island Trader"))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.island_south_to_southeast, player),
                             logic.received("Island Resort"))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.use_island_resort, player),
                             logic.received("Island Resort"))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.island_west_to_qi_walnut_room, player),
                             logic.received("Qi Walnut Room"))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.island_north_to_volcano, player),
                             (logic.tool.can_water(0) | logic.received("Volcano Bridge") |
                              logic.mod.magic.can_blink()))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.volcano_to_secret_beach, player),
                             logic.tool.can_water(2))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.climb_to_volcano_5, player),
                             (logic.ability.can_mine_perfectly() & logic.tool.can_water(1)))
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.talk_to_volcano_dwarf, player),
                             logic.wallet.can_speak_dwarf())
    MultiWorldRules.set_rule(multiworld.get_entrance(Entrance.climb_to_volcano_10, player),
                             (logic.ability.can_mine_perfectly() & logic.tool.can_water(1)))
    parrots = [Entrance.parrot_express_docks_to_volcano, Entrance.parrot_express_jungle_to_volcano,
               Entrance.parrot_express_dig_site_to_volcano, Entrance.parrot_express_docks_to_dig_site,
               Entrance.parrot_express_jungle_to_dig_site, Entrance.parrot_express_volcano_to_dig_site,
               Entrance.parrot_express_docks_to_jungle, Entrance.parrot_express_dig_site_to_jungle,
               Entrance.parrot_express_volcano_to_jungle, Entrance.parrot_express_jungle_to_docks,
               Entrance.parrot_express_dig_site_to_docks, Entrance.parrot_express_volcano_to_docks]
    parrot_express_rule = logic.received(Transportation.parrot_express)
    parrot_express_to_dig_site_rule = dig_site_rule & parrot_express_rule
    for parrot in parrots:
        if "Dig Site" in parrot:
            MultiWorldRules.set_rule(multiworld.get_entrance(parrot, player), parrot_express_to_dig_site_rule)
        else:
            MultiWorldRules.set_rule(multiworld.get_entrance(parrot, player), parrot_express_rule)


def set_island_parrot_rules(logic: StardewLogic, multiworld, player):
    has_walnut = logic.has_walnut(1)
    has_5_walnut = logic.has_walnut(5)
    has_10_walnut = logic.has_walnut(10)
    has_20_walnut = logic.has_walnut(20)
    MultiWorldRules.add_rule(multiworld.get_location("Leo's Parrot", player),
                             has_walnut)
    MultiWorldRules.add_rule(multiworld.get_location("Island West Turtle", player),
                             has_10_walnut & logic.received("Island North Turtle"))
    MultiWorldRules.add_rule(multiworld.get_location("Island Farmhouse", player),
                             has_20_walnut)
    MultiWorldRules.add_rule(multiworld.get_location("Island Mailbox", player),
                             has_5_walnut & logic.received("Island Farmhouse"))
    MultiWorldRules.add_rule(multiworld.get_location(Transportation.farm_obelisk, player),
                             has_20_walnut & logic.received("Island Mailbox"))
    MultiWorldRules.add_rule(multiworld.get_location("Dig Site Bridge", player),
                             has_10_walnut & logic.received("Island West Turtle"))
    MultiWorldRules.add_rule(multiworld.get_location("Island Trader", player),
                             has_10_walnut & logic.received("Island Farmhouse"))
    MultiWorldRules.add_rule(multiworld.get_location("Volcano Bridge", player),
                             has_5_walnut & logic.received("Island West Turtle") &
                             logic.region.can_reach(Region.volcano_floor_10))
    MultiWorldRules.add_rule(multiworld.get_location("Volcano Exit Shortcut", player),
                             has_5_walnut & logic.received("Island West Turtle"))
    MultiWorldRules.add_rule(multiworld.get_location("Island Resort", player),
                             has_20_walnut & logic.received("Island Farmhouse"))
    MultiWorldRules.add_rule(multiworld.get_location(Transportation.parrot_express, player),
                             has_10_walnut)


def set_cropsanity_rules(all_location_names: List[str], logic: StardewLogic, multiworld, player, world_options: StardewValleyOptions):
    if world_options.cropsanity == Cropsanity.option_disabled:
        return

    harvest_prefix = "Harvest "
    harvest_prefix_length = len(harvest_prefix)
    for harvest_location in locations.locations_by_tag[LocationTags.CROPSANITY]:
        if harvest_location.name in all_location_names and (harvest_location.mod_name is None or harvest_location.mod_name in world_options.mods):
            crop_name = harvest_location.name[harvest_prefix_length:]
            MultiWorldRules.set_rule(multiworld.get_location(harvest_location.name, player),
                                     logic.has(crop_name))


def set_story_quests_rules(all_location_names: List[str], logic: StardewLogic, multiworld, player, world_options: StardewValleyOptions):
    if world_options.quest_locations < 0:
        return
    for quest in locations.locations_by_tag[LocationTags.STORY_QUEST]:
        if quest.name in all_location_names and (quest.mod_name is None or quest.mod_name in world_options.mods):
            MultiWorldRules.set_rule(multiworld.get_location(quest.name, player),
                                     logic.registry.quest_rules[quest.name])


def set_special_order_rules(all_location_names: List[str], logic: StardewLogic, multiworld, player,
                            world_options: StardewValleyOptions):
    if world_options.special_order_locations == SpecialOrderLocations.option_disabled:
        return
    board_rule = logic.received("Special Order Board") & logic.time.has_lived_months(4)
    for board_order in locations.locations_by_tag[LocationTags.SPECIAL_ORDER_BOARD]:
        if board_order.name in all_location_names:
            order_rule = board_rule & logic.registry.special_order_rules[board_order.name]
            MultiWorldRules.set_rule(multiworld.get_location(board_order.name, player), order_rule)

    if world_options.exclude_ginger_island == ExcludeGingerIsland.option_true:
        return
    if world_options.special_order_locations == SpecialOrderLocations.option_board_only:
        return
    qi_rule = logic.region.can_reach(Region.qi_walnut_room) & logic.time.has_lived_months(8)
    for qi_order in locations.locations_by_tag[LocationTags.SPECIAL_ORDER_QI]:
        if qi_order.name in all_location_names:
            order_rule = qi_rule & logic.registry.special_order_rules[qi_order.name]
            MultiWorldRules.set_rule(multiworld.get_location(qi_order.name, player), order_rule)


help_wanted_prefix = "Help Wanted:"
item_delivery = "Item Delivery"
gathering = "Gathering"
fishing = "Fishing"
slay_monsters = "Slay Monsters"


def set_help_wanted_quests_rules(logic: StardewLogic, multiworld, player, world_options: StardewValleyOptions):
    help_wanted_number = world_options.quest_locations.value
    if help_wanted_number < 0:
        return
    for i in range(0, help_wanted_number):
        set_number = i // 7
        month_rule = logic.time.has_lived_months(set_number)
        quest_number = set_number + 1
        quest_number_in_set = i % 7
        if quest_number_in_set < 4:
            quest_number = set_number * 4 + quest_number_in_set + 1
            set_help_wanted_delivery_rule(multiworld, player, month_rule, quest_number)
        elif quest_number_in_set == 4:
            set_help_wanted_fishing_rule(multiworld, player, month_rule, quest_number)
        elif quest_number_in_set == 5:
            set_help_wanted_slay_monsters_rule(multiworld, player, month_rule, quest_number)
        elif quest_number_in_set == 6:
            set_help_wanted_gathering_rule(multiworld, player, month_rule, quest_number)


def set_help_wanted_delivery_rule(multiworld, player, month_rule, quest_number):
    location_name = f"{help_wanted_prefix} {item_delivery} {quest_number}"
    MultiWorldRules.set_rule(multiworld.get_location(location_name, player), month_rule)


def set_help_wanted_gathering_rule(multiworld, player, month_rule, quest_number):
    location_name = f"{help_wanted_prefix} {gathering} {quest_number}"
    MultiWorldRules.set_rule(multiworld.get_location(location_name, player), month_rule)


def set_help_wanted_fishing_rule(multiworld, player, month_rule, quest_number):
    location_name = f"{help_wanted_prefix} {fishing} {quest_number}"
    MultiWorldRules.set_rule(multiworld.get_location(location_name, player), month_rule)


def set_help_wanted_slay_monsters_rule(multiworld, player, month_rule, quest_number):
    location_name = f"{help_wanted_prefix} {slay_monsters} {quest_number}"
    MultiWorldRules.set_rule(multiworld.get_location(location_name, player), month_rule)


def set_fishsanity_rules(all_location_names: List[str], logic: StardewLogic, multiworld: MultiWorld, player: int):
    fish_prefix = "Fishsanity: "
    for fish_location in locations.locations_by_tag[LocationTags.FISHSANITY]:
        if fish_location.name in all_location_names:
            fish_name = fish_location.name[len(fish_prefix):]
            MultiWorldRules.set_rule(multiworld.get_location(fish_location.name, player),
                                     logic.has(fish_name))


def set_museumsanity_rules(all_location_names: List[str], logic: StardewLogic, multiworld: MultiWorld, player: int,
                           world_options: StardewValleyOptions):
    museum_prefix = "Museumsanity: "
    if world_options.museumsanity == Museumsanity.option_milestones:
        for museum_milestone in locations.locations_by_tag[LocationTags.MUSEUM_MILESTONES]:
            set_museum_milestone_rule(logic, multiworld, museum_milestone, museum_prefix, player)
    elif world_options.museumsanity != Museumsanity.option_none:
        set_museum_individual_donations_rules(all_location_names, logic, multiworld, museum_prefix, player)


def set_museum_individual_donations_rules(all_location_names, logic: StardewLogic, multiworld, museum_prefix, player):
    all_donations = sorted(locations.locations_by_tag[LocationTags.MUSEUM_DONATIONS],
                           key=lambda x: all_museum_items_by_name[x.name[len(museum_prefix):]].difficulty, reverse=True)
    counter = 0
    number_donations = len(all_donations)
    for museum_location in all_donations:
        if museum_location.name in all_location_names:
            donation_name = museum_location.name[len(museum_prefix):]
            required_detectors = counter * 5 // number_donations
            rule = logic.museum.can_find_museum_item(all_museum_items_by_name[donation_name]) & logic.received("Traveling Merchant Metal Detector",
                                                                                                               required_detectors)
            MultiWorldRules.set_rule(multiworld.get_location(museum_location.name, player),
                                     rule)
        counter += 1


def set_museum_milestone_rule(logic: StardewLogic, multiworld: MultiWorld, museum_milestone, museum_prefix: str,
                              player: int):
    milestone_name = museum_milestone.name[len(museum_prefix):]
    donations_suffix = " Donations"
    minerals_suffix = " Minerals"
    artifacts_suffix = " Artifacts"
    metal_detector = "Traveling Merchant Metal Detector"
    rule = None
    if milestone_name.endswith(donations_suffix):
        rule = get_museum_item_count_rule(logic, donations_suffix, milestone_name, all_museum_items, logic.museum.can_find_museum_items)
    elif milestone_name.endswith(minerals_suffix):
        rule = get_museum_item_count_rule(logic, minerals_suffix, milestone_name, all_museum_minerals, logic.museum.can_find_museum_minerals)
    elif milestone_name.endswith(artifacts_suffix):
        rule = get_museum_item_count_rule(logic, artifacts_suffix, milestone_name, all_museum_artifacts, logic.museum.can_find_museum_artifacts)
    elif milestone_name == "Dwarf Scrolls":
        rule = And(*(logic.museum.can_find_museum_item(item) for item in dwarf_scrolls)) & logic.received(metal_detector, 4)
    elif milestone_name == "Skeleton Front":
        rule = And(*(logic.museum.can_find_museum_item(item) for item in skeleton_front)) & logic.received(metal_detector, 4)
    elif milestone_name == "Skeleton Middle":
        rule = And(*(logic.museum.can_find_museum_item(item) for item in skeleton_middle)) & logic.received(metal_detector, 4)
    elif milestone_name == "Skeleton Back":
        rule = And(*(logic.museum.can_find_museum_item(item) for item in skeleton_back)) & logic.received(metal_detector, 4)
    elif milestone_name == "Ancient Seed":
        rule = logic.museum.can_find_museum_item(Artifact.ancient_seed) & logic.received(metal_detector, 4)
    if rule is None:
        return
    MultiWorldRules.set_rule(multiworld.get_location(museum_milestone.name, player), rule)


def get_museum_item_count_rule(logic: StardewLogic, suffix, milestone_name, accepted_items, donation_func):
    metal_detector = "Traveling Merchant Metal Detector"
    num = int(milestone_name[:milestone_name.index(suffix)])
    required_detectors = (num - 1) * 5 // len(accepted_items)
    rule = donation_func(num) & logic.received(metal_detector, required_detectors)
    return rule


def set_backpack_rules(logic: StardewLogic, multiworld: MultiWorld, player: int, world_options: StardewValleyOptions):
    if world_options.backpack_progression != BackpackProgression.option_vanilla:
        MultiWorldRules.set_rule(multiworld.get_location("Large Pack", player),
                                 logic.money.can_spend(2000))
        MultiWorldRules.set_rule(multiworld.get_location("Deluxe Pack", player),
                                 (logic.money.can_spend(10000) & logic.received("Progressive Backpack")))
        if ModNames.big_backpack in world_options.mods:
            MultiWorldRules.set_rule(multiworld.get_location("Premium Pack", player),
                                     (logic.money.can_spend(150000) &
                                      logic.received("Progressive Backpack", 2)))


def set_festival_rules(all_location_names: List[str], logic: StardewLogic, multiworld, player):
    festival_locations = []
    festival_locations.extend(locations.locations_by_tag[LocationTags.FESTIVAL])
    festival_locations.extend(locations.locations_by_tag[LocationTags.FESTIVAL_HARD])
    for festival in festival_locations:
        if festival.name in all_location_names:
            MultiWorldRules.set_rule(multiworld.get_location(festival.name, player),
                                     logic.registry.festival_rules[festival.name])


monster_eradication_prefix = "Monster Eradication: "


def set_monstersanity_rules(all_location_names: List[str], logic: StardewLogic, multiworld, player, world_options: StardewValleyOptions):
    monstersanity_option = world_options.monstersanity
    if monstersanity_option == Monstersanity.option_none:
        return

    if monstersanity_option == Monstersanity.option_one_per_monster or monstersanity_option == Monstersanity.option_split_goals:
        set_monstersanity_monster_rules(all_location_names, logic, multiworld, player, monstersanity_option)
        return

    if monstersanity_option == Monstersanity.option_progressive_goals:
        set_monstersanity_progressive_category_rules(all_location_names, logic, multiworld, player)
        return

    set_monstersanity_category_rules(all_location_names, logic, multiworld, player, monstersanity_option)


def set_monstersanity_monster_rules(all_location_names: List[str], logic: StardewLogic, multiworld, player, monstersanity_option):
    for monster_name in all_monsters_by_name:
        location_name = f"{monster_eradication_prefix}{monster_name}"
        if location_name not in all_location_names:
            continue
        location = multiworld.get_location(location_name, player)
        if monstersanity_option == Monstersanity.option_split_goals:
            rule = logic.monster.can_kill_max(all_monsters_by_name[monster_name])
        else:
            rule = logic.monster.can_kill(all_monsters_by_name[monster_name])
        MultiWorldRules.set_rule(location, rule)


def set_monstersanity_progressive_category_rules(all_location_names: List[str], logic: StardewLogic, multiworld, player):
    for monster_category in all_monsters_by_category:
        set_monstersanity_progressive_single_category_rules(all_location_names, logic, multiworld, player, monster_category)


def set_monstersanity_progressive_single_category_rules(all_location_names: List[str], logic: StardewLogic, multiworld, player, monster_category: str):
    location_names = [name for name in all_location_names if name.startswith(monster_eradication_prefix) and name.endswith(monster_category)]
    if not location_names:
        return
    location_names = sorted(location_names, key=lambda name: get_monster_eradication_number(name, monster_category))
    for i in range(5):
        location_name = location_names[i]
        set_monstersanity_progressive_category_rule(all_location_names, logic, multiworld, player, monster_category, location_name, i)


def set_monstersanity_progressive_category_rule(all_location_names: List[str], logic: StardewLogic, multiworld, player,
                                                monster_category: str, location_name: str, goal_index):
    if location_name not in all_location_names:
        return
    location = multiworld.get_location(location_name, player)
    if goal_index < 3:
        rule = logic.monster.can_kill_any(all_monsters_by_category[monster_category], goal_index + 1)
    else:
        rule = logic.monster.can_kill_all(all_monsters_by_category[monster_category], goal_index * 2)
    MultiWorldRules.set_rule(location, rule)


def get_monster_eradication_number(location_name, monster_category) -> int:
    number = location_name[len(monster_eradication_prefix):-len(monster_category)]
    number = number.strip()
    if number.isdigit():
        return int(number)
    return 1000


def set_monstersanity_category_rules(all_location_names: List[str], logic: StardewLogic, multiworld, player, monstersanity_option):
    for monster_category in all_monsters_by_category:
        location_name = f"{monster_eradication_prefix}{monster_category}"
        if location_name not in all_location_names:
            continue
        location = multiworld.get_location(location_name, player)
        if monstersanity_option == Monstersanity.option_one_per_category:
            rule = logic.monster.can_kill_any(all_monsters_by_category[monster_category])
        else:
            rule = logic.monster.can_kill_all(all_monsters_by_category[monster_category], 8)
        MultiWorldRules.set_rule(location, rule)


def set_shipsanity_rules(all_location_names: List[str], logic: StardewLogic, multiworld, player, world_options: StardewValleyOptions):
    shipsanity_option = world_options.shipsanity
    if shipsanity_option == Shipsanity.option_none:
        return

    shipsanity_prefix = "Shipsanity: "
    for location in locations.locations_by_tag[LocationTags.SHIPSANITY]:
        if location.name not in all_location_names:
            continue
        item_to_ship = location.name[len(shipsanity_prefix):]
        MultiWorldRules.set_rule(multiworld.get_location(location.name, player), logic.shipping.can_ship(item_to_ship))


def set_cooksanity_rules(all_location_names: List[str], logic: StardewLogic, multiworld, player, world_options: StardewValleyOptions):
    cooksanity_option = world_options.cooksanity
    if cooksanity_option == Cooksanity.option_none:
        return

    cooksanity_prefix = "Cook "
    for location in locations.locations_by_tag[LocationTags.COOKSANITY]:
        if location.name not in all_location_names:
            continue
        recipe_name = location.name[len(cooksanity_prefix):]
        recipe = all_cooking_recipes_by_name[recipe_name]
        cook_rule = logic.cooking.can_cook(recipe)
        MultiWorldRules.set_rule(multiworld.get_location(location.name, player), cook_rule)


def set_chefsanity_rules(all_location_names: List[str], logic: StardewLogic, multiworld, player, world_options: StardewValleyOptions):
    chefsanity_option = world_options.chefsanity
    if chefsanity_option == Chefsanity.option_none:
        return

    chefsanity_suffix = " Recipe"
    for location in locations.locations_by_tag[LocationTags.CHEFSANITY]:
        if location.name not in all_location_names:
            continue
        recipe_name = location.name[:-len(chefsanity_suffix)]
        recipe = all_cooking_recipes_by_name[recipe_name]
        learn_rule = logic.cooking.can_learn_recipe(recipe.source)
        MultiWorldRules.set_rule(multiworld.get_location(location.name, player), learn_rule)


def set_craftsanity_rules(all_location_names: List[str], logic: StardewLogic, multiworld, player, world_options: StardewValleyOptions):
    craftsanity_option = world_options.craftsanity
    if craftsanity_option == Craftsanity.option_none:
        return

    craft_prefix = "Craft "
    craft_suffix = " Recipe"
    for location in locations.locations_by_tag[LocationTags.CRAFTSANITY]:
        if location.name not in all_location_names:
            continue
        if location.name.endswith(craft_suffix):
            recipe_name = location.name[:-len(craft_suffix)]
            recipe = all_crafting_recipes_by_name[recipe_name]
            craft_rule = logic.crafting.can_learn_recipe(recipe)
        else:
            recipe_name = location.name[len(craft_prefix):]
            recipe = all_crafting_recipes_by_name[recipe_name]
            craft_rule = logic.crafting.can_craft(recipe)
        MultiWorldRules.set_rule(multiworld.get_location(location.name, player), craft_rule)


def set_traveling_merchant_day_rules(logic: StardewLogic, multiworld: MultiWorld, player: int):
    for day in Weekday.all_days:
        item_for_day = f"Traveling Merchant: {day}"
        entrance_name = f"Buy from Traveling Merchant {day}"
        MultiWorldRules.set_rule(multiworld.get_entrance(entrance_name, player), logic.received(item_for_day))


def set_arcade_machine_rules(logic: StardewLogic, multiworld: MultiWorld, player: int, world_options: StardewValleyOptions):
    MultiWorldRules.add_rule(multiworld.get_entrance(Entrance.play_junimo_kart, player),
                             logic.received(Wallet.skull_key))
    if world_options.arcade_machine_locations != ArcadeMachineLocations.option_full_shuffling:
        return

    MultiWorldRules.add_rule(multiworld.get_entrance(Entrance.play_junimo_kart, player),
                             logic.has("Junimo Kart Small Buff"))
    MultiWorldRules.add_rule(multiworld.get_entrance(Entrance.reach_junimo_kart_2, player),
                             logic.has("Junimo Kart Medium Buff"))
    MultiWorldRules.add_rule(multiworld.get_entrance(Entrance.reach_junimo_kart_3, player),
                             logic.has("Junimo Kart Big Buff"))
    MultiWorldRules.add_rule(multiworld.get_location("Junimo Kart: Sunset Speedway (Victory)", player),
                             logic.has("Junimo Kart Max Buff"))
    MultiWorldRules.add_rule(multiworld.get_entrance(Entrance.play_journey_of_the_prairie_king, player),
                             logic.has("JotPK Small Buff"))
    MultiWorldRules.add_rule(multiworld.get_entrance(Entrance.reach_jotpk_world_2, player),
                             logic.has("JotPK Medium Buff"))
    MultiWorldRules.add_rule(multiworld.get_entrance(Entrance.reach_jotpk_world_3, player),
                             logic.has("JotPK Big Buff"))
    MultiWorldRules.add_rule(multiworld.get_location("Journey of the Prairie King Victory", player),
                             logic.has("JotPK Max Buff"))


def set_friendsanity_rules(all_location_names: List[str], logic: StardewLogic, multiworld: MultiWorld, player: int, world_options: StardewValleyOptions):
    if world_options.friendsanity == Friendsanity.option_none:
        return
    MultiWorldRules.add_rule(multiworld.get_location("Spouse Stardrop", player),
                             logic.relationship.has_hearts(Generic.bachelor, 13))
    MultiWorldRules.add_rule(multiworld.get_location("Have a Baby", player),
                             logic.relationship.can_reproduce(1))
    MultiWorldRules.add_rule(multiworld.get_location("Have Another Baby", player),
                             logic.relationship.can_reproduce(2))

    friend_prefix = "Friendsanity: "
    friend_suffix = " <3"
    for friend_location in locations.locations_by_tag[LocationTags.FRIENDSANITY]:
        if not friend_location.name in all_location_names:
            continue
        friend_location_without_prefix = friend_location.name[len(friend_prefix):]
        friend_location_trimmed = friend_location_without_prefix[:friend_location_without_prefix.index(friend_suffix)]
        split_index = friend_location_trimmed.rindex(" ")
        friend_name = friend_location_trimmed[:split_index]
        num_hearts = int(friend_location_trimmed[split_index + 1:])
        MultiWorldRules.set_rule(multiworld.get_location(friend_location.name, player),
                                 logic.relationship.can_earn_relationship(friend_name, num_hearts))


def set_deepwoods_rules(logic: StardewLogic, multiworld: MultiWorld, player: int, world_options: StardewValleyOptions):
    if ModNames.deepwoods in world_options.mods:
        MultiWorldRules.add_rule(multiworld.get_location("Breaking Up Deep Woods Gingerbread House", player),
                                 logic.tool.has_tool(Tool.axe, "Gold"))
        MultiWorldRules.add_rule(multiworld.get_location("Chop Down a Deep Woods Iridium Tree", player),
                                 logic.tool.has_tool(Tool.axe, "Iridium"))
        MultiWorldRules.set_rule(multiworld.get_entrance(DeepWoodsEntrance.use_woods_obelisk, player),
                                 logic.received("Woods Obelisk"))
        for depth in range(10, 100 + 10, 10):
            MultiWorldRules.set_rule(multiworld.get_entrance(move_to_woods_depth(depth), player),
                                     logic.mod.deepwoods.can_chop_to_depth(depth))
        MultiWorldRules.add_rule(multiworld.get_location("The Sword in the Stone", player),
                                 logic.mod.deepwoods.can_pull_sword() & logic.mod.deepwoods.can_chop_to_depth(100))


def set_magic_spell_rules(logic: StardewLogic, multiworld: MultiWorld, player: int, world_options: StardewValleyOptions):
    if ModNames.magic not in world_options.mods:
        return

    MultiWorldRules.set_rule(multiworld.get_entrance(MagicEntrance.store_to_altar, player),
                             (logic.relationship.has_hearts(NPC.wizard, 3) &
                              logic.region.can_reach(Region.wizard_tower)))
    MultiWorldRules.add_rule(multiworld.get_location("Analyze: Clear Debris", player),
                             (logic.tool.has_tool("Axe", "Basic") | logic.tool.has_tool("Pickaxe", "Basic")))
    MultiWorldRules.add_rule(multiworld.get_location("Analyze: Till", player),
                             logic.tool.has_tool("Hoe", "Basic"))
    MultiWorldRules.add_rule(multiworld.get_location("Analyze: Water", player),
                             logic.tool.has_tool("Watering Can", "Basic"))
    MultiWorldRules.add_rule(multiworld.get_location("Analyze All Toil School Locations", player),
                             (logic.tool.has_tool("Watering Can", "Basic") & logic.tool.has_tool("Hoe", "Basic")
                              & (logic.tool.has_tool("Axe", "Basic") | logic.tool.has_tool("Pickaxe", "Basic"))))
    # Do I *want* to add boots into logic when you get them even in vanilla without effort?  idk
    MultiWorldRules.add_rule(multiworld.get_location("Analyze: Evac", player),
                             logic.ability.can_mine_perfectly())
    MultiWorldRules.add_rule(multiworld.get_location("Analyze: Haste", player),
                             logic.has("Coffee"))
    MultiWorldRules.add_rule(multiworld.get_location("Analyze: Heal", player),
                             logic.has("Life Elixir"))
    MultiWorldRules.add_rule(multiworld.get_location("Analyze All Life School Locations", player),
                             (logic.has("Coffee") & logic.has("Life Elixir")
                              & logic.ability.can_mine_perfectly()))
    MultiWorldRules.add_rule(multiworld.get_location("Analyze: Descend", player),
                             logic.region.can_reach(Region.mines))
    MultiWorldRules.add_rule(multiworld.get_location("Analyze: Fireball", player),
                             logic.has("Fire Quartz"))
    MultiWorldRules.add_rule(multiworld.get_location("Analyze: Frostbolt", player),
                             logic.region.can_reach(Region.mines_floor_60) & logic.skill.can_fish(difficulty=85))
    MultiWorldRules.add_rule(multiworld.get_location("Analyze All Elemental School Locations", player),
                             logic.has("Fire Quartz") & logic.region.can_reach(Region.mines_floor_60) & logic.skill.can_fish(difficulty=85))
    # MultiWorldRules.add_rule(multiworld.get_location("Analyze: Lantern", player),)
    MultiWorldRules.add_rule(multiworld.get_location("Analyze: Tendrils", player),
                             logic.region.can_reach(Region.farm))
    MultiWorldRules.add_rule(multiworld.get_location("Analyze: Shockwave", player),
                             logic.has("Earth Crystal"))
    MultiWorldRules.add_rule(multiworld.get_location("Analyze All Nature School Locations", player),
                             (logic.has("Earth Crystal") & logic.region.can_reach("Farm"))),
    MultiWorldRules.add_rule(multiworld.get_location("Analyze: Meteor", player),
                             (logic.region.can_reach(Region.farm) & logic.time.has_lived_months(12))),
    MultiWorldRules.add_rule(multiworld.get_location("Analyze: Lucksteal", player),
                             logic.region.can_reach(Region.witch_hut))
    MultiWorldRules.add_rule(multiworld.get_location("Analyze: Bloodmana", player),
                             logic.region.can_reach(Region.mines_floor_100))
    MultiWorldRules.add_rule(multiworld.get_location("Analyze All Eldritch School Locations", player),
                             (logic.region.can_reach(Region.witch_hut) &
                              logic.region.can_reach(Region.mines_floor_100) &
                              logic.region.can_reach(Region.farm) & logic.time.has_lived_months(12)))
    MultiWorldRules.add_rule(multiworld.get_location("Analyze Every Magic School Location", player),
                             (logic.tool.has_tool("Watering Can", "Basic") & logic.tool.has_tool("Hoe", "Basic")
                              & (logic.tool.has_tool("Axe", "Basic") | logic.tool.has_tool("Pickaxe", "Basic")) &
                              logic.has("Coffee") & logic.has("Life Elixir")
                              & logic.ability.can_mine_perfectly() & logic.has("Earth Crystal") &
                              logic.has("Fire Quartz") & logic.skill.can_fish(difficulty=85) &
                              logic.region.can_reach(Region.witch_hut) &
                              logic.region.can_reach(Region.mines_floor_100) &
                              logic.region.can_reach(Region.farm) & logic.time.has_lived_months(12)))


def set_sve_rules(logic: StardewLogic, multiworld: MultiWorld, player: int, world_options: StardewValleyOptions):
    if ModNames.sve not in world_options.mods:
        return
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.forest_to_lost_woods, player),
                             logic.bundle.can_complete_community_center)
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.enter_summit, player),
                             logic.mod.sve.has_iridium_bomb())
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.backwoods_to_grove, player),
                             logic.mod.sve.has_any_rune())
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.badlands_to_cave, player),
                             logic.has("Aegis Elixir"))
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.forest_west_to_spring, player),
                             logic.quest.can_complete_quest(Quest.magic_ink))
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.secret_woods_to_west, player),
                             logic.tool.has_tool(Tool.axe, ToolMaterial.iron))
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.grandpa_shed_to_interior, player),
                             logic.tool.has_tool(Tool.axe, ToolMaterial.iron))
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.aurora_warp_to_aurora, player),
                             logic.received("Nexus: Aurora Vineyard Runes"))
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.farm_warp_to_farm, player),
                             logic.received("Nexus: Farm and Wizard Runes"))
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.guild_warp_to_guild, player),
                             logic.received("Nexus: Adventurer's Guild Runes"))
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.junimo_warp_to_junimo, player),
                             logic.received("Nexus: Junimo and Outpost Runes"))
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.spring_warp_to_spring, player),
                             logic.received("Nexus: Sprite Spring Runes"))
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.outpost_warp_to_outpost, player),
                             logic.received("Nexus: Junimo and Outpost Runes"))
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.wizard_warp_to_wizard, player),
                             logic.received("Nexus: Farm and Wizard Runes"))
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.use_purple_junimo, player),
                             logic.relationship.has_hearts(ModNPC.apples, 10))
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.grandpa_interior_to_upstairs, player),
                             logic.quest.can_complete_quest(ModQuest.GrandpasShed))
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.use_bear_shop, player),
                             (logic.quest.can_complete_quest(Quest.strange_note) & logic.tool.has_tool(Tool.axe, ToolMaterial.basic) &
                              logic.tool.has_tool(Tool.pickaxe, ToolMaterial.basic)))
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.railroad_to_grampleton_station, player),
                             logic.received(SVEQuestItem.scarlett_job_offer))
    logic.mod.sve.initialize_rules()
    for location in logic.registry.sve_location_rules:
        MultiWorldRules.set_rule(multiworld.get_location(location, player),
                                 logic.registry.sve_location_rules[location])
    set_sve_ginger_island_rules(logic, multiworld, player, world_options)


def set_sve_ginger_island_rules(logic: StardewLogic, multiworld: MultiWorld, player: int, world_options: StardewValleyOptions):
    if world_options.exclude_ginger_island == ExcludeGingerIsland.option_true:
        return
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.summit_to_highlands, player),
                             logic.received("Marlon's Boat Paddle"))
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.wizard_to_fable_reef, player),
                             logic.received("Fable Reef Portal"))
    MultiWorldRules.set_rule(multiworld.get_location(SVELocation.diamond_wand, player),
                             logic.quest.can_complete_quest(ModQuest.MonsterCrops) & logic.region.can_reach(SVERegion.lances_house))
    MultiWorldRules.set_rule(multiworld.get_entrance(SVEEntrance.highlands_to_cave, player),
                             logic.tool.has_tool(Tool.pickaxe, ToolMaterial.iron) & logic.tool.has_tool(Tool.axe, ToolMaterial.iron))
