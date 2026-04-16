from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Region
from Options import OptionError
from rule_builder.rules import Has
from .options import GoalCondition

if TYPE_CHECKING:
    from . import MSMWorld


def create_and_connect_regions(world: MSMWorld) -> None:
    main_menu = Region("Main Menu", world.player, world.multiworld)
    # Basketball
    basketball = Region("Basketball", world.player, world.multiworld)
    b_exhibition_e = Region("Basketball: Exhibition (Easy)", world.player, world.multiworld)
    b_exhibition_n = Region("Basketball: Exhibition (Normal)", world.player, world.multiworld)
    b_exhibition_h = Region("Basketball: Exhibition (Hard)", world.player, world.multiworld)
    b_exhibition_ex = Region("Basketball: Exhibition (Expert)", world.player, world.multiworld)
    b_extra = Region("Basketball: Extra", world.player, world.multiworld)
    # Dodgeball
    dodgeball = Region("Dodgeball", world.player, world.multiworld)
    d_exhibition_e = Region("Dodgeball: Exhibition (Easy)", world.player, world.multiworld)
    d_exhibition_n = Region("Dodgeball: Exhibition (Normal)", world.player, world.multiworld)
    d_exhibition_h = Region("Dodgeball: Exhibition (Hard)", world.player, world.multiworld)
    d_exhibition_ex = Region("Dodgeball: Exhibition (Expert)", world.player, world.multiworld)
    d_extra = Region("Dodgeball: Extra", world.player, world.multiworld)
    # Volleyball
    volleyball = Region("Volleyball", world.player, world.multiworld)
    v_exhibition_e = Region("Volleyball: Exhibition (Easy)", world.player, world.multiworld)
    v_exhibition_n = Region("Volleyball: Exhibition (Normal)", world.player, world.multiworld)
    v_exhibition_h = Region("Volleyball: Exhibition (Hard)", world.player, world.multiworld)
    v_exhibition_ex = Region("Volleyball: Exhibition (Expert)", world.player, world.multiworld)
    v_extra = Region("Volleyball: Extra", world.player, world.multiworld)
    # Hockey
    hockey = Region("Hockey", world.player, world.multiworld)
    h_exhibition_e = Region("Hockey: Exhibition (Easy)", world.player, world.multiworld)
    h_exhibition_n = Region("Hockey: Exhibition (Normal)", world.player, world.multiworld)
    h_exhibition_h = Region("Hockey: Exhibition (Hard)", world.player, world.multiworld)
    h_exhibition_ex = Region("Hockey: Exhibition (Expert)", world.player, world.multiworld)
    h_extra = Region("Hockey: Extra", world.player, world.multiworld)
    # Sports Mix
    sports_mix = Region("Sports Mix", world.player, world.multiworld)
    sm_mushroom_cup = Region("Sports Mix: Mushroom Cup", world.player, world.multiworld)
    sm_flower_cup = Region("Sports Mix: Flower Cup", world.player, world.multiworld)
    sm_star_cup = Region("Sports Mix: Star Cup", world.player, world.multiworld)
    # Party mode
    party_mode = Region("Party Mode", world.player, world.multiworld)
    regions = [main_menu, basketball, b_exhibition_e, b_exhibition_n, b_exhibition_h, b_exhibition_ex, b_extra,
               dodgeball, d_exhibition_e, d_exhibition_n, d_exhibition_h, d_exhibition_ex, d_extra,
               volleyball, v_exhibition_e, v_exhibition_n, v_exhibition_h, v_exhibition_ex, v_extra,
               hockey, h_exhibition_e, h_exhibition_n, h_exhibition_h, h_exhibition_ex, h_extra,
               sports_mix, sm_mushroom_cup, sm_flower_cup, sm_star_cup,
               party_mode]

    behemoth_boss = Region("Behemoth Boss Battle", world.player, world.multiworld)
    regions.append(behemoth_boss)

    # Regions based on options
    if "Normal" in world.options.exhibition_difficulty:
        # Basketball
        b_mushroom_cup_n = Region("Basketball: Mushroom Cup (Normal)", world.player, world.multiworld)
        b_flower_cup_n = Region("Basketball: Flower Cup (Normal)", world.player, world.multiworld)
        b_star_cup_n = Region("Basketball: Star Cup (Normal)", world.player, world.multiworld)
        basketball.connect(b_mushroom_cup_n, "Basketball -> Mushroom Cup (Normal)")
        basketball.connect(b_flower_cup_n, "Basketball -> Flower Cup (Normal)")
        basketball.connect(b_star_cup_n, "Basketball -> Star Cup (Normal)")
        # Dodgeball
        d_mushroom_cup_n = Region("Dodgeball: Mushroom Cup (Normal)", world.player, world.multiworld)
        d_flower_cup_n = Region("Dodgeball: Flower Cup (Normal)", world.player, world.multiworld)
        d_star_cup_n = Region("Dodgeball: Star Cup (Normal)", world.player, world.multiworld)
        dodgeball.connect(d_mushroom_cup_n, "Dodgeball -> Mushroom Cup (Normal)")
        dodgeball.connect(d_flower_cup_n, "Dodgeball -> Flower Cup (Normal)")
        dodgeball.connect(d_star_cup_n, "Dodgeball -> Star Cup (Normal)")
        # Volleyball
        v_mushroom_cup_n = Region("Volleyball: Mushroom Cup (Normal)", world.player, world.multiworld)
        v_flower_cup_n = Region("Volleyball: Flower Cup (Normal)", world.player, world.multiworld)
        v_star_cup_n = Region("Volleyball: Star Cup (Normal)", world.player, world.multiworld)
        volleyball.connect(v_mushroom_cup_n, "Volleyball -> Mushroom Cup (Normal)")
        volleyball.connect(v_flower_cup_n, "Volleyball -> Flower Cup (Normal)")
        volleyball.connect(v_star_cup_n, "Volleyball -> Star Cup (Normal)")
        # Hockey
        h_mushroom_cup_n = Region("Hockey: Mushroom Cup (Normal)", world.player, world.multiworld)
        h_flower_cup_n = Region("Hockey: Flower Cup (Normal)", world.player, world.multiworld)
        h_star_cup_n = Region("Hockey: Star Cup (Normal)", world.player, world.multiworld)
        hockey.connect(h_mushroom_cup_n, "Hockey -> Mushroom Cup (Normal)")
        hockey.connect(h_flower_cup_n, "Hockey -> Flower Cup (Normal)")
        hockey.connect(h_star_cup_n, "Hockey -> Star Cup (Normal)")
        # Append to regions list
        # Basketball
        regions.append(b_mushroom_cup_n)
        regions.append(b_flower_cup_n)
        regions.append(b_star_cup_n)
        # Dodgeball
        regions.append(d_mushroom_cup_n)
        regions.append(d_flower_cup_n)
        regions.append(d_star_cup_n)
        # Volleyball
        regions.append(v_mushroom_cup_n)
        regions.append(v_flower_cup_n)
        regions.append(v_star_cup_n)
        # Hockey
        regions.append(h_mushroom_cup_n)
        regions.append(h_flower_cup_n)
        regions.append(h_star_cup_n)
        if world.options.goal_condition == GoalCondition.option_defeat_behemoth:
            # Behemoth is accessed by completing all normal star cups, connect all to the Behemoth Boss region
            # Note: Add rule if 3 other star cups have been beaten, gonna have to figure out something
            b_star_cup_n.connect(behemoth_boss, "Basketball Star Cup (Normal) -> Behemoth Boss")
            d_star_cup_n.connect(behemoth_boss, "Dodgeball Star Cup (Normal) -> Behemoth Boss")
            v_star_cup_n.connect(behemoth_boss, "Volleyball Star Cup (Normal) -> Behemoth Boss")
            h_star_cup_n.connect(behemoth_boss, "Hockey Star Cup (Normal) -> Behemoth Boss")

    if "Hard" in world.options.exhibition_difficulty:
        # Basketball
        b_mushroom_cup_h = Region("Basketball: Mushroom Cup (Hard)", world.player, world.multiworld)
        b_flower_cup_h = Region("Basketball: Flower Cup (Hard)", world.player, world.multiworld)
        b_star_cup_h = Region("Basketball: Star Cup (Hard)", world.player, world.multiworld)
        basketball.connect(b_mushroom_cup_h, "Basketball -> Mushroom Cup (Hard)")
        basketball.connect(b_flower_cup_h, "Basketball -> Flower Cup (Hard)")
        basketball.connect(b_star_cup_h, "Basketball -> Star Cup (Hard)")
        # Dodgeball
        d_mushroom_cup_h = Region("Dodgeball: Mushroom Cup (Hard)", world.player, world.multiworld)
        d_flower_cup_h = Region("Dodgeball: Flower Cup (Hard)", world.player, world.multiworld)
        d_star_cup_h = Region("Dodgeball: Star Cup (Hard)", world.player, world.multiworld)
        dodgeball.connect(d_mushroom_cup_h, "Dodgeball -> Mushroom Cup (Hard)")
        dodgeball.connect(d_flower_cup_h, "Dodgeball -> Flower Cup (Hard)")
        dodgeball.connect(d_star_cup_h, "Dodgeball -> Star Cup (Hard)")
        # Volleyball
        v_mushroom_cup_h = Region("Volleyball: Mushroom Cup (Hard)", world.player, world.multiworld)
        v_flower_cup_h = Region("Volleyball: Flower Cup (Hard)", world.player, world.multiworld)
        v_star_cup_h = Region("Volleyball: Star Cup (Hard)", world.player, world.multiworld)
        volleyball.connect(v_mushroom_cup_h, "Volleyball -> Mushroom Cup (Hard)")
        volleyball.connect(v_flower_cup_h, "Volleyball -> Flower Cup (Hard)")
        volleyball.connect(v_star_cup_h, "Volleyball -> Star Cup (Hard)")
        # Hockey
        h_mushroom_cup_h = Region("Hockey: Mushroom Cup (Hard)", world.player, world.multiworld)
        h_flower_cup_h = Region("Hockey: Flower Cup (Hard)", world.player, world.multiworld)
        h_star_cup_h = Region("Hockey: Star Cup (Hard)", world.player, world.multiworld)
        hockey.connect(h_mushroom_cup_h, "Hockey -> Mushroom Cup (Hard)")
        hockey.connect(h_flower_cup_h, "Hockey -> Flower Cup (Hard)")
        hockey.connect(h_star_cup_h, "Hockey -> Star Cup (Hard)")
        # Append to regions list
        # Basketball
        regions.append(b_mushroom_cup_h)
        regions.append(b_flower_cup_h)
        regions.append(b_star_cup_h)
        # Dodgeball
        regions.append(d_mushroom_cup_h)
        regions.append(d_flower_cup_h)
        regions.append(d_star_cup_h)
        # Volleyball
        regions.append(v_mushroom_cup_h)
        regions.append(v_flower_cup_h)
        regions.append(v_star_cup_h)
        # Hockey
        regions.append(h_mushroom_cup_h)
        regions.append(h_flower_cup_h)
        regions.append(h_star_cup_h)

    if "Feed Petey" in world.options.party_mode:
        feed_petey = Region("Party Mode: Feed Petey", world.player, world.multiworld)
        regions.append(feed_petey)
        party_mode.connect(feed_petey, "Party Mode -> Feed Petey")
    if "Harmony Hustle" in world.options.party_mode:
        harmony_hustle = Region("Party Mode: Harmony Hustle", world.player, world.multiworld)
        regions.append(harmony_hustle)
        party_mode.connect(harmony_hustle, "Party Mode -> Harmony Hustle")
    if "Bob-omb Dodge" in world.options.party_mode:
        bobomb_dodge = Region("Party Mode: Bob-omb Dodge", world.player, world.multiworld)
        regions.append(bobomb_dodge)
        party_mode.connect(bobomb_dodge, "Party Mode -> Bob Omb Dodge")
    if "Smash Skate" in world.options.party_mode:
        smash_skate = Region("Party Mode: Smash Skate", world.player, world.multiworld)
        regions.append(smash_skate)
        party_mode.connect(smash_skate, "Party Mode -> Smash Skate")

    # Boss stuff
    if world.options.goal_condition == GoalCondition.option_defeat_behemoth_king:
        behemoth_king_boss = Region("Behemoth King Boss Battle", world.player, world.multiworld)
        regions.append(behemoth_king_boss)
        sm_star_cup.connect(behemoth_king_boss, "Sports Mix Star Cup -> Behemoth King Boss")

    # Add regions to AP multiworld so it knows it exists
    world.multiworld.regions += regions

    world.create_entrance(main_menu, basketball, Has("Sport: Basketball"), "Main Menu -> Basketball")
    world.create_entrance(main_menu, dodgeball, Has("Sport: Dodgeball"), "Main Menu -> Dodgeball")
    world.create_entrance(main_menu, volleyball, Has("Sport: Volleyball"), "Main Menu -> Volleyball")
    world.create_entrance(main_menu, hockey, Has("Sport: Hockey"), "Main Menu -> Hockey")
    world.create_entrance(main_menu, sports_mix, Has("Sport: Sports Mix"), "Main Menu -> Sports Mix")
    main_menu.connect(party_mode, "Main Menu -> Party Mode")

    # Connect Basketball to everything
    basketball.connect(b_exhibition_e, "Basketball -> Exhibition (Easy)")
    basketball.connect(b_exhibition_n, "Basketball -> Exhibition (Normal)")
    basketball.connect(b_exhibition_h, "Basketball -> Exhibition (Hard)")
    basketball.connect(b_exhibition_ex, "Basketball -> Exhibition (Expert)")
    basketball.connect(b_extra, "Basketball -> Extra")

    # Connect Dodgeball to everything
    dodgeball.connect(d_exhibition_e, "Dodgeball -> Exhibition (Easy)")
    dodgeball.connect(d_exhibition_n, "Dodgeball -> Exhibition (Normal)")
    dodgeball.connect(d_exhibition_h, "Dodgeball -> Exhibition (Hard)")
    dodgeball.connect(d_exhibition_ex, "Dodgeball -> Exhibition (Expert)")
    dodgeball.connect(d_extra, "Dodgeball -> Extra")

    # Connect Volleyball to everything
    volleyball.connect(v_exhibition_e, "Volleyball -> Exhibition (Easy)")
    volleyball.connect(v_exhibition_n, "Volleyball -> Exhibition (Normal)")
    volleyball.connect(v_exhibition_h, "Volleyball -> Exhibition (Hard)")
    volleyball.connect(v_exhibition_ex, "Volleyball -> Exhibition (Expert)")
    volleyball.connect(v_extra, "Volleyball -> Extra")

    # Connect Hockey to everything
    hockey.connect(h_exhibition_e, "Hockey -> Exhibition (Easy)")
    hockey.connect(h_exhibition_n, "Hockey -> Exhibition (Normal)")
    hockey.connect(h_exhibition_h, "Hockey -> Exhibition (Hard)")
    hockey.connect(h_exhibition_ex, "Hockey -> Exhibition (Expert)")
    hockey.connect(h_extra, "Hockey -> Extra")

    # Connect Sports Mix to everything
    world.create_entrance(sports_mix, sm_mushroom_cup, Has("Sports Mix: Mushroom Cup"), "Sports Mix -> Mushroom Cup")
    world.create_entrance(sports_mix, sm_flower_cup, Has("Sports Mix: Flower Cup"), "Sports Mix -> Flower Cup")
    world.create_entrance(sports_mix, sm_star_cup, Has("Sports Mix: Star Cup"), "Sports Mix -> Star Cup")

