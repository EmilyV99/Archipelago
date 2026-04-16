from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.rules import Has, HasAll, CanReachRegion
from .options import StageUnlockType

if TYPE_CHECKING:
    from . import MSMWorld


def set_all_rules(world: MSMWorld) -> None:
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_location_rules(world: MSMWorld) -> None:
    # Get ready for a whole lotta world.get_location

    # ===== Sports Mix =====
    has_mario_stadium = Has("Stage: Mario Stadium")
    has_koopa_troopa_beach = Has("Stage: Koopa Troopa Beach")
    has_peach_castle = Has("Stage: Peach's Castle")
    has_toad_park = Has("Stage: Toad Park")
    has_dk_dock = Has("Stage: DK Dock")
    has_luigi_mansion = Has("Stage: Luigi's Mansion")
    has_daisy_garden = Has("Stage: Daisy Garden")
    has_wario_factory = Has("Stage: Wario Factory")
    has_bowser_jr_blvd = Has("Stage: Bowser Jr. Blvd.")
    has_bowser_castle = Has("Stage: Bowser's Castle")
    has_waluigi_pinball = Has("Stage: Waluigi Pinball")
    has_ghoulish_galleon = Has("Stage: Ghoulish Galleon")
    has_star_ship = Has("Stage: Star Ship")
    has_western_junction = Has("Stage: Western Junction")
    has_boss_stage = Has("Boss Stage")

    if "Easy" in world.options.exhibition_difficulty:
        # Basketball
        b_dk_dock_e = world.get_location("Basketball Ex: Beat DK Dock (Easy)")
        b_luigi_mansion_e = world.get_location("Basketball Ex: Beat Luigi's Mansion (Easy)")
        b_western_junction_e = world.get_location("Basketball Ex: Beat Western Junction (Easy)")
        b_daisy_garden_e = world.get_location("Basketball Ex: Beat Daisy Garden (Easy)")
        b_bowser_jr_blvd_e = world.get_location("Basketball Ex: Beat Bowser Jr. Blvd. (Easy)")
        b_bowsers_castle_e = world.get_location("Basketball Ex: Beat Bowser's Castle (Easy)")
        b_star_ship_e = world.get_location("Basketball Ex: Beat Star Ship (Easy)")
        b_peach_castle_e = world.get_location("Basketball Ex: Beat Peach's Castle (Easy)")
        b_wario_factory_e = world.get_location("Basketball Ex: Beat Wario Factory (Easy)")
        b_ghoulish_galleon_e = world.get_location("Basketball Ex: Beat Ghoulish Galleon (Easy)")
        # Dodgeball
        d_mario_stadium_e = world.get_location("Dodgeball Ex: Beat Mario Stadium (Easy)")
        d_koopa_troopa_beach_e = world.get_location("Dodgeball Ex: Beat Koopa Troopa Beach (Easy)")
        d_dk_dock_e = world.get_location("Dodgeball Ex: Beat DK Dock (Easy)")
        d_western_junction_e = world.get_location("Dodgeball Ex: Beat Western Junction (Easy)")
        d_daisy_garden_e = world.get_location("Dodgeball Ex: Beat Daisy Garden (Easy)")
        d_bowsers_castle_e = world.get_location("Dodgeball Ex: Beat Bowser's Castle (Easy)")
        d_star_ship_e = world.get_location("Dodgeball Ex: Beat Star Ship (Easy)")
        d_peach_castle_e = world.get_location("Dodgeball Ex: Beat Peach's Castle (Easy)")
        d_wario_factory_e = world.get_location("Dodgeball Ex: Beat Wario Factory (Easy)")
        d_ghoulish_galleon_e = world.get_location("Dodgeball Ex: Beat Ghoulish Galleon (Easy)")
        d_toad_park_e = world.get_location("Dodgeball Ex: Beat Toad Park (Easy)")
        d_waluigi_pinball_e = world.get_location("Dodgeball Ex: Beat Waluigi Pinball (Easy)")
        # Volleyball
        v_mario_stadium_e = world.get_location("Volleyball Ex: Beat Mario Stadium (Easy)")
        v_koopa_troopa_beach_e = world.get_location("Volleyball Ex: Beat Koopa Troopa Beach (Easy)")
        v_dk_dock_e = world.get_location("Volleyball Ex: Beat DK Dock (Easy)")
        v_luigi_mansion_e = world.get_location("Volleyball Ex: Beat Luigi's Mansion (Easy)")
        v_western_junction_e = world.get_location("Volleyball Ex: Beat Western Junction (Easy)")
        v_bowser_jr_blvd_e = world.get_location("Volleyball Ex: Beat Bowser Jr. Blvd. (Easy)")
        v_bowsers_castle_e = world.get_location("Volleyball Ex: Beat Bowser's Castle (Easy)")
        v_star_ship_e = world.get_location("Volleyball Ex: Beat Star Ship (Easy)")
        v_peach_castle_e = world.get_location("Volleyball Ex: Beat Peach's Castle (Easy)")
        v_wario_factory_e = world.get_location("Volleyball Ex: Beat Wario Factory (Easy)")
        v_ghoulish_galleon_e = world.get_location("Volleyball Ex: Beat Ghoulish Galleon (Easy)")
        v_waluigi_pinball_e = world.get_location("Volleyball Ex: Beat Waluigi Pinball (Easy)")
        # Hockey
        h_mario_stadium_e = world.get_location("Hockey Ex: Beat Mario Stadium (Easy)")
        h_koopa_troopa_beach_e = world.get_location("Hockey Ex: Beat Koopa Troopa Beach (Easy)")
        h_western_junction_e = world.get_location("Hockey Ex: Beat Western Junction (Easy)")
        h_daisy_garden_e = world.get_location("Hockey Ex: Beat Daisy Garden (Easy)")
        h_bowser_jr_blvd_e = world.get_location("Hockey Ex: Beat Bowser Jr. Blvd. (Easy)")
        h_bowsers_castle_e = world.get_location("Hockey Ex: Beat Bowser's Castle (Easy)")
        h_star_ship_e = world.get_location("Hockey Ex: Beat Star Ship (Easy)")
        h_peach_castle_e = world.get_location("Hockey Ex: Beat Peach's Castle (Easy)")
        h_wario_factory_e = world.get_location("Hockey Ex: Beat Wario Factory (Easy)")

        # Basketball
        world.set_rule(world.get_location("Basketball Ex: Beat Mario Stadium (Easy)"), has_mario_stadium)
        world.set_rule(world.get_location("Basketball Ex: Beat Koopa Troopa Beach (Easy)"), has_koopa_troopa_beach)
        world.set_rule(b_dk_dock_e, has_dk_dock)
        world.set_rule(b_luigi_mansion_e, has_luigi_mansion)
        world.set_rule(b_western_junction_e, has_western_junction)
        world.set_rule(b_daisy_garden_e, has_daisy_garden)
        world.set_rule(b_bowser_jr_blvd_e, has_bowser_jr_blvd)
        world.set_rule(b_bowsers_castle_e, has_bowser_castle)
        world.set_rule(b_star_ship_e, has_star_ship)
        world.set_rule(b_peach_castle_e, has_peach_castle)
        world.set_rule(b_wario_factory_e, has_wario_factory)
        world.set_rule(b_ghoulish_galleon_e, has_ghoulish_galleon)

        # Dodgeball
        world.set_rule(d_mario_stadium_e, has_mario_stadium)
        world.set_rule(d_koopa_troopa_beach_e, has_koopa_troopa_beach)
        world.set_rule(d_dk_dock_e, has_dk_dock)
        world.set_rule(d_western_junction_e, has_western_junction)
        world.set_rule(d_daisy_garden_e, has_daisy_garden)
        world.set_rule(d_bowsers_castle_e, has_bowser_castle)
        world.set_rule(d_star_ship_e, has_star_ship)
        world.set_rule(d_peach_castle_e, has_peach_castle)
        world.set_rule(d_wario_factory_e, has_wario_factory)
        world.set_rule(d_ghoulish_galleon_e, has_ghoulish_galleon)
        world.set_rule(d_toad_park_e, has_toad_park)
        world.set_rule(d_waluigi_pinball_e, has_waluigi_pinball)

        # Volleyball
        world.set_rule(v_mario_stadium_e, has_mario_stadium)
        world.set_rule(v_koopa_troopa_beach_e, has_koopa_troopa_beach)
        world.set_rule(v_dk_dock_e, has_dk_dock)
        world.set_rule(v_luigi_mansion_e, has_luigi_mansion)
        world.set_rule(v_western_junction_e, has_western_junction)
        world.set_rule(v_bowser_jr_blvd_e, has_bowser_jr_blvd)
        world.set_rule(v_bowsers_castle_e, has_bowser_castle)
        world.set_rule(v_star_ship_e, has_star_ship)
        world.set_rule(v_peach_castle_e, has_peach_castle)
        world.set_rule(v_wario_factory_e, has_wario_factory)
        world.set_rule(v_ghoulish_galleon_e, has_ghoulish_galleon)
        world.set_rule(v_waluigi_pinball_e, has_waluigi_pinball)

        # Hockey
        world.set_rule(h_mario_stadium_e, has_mario_stadium)
        world.set_rule(h_koopa_troopa_beach_e, has_koopa_troopa_beach)
        world.set_rule(h_western_junction_e, has_western_junction)
        world.set_rule(h_daisy_garden_e, has_daisy_garden)
        world.set_rule(h_bowser_jr_blvd_e, has_bowser_jr_blvd)
        world.set_rule(h_bowsers_castle_e, has_bowser_castle)
        world.set_rule(h_star_ship_e, has_star_ship)
        world.set_rule(h_peach_castle_e, has_peach_castle)
        world.set_rule(h_wario_factory_e, has_wario_factory)
        world.set_rule(world.get_location("Hockey Ex: Beat Ghoulish Galleon (Easy)"), has_ghoulish_galleon)
        world.set_rule(world.get_location("Hockey Ex: Beat Toad Park (Easy)"), has_toad_park)
        world.set_rule(world.get_location("Hockey Ex: Beat Waluigi Pinball (Easy)"), has_waluigi_pinball)

    if "Normal" in world.options.exhibition_difficulty:
        # Basketball
        b_mario_stadium_n = world.get_location("Basketball Ex: Beat Mario Stadium (Normal)")
        b_koopa_troopa_beach_n = world.get_location("Basketball Ex: Beat Koopa Troopa Beach (Normal)")
        b_dk_dock_n = world.get_location("Basketball Ex: Beat DK Dock (Normal)")
        b_luigi_mansion_n = world.get_location("Basketball Ex: Beat Luigi's Mansion (Normal)")
        b_western_junction_n = world.get_location("Basketball Ex: Beat Western Junction (Normal)")
        b_daisy_garden_n = world.get_location("Basketball Ex: Beat Daisy Garden (Normal)")
        b_bowser_jr_blvd_n = world.get_location("Basketball Ex: Beat Bowser Jr. Blvd. (Normal)")
        b_bowsers_castle_n = world.get_location("Basketball Ex: Beat Bowser's Castle (Normal)")
        b_star_ship_n = world.get_location("Basketball Ex: Beat Star Ship (Normal)")
        b_peach_castle_n = world.get_location("Basketball Ex: Beat Peach's Castle (Normal)")
        b_wario_factory_n = world.get_location("Basketball Ex: Beat Wario Factory (Normal)")
        b_ghoulish_galleon_n = world.get_location("Basketball Ex: Beat Ghoulish Galleon (Normal)")
        # Dodgeball
        d_mario_stadium_n = world.get_location("Dodgeball Ex: Beat Mario Stadium (Normal)")
        d_koopa_troopa_beach_n = world.get_location("Dodgeball Ex: Beat Koopa Troopa Beach (Normal)")
        d_dk_dock_n = world.get_location("Dodgeball Ex: Beat DK Dock (Normal)")
        d_western_junction_n = world.get_location("Dodgeball Ex: Beat Western Junction (Normal)")
        d_daisy_garden_n = world.get_location("Dodgeball Ex: Beat Daisy Garden (Normal)")
        d_bowsers_castle_n = world.get_location("Dodgeball Ex: Beat Bowser's Castle (Normal)")
        d_star_ship_n = world.get_location("Dodgeball Ex: Beat Star Ship (Normal)")
        d_peach_castle_n = world.get_location("Dodgeball Ex: Beat Peach's Castle (Normal)")
        d_wario_factory_n = world.get_location("Dodgeball Ex: Beat Wario Factory (Normal)")
        d_ghoulish_galleon_n = world.get_location("Dodgeball Ex: Beat Ghoulish Galleon (Normal)")
        d_toad_park_n = world.get_location("Dodgeball Ex: Beat Toad Park (Normal)")
        d_waluigi_pinball_n = world.get_location("Dodgeball Ex: Beat Waluigi Pinball (Normal)")
        # Volleyball
        v_mario_stadium_n = world.get_location("Volleyball Ex: Beat Mario Stadium (Normal)")
        v_koopa_troopa_beach_n = world.get_location("Volleyball Ex: Beat Koopa Troopa Beach (Normal)")
        v_dk_dock_n = world.get_location("Volleyball Ex: Beat DK Dock (Normal)")
        v_luigi_mansion_n = world.get_location("Volleyball Ex: Beat Luigi's Mansion (Normal)")
        v_western_junction_n = world.get_location("Volleyball Ex: Beat Western Junction (Normal)")
        v_bowser_jr_blvd_n = world.get_location("Volleyball Ex: Beat Bowser Jr. Blvd. (Normal)")
        v_bowsers_castle_n = world.get_location("Volleyball Ex: Beat Bowser's Castle (Normal)")
        v_star_ship_n = world.get_location("Volleyball Ex: Beat Star Ship (Normal)")
        v_peach_castle_n = world.get_location("Volleyball Ex: Beat Peach's Castle (Normal)")
        v_wario_factory_n = world.get_location("Volleyball Ex: Beat Wario Factory (Normal)")
        v_ghoulish_galleon_n = world.get_location("Volleyball Ex: Beat Ghoulish Galleon (Normal)")
        v_waluigi_pinball_n = world.get_location("Volleyball Ex: Beat Waluigi Pinball (Normal)")
        # Hockey
        h_mario_stadium_n = world.get_location("Hockey Ex: Beat Mario Stadium (Normal)")
        h_koopa_troopa_beach_n = world.get_location("Hockey Ex: Beat Koopa Troopa Beach (Normal)")
        h_western_junction_n = world.get_location("Hockey Ex: Beat Western Junction (Normal)")
        h_daisy_garden_n = world.get_location("Hockey Ex: Beat Daisy Garden (Normal)")
        h_bowser_jr_blvd_n = world.get_location("Hockey Ex: Beat Bowser Jr. Blvd. (Normal)")
        h_bowsers_castle_n = world.get_location("Hockey Ex: Beat Bowser's Castle (Normal)")
        h_star_ship_n = world.get_location("Hockey Ex: Beat Star Ship (Normal)")
        h_peach_castle_n = world.get_location("Hockey Ex: Beat Peach's Castle (Normal)")
        h_wario_factory_n = world.get_location("Hockey Ex: Beat Wario Factory (Normal)")
        h_ghoulish_galleon_n = world.get_location("Hockey Ex: Beat Ghoulish Galleon (Normal)")
        h_toad_park_n = world.get_location("Hockey Ex: Beat Toad Park (Normal)")
        h_waluigi_pinball_n = world.get_location("Hockey Ex: Beat Waluigi Pinball (Normal)")

        # Basketball
        world.set_rule(b_mario_stadium_n, has_mario_stadium)
        world.set_rule(b_koopa_troopa_beach_n, has_koopa_troopa_beach)
        world.set_rule(b_dk_dock_n, has_dk_dock)
        world.set_rule(b_luigi_mansion_n, has_luigi_mansion)
        world.set_rule(b_western_junction_n, has_western_junction)
        world.set_rule(b_daisy_garden_n, has_daisy_garden)
        world.set_rule(b_bowser_jr_blvd_n, has_bowser_jr_blvd)
        world.set_rule(b_bowsers_castle_n, has_bowser_castle)
        world.set_rule(b_star_ship_n, has_star_ship)
        world.set_rule(b_peach_castle_n, has_peach_castle)
        world.set_rule(b_wario_factory_n, has_wario_factory)
        world.set_rule(b_ghoulish_galleon_n, has_ghoulish_galleon)

        # Dodgeball
        world.set_rule(d_mario_stadium_n, has_mario_stadium)
        world.set_rule(d_koopa_troopa_beach_n, has_koopa_troopa_beach)
        world.set_rule(d_dk_dock_n, has_dk_dock)
        world.set_rule(d_western_junction_n, has_western_junction)
        world.set_rule(d_daisy_garden_n, has_daisy_garden)
        world.set_rule(d_bowsers_castle_n, has_bowser_castle)
        world.set_rule(d_star_ship_n, has_star_ship)
        world.set_rule(d_peach_castle_n, has_peach_castle)
        world.set_rule(d_wario_factory_n, has_wario_factory)
        world.set_rule(d_ghoulish_galleon_n, has_ghoulish_galleon)
        world.set_rule(d_toad_park_n, has_toad_park)
        world.set_rule(d_waluigi_pinball_n, has_waluigi_pinball)

        # Volleyball
        world.set_rule(v_mario_stadium_n, has_mario_stadium)
        world.set_rule(v_koopa_troopa_beach_n, has_koopa_troopa_beach)
        world.set_rule(v_dk_dock_n, has_dk_dock)
        world.set_rule(v_luigi_mansion_n, has_luigi_mansion)
        world.set_rule(v_western_junction_n, has_western_junction)
        world.set_rule(v_bowser_jr_blvd_n, has_bowser_jr_blvd)
        world.set_rule(v_bowsers_castle_n, has_bowser_castle)
        world.set_rule(v_star_ship_n, has_star_ship)
        world.set_rule(v_peach_castle_n, has_peach_castle)
        world.set_rule(v_wario_factory_n, has_wario_factory)
        world.set_rule(v_ghoulish_galleon_n, has_ghoulish_galleon)
        world.set_rule(v_waluigi_pinball_n, has_waluigi_pinball)

        # Hockey
        world.set_rule(h_mario_stadium_n, has_mario_stadium)
        world.set_rule(h_koopa_troopa_beach_n, has_koopa_troopa_beach)
        world.set_rule(h_western_junction_n, has_western_junction)
        world.set_rule(h_daisy_garden_n, has_daisy_garden)
        world.set_rule(h_bowser_jr_blvd_n, has_bowser_jr_blvd)
        world.set_rule(h_bowsers_castle_n, has_bowser_castle)
        world.set_rule(h_star_ship_n, has_star_ship)
        world.set_rule(h_peach_castle_n, has_peach_castle)
        world.set_rule(h_wario_factory_n, has_wario_factory)
        world.set_rule(h_ghoulish_galleon_n, has_ghoulish_galleon)
        world.set_rule(h_toad_park_n, has_toad_park)
        world.set_rule(h_waluigi_pinball_n, has_waluigi_pinball)

    if "Hard" in world.options.exhibition_difficulty:
        # Basketball
        b_mario_stadium_h = world.get_location("Basketball Ex: Beat Mario Stadium (Hard)")
        b_koopa_troopa_beach_h = world.get_location("Basketball Ex: Beat Koopa Troopa Beach (Hard)")
        b_dk_dock_h = world.get_location("Basketball Ex: Beat DK Dock (Hard)")
        b_luigi_mansion_h = world.get_location("Basketball Ex: Beat Luigi's Mansion (Hard)")
        b_western_junction_h = world.get_location("Basketball Ex: Beat Western Junction (Hard)")
        b_daisy_garden_h = world.get_location("Basketball Ex: Beat Daisy Garden (Hard)")
        b_bowser_jr_blvd_h = world.get_location("Basketball Ex: Beat Bowser Jr. Blvd. (Hard)")
        b_bowsers_castle_h = world.get_location("Basketball Ex: Beat Bowser's Castle (Hard)")
        b_star_ship_h = world.get_location("Basketball Ex: Beat Star Ship (Hard)")
        b_peach_castle_h = world.get_location("Basketball Ex: Beat Peach's Castle (Hard)")
        b_wario_factory_h = world.get_location("Basketball Ex: Beat Wario Factory (Hard)")
        b_ghoulish_galleon_h = world.get_location("Basketball Ex: Beat Ghoulish Galleon (Hard)")
        # Dodgeball
        d_mario_stadium_h = world.get_location("Dodgeball Ex: Beat Mario Stadium (Hard)")
        d_koopa_troopa_beach_h = world.get_location("Dodgeball Ex: Beat Koopa Troopa Beach (Hard)")
        d_dk_dock_h = world.get_location("Dodgeball Ex: Beat DK Dock (Hard)")
        d_western_junction_h = world.get_location("Dodgeball Ex: Beat Western Junction (Hard)")
        d_daisy_garden_h = world.get_location("Dodgeball Ex: Beat Daisy Garden (Hard)")
        d_bowsers_castle_h = world.get_location("Dodgeball Ex: Beat Bowser's Castle (Hard)")
        d_star_ship_h = world.get_location("Dodgeball Ex: Beat Star Ship (Hard)")
        d_peach_castle_h = world.get_location("Dodgeball Ex: Beat Peach's Castle (Hard)")
        d_wario_factory_h = world.get_location("Dodgeball Ex: Beat Wario Factory (Hard)")
        d_ghoulish_galleon_h = world.get_location("Dodgeball Ex: Beat Ghoulish Galleon (Hard)")
        d_toad_park_h = world.get_location("Dodgeball Ex: Beat Toad Park (Hard)")
        d_waluigi_pinball_h = world.get_location("Dodgeball Ex: Beat Waluigi Pinball (Hard)")
        # Volleyball
        v_mario_stadium_h = world.get_location("Volleyball Ex: Beat Mario Stadium (Hard)")
        v_koopa_troopa_beach_h = world.get_location("Volleyball Ex: Beat Koopa Troopa Beach (Hard)")
        v_dk_dock_h = world.get_location("Volleyball Ex: Beat DK Dock (Hard)")
        v_luigi_mansion_h = world.get_location("Volleyball Ex: Beat Luigi's Mansion (Hard)")
        v_western_junction_h = world.get_location("Volleyball Ex: Beat Western Junction (Hard)")
        v_bowser_jr_blvd_h = world.get_location("Volleyball Ex: Beat Bowser Jr. Blvd. (Hard)")
        v_bowsers_castle_h = world.get_location("Volleyball Ex: Beat Bowser's Castle (Hard)")
        v_star_ship_h = world.get_location("Volleyball Ex: Beat Star Ship (Hard)")
        v_peach_castle_h = world.get_location("Volleyball Ex: Beat Peach's Castle (Hard)")
        v_wario_factory_h = world.get_location("Volleyball Ex: Beat Wario Factory (Hard)")
        v_ghoulish_galleon_h = world.get_location("Volleyball Ex: Beat Ghoulish Galleon (Hard)")
        v_waluigi_pinball_h = world.get_location("Volleyball Ex: Beat Waluigi Pinball (Hard)")
        # Hockey
        h_mario_stadium_h = world.get_location("Hockey Ex: Beat Mario Stadium (Hard)")
        h_koopa_troopa_beach_h = world.get_location("Hockey Ex: Beat Koopa Troopa Beach (Hard)")
        h_western_junction_h = world.get_location("Hockey Ex: Beat Western Junction (Hard)")
        h_daisy_garden_h = world.get_location("Hockey Ex: Beat Daisy Garden (Hard)")
        h_bowser_jr_blvd_h = world.get_location("Hockey Ex: Beat Bowser Jr. Blvd. (Hard)")
        h_bowsers_castle_h = world.get_location("Hockey Ex: Beat Bowser's Castle (Hard)")
        h_star_ship_h = world.get_location("Hockey Ex: Beat Star Ship (Hard)")
        h_peach_castle_h = world.get_location("Hockey Ex: Beat Peach's Castle (Hard)")
        h_wario_factory_h = world.get_location("Hockey Ex: Beat Wario Factory (Hard)")
        h_ghoulish_galleon_h = world.get_location("Hockey Ex: Beat Ghoulish Galleon (Hard)")
        h_toad_park_h = world.get_location("Hockey Ex: Beat Toad Park (Hard)")
        h_waluigi_pinball_h = world.get_location("Hockey Ex: Beat Waluigi Pinball (Hard)")

        # Basketball
        world.set_rule(b_mario_stadium_h, has_mario_stadium)
        world.set_rule(b_koopa_troopa_beach_h, has_koopa_troopa_beach)
        world.set_rule(b_dk_dock_h, has_dk_dock)
        world.set_rule(b_luigi_mansion_h, has_luigi_mansion)
        world.set_rule(b_western_junction_h, has_western_junction)
        world.set_rule(b_daisy_garden_h, has_daisy_garden)
        world.set_rule(b_bowser_jr_blvd_h, has_bowser_jr_blvd)
        world.set_rule(b_bowsers_castle_h, has_bowser_castle)
        world.set_rule(b_star_ship_h, has_star_ship)
        world.set_rule(b_peach_castle_h, has_peach_castle)
        world.set_rule(b_wario_factory_h, has_wario_factory)
        world.set_rule(b_ghoulish_galleon_h, has_ghoulish_galleon)

        # Dodgeball
        world.set_rule(d_mario_stadium_h, has_mario_stadium)
        world.set_rule(d_koopa_troopa_beach_h, has_koopa_troopa_beach)
        world.set_rule(d_dk_dock_h, has_dk_dock)
        world.set_rule(d_western_junction_h, has_western_junction)
        world.set_rule(d_daisy_garden_h, has_daisy_garden)
        world.set_rule(d_bowsers_castle_h, has_bowser_castle)
        world.set_rule(d_star_ship_h, has_star_ship)
        world.set_rule(d_peach_castle_h, has_peach_castle)
        world.set_rule(d_wario_factory_h, has_wario_factory)
        world.set_rule(d_ghoulish_galleon_h, has_ghoulish_galleon)
        world.set_rule(d_toad_park_h, has_toad_park)
        world.set_rule(d_waluigi_pinball_h, has_waluigi_pinball)

        # Volleyball
        world.set_rule(v_mario_stadium_h, has_mario_stadium)
        world.set_rule(v_koopa_troopa_beach_h, has_koopa_troopa_beach)
        world.set_rule(v_dk_dock_h, has_dk_dock)
        world.set_rule(v_luigi_mansion_h, has_luigi_mansion)
        world.set_rule(v_western_junction_h, has_western_junction)
        world.set_rule(v_bowser_jr_blvd_h, has_bowser_jr_blvd)
        world.set_rule(v_bowsers_castle_h, has_bowser_castle)
        world.set_rule(v_star_ship_h, has_star_ship)
        world.set_rule(v_peach_castle_h, has_peach_castle)
        world.set_rule(v_wario_factory_h, has_wario_factory)
        world.set_rule(v_ghoulish_galleon_h, has_ghoulish_galleon)
        world.set_rule(v_waluigi_pinball_h, has_waluigi_pinball)

        # Hockey
        world.set_rule(h_mario_stadium_h, has_mario_stadium)
        world.set_rule(h_koopa_troopa_beach_h, has_koopa_troopa_beach)
        world.set_rule(h_western_junction_h, has_western_junction)
        world.set_rule(h_daisy_garden_h, has_daisy_garden)
        world.set_rule(h_bowser_jr_blvd_h, has_bowser_jr_blvd)
        world.set_rule(h_bowsers_castle_h, has_bowser_castle)
        world.set_rule(h_star_ship_h, has_star_ship)
        world.set_rule(h_peach_castle_h, has_peach_castle)
        world.set_rule(h_wario_factory_h, has_wario_factory)
        world.set_rule(h_ghoulish_galleon_h, has_ghoulish_galleon)
        world.set_rule(h_toad_park_h, has_toad_park)
        world.set_rule(h_waluigi_pinball_h, has_waluigi_pinball)

    if "Expert" in world.options.exhibition_difficulty:
        # Basketball
        b_mario_stadium_x = world.get_location("Basketball Ex: Beat Mario Stadium (Expert)")
        b_koopa_troopa_beach_x = world.get_location("Basketball Ex: Beat Koopa Troopa Beach (Expert)")
        b_dk_dock_x = world.get_location("Basketball Ex: Beat DK Dock (Expert)")
        b_luigi_mansion_x = world.get_location("Basketball Ex: Beat Luigi's Mansion (Expert)")
        b_western_junction_x = world.get_location("Basketball Ex: Beat Western Junction (Expert)")
        b_daisy_garden_x = world.get_location("Basketball Ex: Beat Daisy Garden (Expert)")
        b_bowser_jr_blvd_x = world.get_location("Basketball Ex: Beat Bowser Jr. Blvd. (Expert)")
        b_bowsers_castle_x = world.get_location("Basketball Ex: Beat Bowser's Castle (Expert)")
        b_star_ship_x = world.get_location("Basketball Ex: Beat Star Ship (Expert)")
        b_peach_castle_x = world.get_location("Basketball Ex: Beat Peach's Castle (Expert)")
        b_wario_factory_x = world.get_location("Basketball Ex: Beat Wario Factory (Expert)")
        b_ghoulish_galleon_x = world.get_location("Basketball Ex: Beat Ghoulish Galleon (Expert)")
        # Dodgeball
        d_mario_stadium_x = world.get_location("Dodgeball Ex: Beat Mario Stadium (Expert)")
        d_koopa_troopa_beach_x = world.get_location("Dodgeball Ex: Beat Koopa Troopa Beach (Expert)")
        d_dk_dock_x = world.get_location("Dodgeball Ex: Beat DK Dock (Expert)")
        d_western_junction_x = world.get_location("Dodgeball Ex: Beat Western Junction (Expert)")
        d_daisy_garden_x = world.get_location("Dodgeball Ex: Beat Daisy Garden (Expert)")
        d_bowsers_castle_x = world.get_location("Dodgeball Ex: Beat Bowser's Castle (Expert)")
        d_star_ship_x = world.get_location("Dodgeball Ex: Beat Star Ship (Expert)")
        d_peach_castle_x = world.get_location("Dodgeball Ex: Beat Peach's Castle (Expert)")
        d_wario_factory_x = world.get_location("Dodgeball Ex: Beat Wario Factory (Expert)")
        d_ghoulish_galleon_x = world.get_location("Dodgeball Ex: Beat Ghoulish Galleon (Expert)")
        d_toad_park_x = world.get_location("Dodgeball Ex: Beat Toad Park (Expert)")
        d_waluigi_pinball_x = world.get_location("Dodgeball Ex: Beat Waluigi Pinball (Expert)")
        # Volleyball
        v_mario_stadium_x = world.get_location("Volleyball Ex: Beat Mario Stadium (Expert)")
        v_koopa_troopa_beach_x = world.get_location("Volleyball Ex: Beat Koopa Troopa Beach (Expert)")
        v_dk_dock_x = world.get_location("Volleyball Ex: Beat DK Dock (Expert)")
        v_luigi_mansion_x = world.get_location("Volleyball Ex: Beat Luigi's Mansion (Expert)")
        v_western_junction_x = world.get_location("Volleyball Ex: Beat Western Junction (Expert)")
        v_bowser_jr_blvd_x = world.get_location("Volleyball Ex: Beat Bowser Jr. Blvd. (Expert)")
        v_bowsers_castle_x = world.get_location("Volleyball Ex: Beat Bowser's Castle (Expert)")
        v_star_ship_x = world.get_location("Volleyball Ex: Beat Star Ship (Expert)")
        v_peach_castle_x = world.get_location("Volleyball Ex: Beat Peach's Castle (Expert)")
        v_wario_factory_x = world.get_location("Volleyball Ex: Beat Wario Factory (Expert)")
        v_ghoulish_galleon_x = world.get_location("Volleyball Ex: Beat Ghoulish Galleon (Expert)")
        v_waluigi_pinball_x = world.get_location("Volleyball Ex: Beat Waluigi Pinball (Expert)")
        # Hockey
        h_mario_stadium_x = world.get_location("Hockey Ex: Beat Mario Stadium (Expert)")
        h_koopa_troopa_beach_x = world.get_location("Hockey Ex: Beat Koopa Troopa Beach (Expert)")
        h_western_junction_x = world.get_location("Hockey Ex: Beat Western Junction (Expert)")
        h_daisy_garden_x = world.get_location("Hockey Ex: Beat Daisy Garden (Expert)")
        h_bowser_jr_blvd_x = world.get_location("Hockey Ex: Beat Bowser Jr. Blvd. (Expert)")
        h_bowsers_castle_x = world.get_location("Hockey Ex: Beat Bowser's Castle (Expert)")
        h_star_ship_x = world.get_location("Hockey Ex: Beat Star Ship (Expert)")
        h_peach_castle_x = world.get_location("Hockey Ex: Beat Peach's Castle (Expert)")
        h_wario_factory_x = world.get_location("Hockey Ex: Beat Wario Factory (Expert)")
        h_ghoulish_galleon_x = world.get_location("Hockey Ex: Beat Ghoulish Galleon (Expert)")
        h_toad_park_x = world.get_location("Hockey Ex: Beat Toad Park (Expert)")
        h_waluigi_pinball_x = world.get_location("Hockey Ex: Beat Waluigi Pinball (Expert)")

        # Basketball
        world.set_rule(b_mario_stadium_x, has_mario_stadium)
        world.set_rule(b_koopa_troopa_beach_x, has_koopa_troopa_beach)
        world.set_rule(b_dk_dock_x, has_dk_dock)
        world.set_rule(b_luigi_mansion_x, has_luigi_mansion)
        world.set_rule(b_western_junction_x, has_western_junction)
        world.set_rule(b_daisy_garden_x, has_daisy_garden)
        world.set_rule(b_bowser_jr_blvd_x, has_bowser_jr_blvd)
        world.set_rule(b_bowsers_castle_x, has_bowser_castle)
        world.set_rule(b_star_ship_x, has_star_ship)
        world.set_rule(b_peach_castle_x, has_peach_castle)
        world.set_rule(b_wario_factory_x, has_wario_factory)
        world.set_rule(b_ghoulish_galleon_x, has_ghoulish_galleon)

        # Dodgeball
        world.set_rule(d_mario_stadium_x, has_mario_stadium)
        world.set_rule(d_koopa_troopa_beach_x, has_koopa_troopa_beach)
        world.set_rule(d_dk_dock_x, has_dk_dock)
        world.set_rule(d_western_junction_x, has_western_junction)
        world.set_rule(d_daisy_garden_x, has_daisy_garden)
        world.set_rule(d_bowsers_castle_x, has_bowser_castle)
        world.set_rule(d_star_ship_x, has_star_ship)
        world.set_rule(d_peach_castle_x, has_peach_castle)
        world.set_rule(d_wario_factory_x, has_wario_factory)
        world.set_rule(d_ghoulish_galleon_x, has_ghoulish_galleon)
        world.set_rule(d_toad_park_x, has_toad_park)
        world.set_rule(d_waluigi_pinball_x, has_waluigi_pinball)

        # Volleyball
        world.set_rule(v_mario_stadium_x, has_mario_stadium)
        world.set_rule(v_koopa_troopa_beach_x, has_koopa_troopa_beach)
        world.set_rule(v_dk_dock_x, has_dk_dock)
        world.set_rule(v_luigi_mansion_x, has_luigi_mansion)
        world.set_rule(v_western_junction_x, has_western_junction)
        world.set_rule(v_bowser_jr_blvd_x, has_bowser_jr_blvd)
        world.set_rule(v_bowsers_castle_x, has_bowser_castle)
        world.set_rule(v_star_ship_x, has_star_ship)
        world.set_rule(v_peach_castle_x, has_peach_castle)
        world.set_rule(v_wario_factory_x, has_wario_factory)
        world.set_rule(v_ghoulish_galleon_x, has_ghoulish_galleon)
        world.set_rule(v_waluigi_pinball_x, has_waluigi_pinball)

        # Hockey
        world.set_rule(h_mario_stadium_x, has_mario_stadium)
        world.set_rule(h_koopa_troopa_beach_x, has_koopa_troopa_beach)
        world.set_rule(h_western_junction_x, has_western_junction)
        world.set_rule(h_daisy_garden_x, has_daisy_garden)
        world.set_rule(h_bowser_jr_blvd_x, has_bowser_jr_blvd)
        world.set_rule(h_bowsers_castle_x, has_bowser_castle)
        world.set_rule(h_star_ship_x, has_star_ship)
        world.set_rule(h_peach_castle_x, has_peach_castle)
        world.set_rule(h_wario_factory_x, has_wario_factory)
        world.set_rule(h_ghoulish_galleon_x, has_ghoulish_galleon)
        world.set_rule(h_toad_park_x, has_toad_park)
        world.set_rule(h_waluigi_pinball_x, has_waluigi_pinball)



    # Basketball
    rule_b_mushroom_1 = Has("Stage: Mario Stadium")
    rule_b_mushroom_2 = HasAll("Stage: Mario Stadium", "Stage: Koopa Troopa Beach")
    rule_b_mushroom_3 = HasAll("Stage: Mario Stadium", "Stage: Koopa Troopa Beach", "Stage: DK Dock")
    rule_b_flower_1 = Has("Stage: Luigi's Mansion")
    rule_b_flower_2 = HasAll("Stage: Luigi's Mansion", "Stage: Western Junction")
    rule_b_flower_3 = HasAll("Stage: Luigi's Mansion", "Stage: Western Junction", "Stage: Daisy Garden")
    rule_b_star_1 = Has("Stage: Bowser Jr. Blvd.")
    rule_b_star_2 = HasAll("Stage: Bowser Jr. Blvd.", "Stage: Bowser's Castle")
    rule_b_star_3 = HasAll("Stage: Bowser Jr. Blvd.", "Stage: Bowser's Castle", "Stage: Star Ship")

    # Dodgeball
    rule_d_mushroom_1 = Has("Stage: Mario Stadium")
    rule_d_mushroom_2 = HasAll("Stage: Mario Stadium", "Stage: Koopa Troopa Beach")
    rule_d_mushroom_3 = HasAll("Stage: Mario Stadium", "Stage: Koopa Troopa Beach", "Stage: Peach's Castle")
    rule_d_flower_1 = Has("Stage: DK Dock")
    rule_d_flower_2 = HasAll("Stage: DK Dock", "Stage: Toad Park")
    rule_d_flower_3 = HasAll("Stage: DK Dock", "Stage: Toad Park", "Stage: Daisy Garden")
    rule_d_star_1 = Has("Stage: Wario Factory")
    rule_d_star_2 = HasAll("Stage: Wario Factory", "Stage: Bowser's Castle")
    rule_d_star_3 = HasAll("Stage: Wario Factory", "Stage: Bowser's Castle", "Stage: Star Ship")

    # Volleyball
    rule_v_mushroom_1 = Has("Stage: Mario Stadium")
    rule_v_mushroom_2 = HasAll("Stage: Mario Stadium", "Stage: Koopa Troopa Beach")
    rule_v_mushroom_3 = HasAll("Stage: Mario Stadium", "Stage: Koopa Troopa Beach", "Stage: Peach's Castle")
    rule_v_flower_1 = Has("Stage: DK Dock")
    rule_v_flower_2 = HasAll("Stage: DK Dock", "Stage: Luigi's Mansion")
    rule_v_flower_3 = HasAll("Stage: DK Dock", "Stage: Luigi's Mansion", "Stage: Western Junction")
    rule_v_star_1 = Has("Stage: Bowser Jr. Blvd.")
    rule_v_star_2 = HasAll("Stage: Bowser Jr. Blvd.", "Stage: Bowser's Castle")
    rule_v_star_3 = HasAll("Stage: Bowser Jr. Blvd.", "Stage: Bowser's Castle", "Stage: Star Ship")

    # Hockey
    rule_h_mushroom_1 = Has("Stage: Mario Stadium")
    rule_h_mushroom_2 = HasAll("Stage: Mario Stadium", "Stage: Toad Park")
    rule_h_mushroom_3 = HasAll("Stage: Mario Stadium", "Stage: Toad Park", "Stage: Peach's Castle")
    rule_h_flower_1 = Has("Stage: Western Junction")
    rule_h_flower_2 = HasAll("Stage: Western Junction", "Stage: Wario Factory")
    rule_h_flower_3 = HasAll("Stage: Western Junction", "Stage: Wario Factory", "Stage: Daisy Garden")
    rule_h_star_1 = Has("Stage: Bowser Jr. Blvd.")
    rule_h_star_2 = HasAll("Stage: Bowser Jr. Blvd.", "Stage: Waluigi Pinball")
    rule_h_star_3 = HasAll("Stage: Bowser Jr. Blvd.", "Stage: Waluigi Pinball", "Stage: Star Ship")




    # Location rules work no differently from Entrance rules.
    # Most of our locations are chests that can simply be opened by walking up to them.
    # Thus, their logical requirements are covered by the Entrance rules of the Entrances that were required to
    # reach the region that the chest sits in.
    # However, our two enemies work differently.
    # Entering the room with the enemy is not enough, you also need to have enough combat items to be able to defeat it.
    # So, we need to set requirements on the Locations themselves.
    # Since combat is a bit more complicated, we'll use this chance to cover some advanced access rule concepts.



    # In "set_all_entrance_rules", we had a rule for a location that doesn't always exist.
    # In this case, we had to check for its existence (by checking the player's chosen options) before setting the rule.
    # Other times, you may have a situation where a location can have two different rules depending on the options.
    # In our case, the enemy in the right room has more health if hard mode is selected,
    # so ontop of the Sword, the player will either need one more health or a Shield in hard mode.
    # First, let's make our sword condition.
    #can_defeat_basic_enemy: Rule = Has("Sword")

    # Next, we'll check whether hard mode has been chosen in the player options.
    #if world.options.hard_mode:
        # We'll make the condition for "Has a Shield or a Health Upgrade".
        # We can chain two "Has" conditions together with the | operator to make "Has Shield or has Health Upgrade".
        #can_withstand_a_hit = Has("Shield") | Has("Health Upgrade")

        # Now, we chain this rule to our Sword rule.
        # Since we want both conditions to be true, in this case, we have to chain them in an "and" way.
        # For this, we can use the & operator.
        #can_defeat_basic_enemy = can_defeat_basic_enemy & can_withstand_a_hit

    # Finally, we set our rule onto the Right Room Enemy Drop location.
    #right_room_enemy = world.get_location("Right Room Enemy Drop")
    #world.set_rule(right_room_enemy, can_defeat_basic_enemy)

    # For the final boss, we also need to chain multiple conditions.
    # First of all, you always need a Sword and a Shield.
    # So far, we used the | and & operators to chain "Has" rules.
    # Instead, we can also use HasAny for an or-chain of items, or HasAll for an and-chain of items.
    #has_sword_and_shield: Rule = HasAll("Sword", "Shield")

    # In hard mode, the player also needs both Health Upgrades to survive long enough to defeat the boss.
    # For this, we can use the optional "count" parameter for "Has".
    #has_both_health_upgrades = Has("Health Upgrade", count=2)

    # Previously, we used an "if world.options.hard_mode" condition to check if we should apply the extra requirement.
    # However, if you're comfortable with boolean logic, there is another way.
    # OptionFilter is a rule which just resolves to True if the option has the specified value, or False otherwise.
    #hard_mode_is_off = OptionFilter(HardMode, False)

    # Now we can combine our rule as follows.
    #can_defeat_final_boss = has_sword_and_shield & (hard_mode_is_off | has_both_health_upgrades)
    # If you're not as comfortable with boolean logic, it might be somewhat confusing why this is correct.
    # There is nothing wrong with using "if" conditions to check for options, if you find that easier to understand.

    # Finally, we apply the rule to our "Final Boss Defeated" event location.
    #final_boss = world.get_location("Final Boss Defeated")
    #world.set_rule(final_boss, can_defeat_final_boss)


def set_completion_condition(world: MSMWorld) -> None:
    world.set_completion_rule(Has("Victory"))



# One final comment about rules:
# If your world exclusively uses Rule Builder rules (like APQuest), it's worth trying CachedRuleBuilderWorld.
# CachedRuleBuilderWorld is a subclass of World that has a bunch of caching magic to make rules faster.
# Just have your world class subclass CachedRuleBuilderWorld instead of World:
#   class APQuestWorld(CachedRuleBuilderWorld): ...
# This may speed up your world, or it may make it slower.
# The exact factors are complex and not well understood, but there is no harm in trying it.
# Generate a few seeds and see if there is a noticeable difference!
# If you're wondering, author has checked: APQuest is too simple to see any benefits, so we'll stick with "World".