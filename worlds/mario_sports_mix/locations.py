from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import Location
from . import items
from .options import GoalCondition

if TYPE_CHECKING:
    from . import MSMWorld


class MSMLocation(Location):
    game = "Mario Sports Mix"

# class LocationData(str, int):
#     name: str
#     code: Optional[int]


def create_all_locations(world: "MSMWorld") -> None:
    create_regular_locations(world)
    create_events(world)


base_loc_id = 0


LOCATION_NAME_TO_ID = {
    # Basketball
    "Basketball: Beat Normal Mushroom Cup Round 1": base_loc_id + 1,
    "Basketball: Beat Normal Mushroom Cup Round 2": base_loc_id + 2,
    "Basketball: Beat Normal Mushroom Cup Round 3": base_loc_id + 3,
    "Basketball: Beat Normal Flower Cup Round 1": base_loc_id + 4,
    "Basketball: Beat Normal Flower Cup Round 2": base_loc_id + 5,
    "Basketball: Beat Normal Flower Cup Round 3": base_loc_id + 6,
    "Basketball: Beat Normal Star Cup Round 1": base_loc_id + 7,
    "Basketball: Beat Normal Star Cup Round 2": base_loc_id + 8,
    "Basketball: Beat Normal Star Cup Round 3": base_loc_id + 9,

    # Dodgeball
    "Dodgeball: Beat Normal Mushroom Cup Round 1": base_loc_id + 10,
    "Dodgeball: Beat Normal Mushroom Cup Round 2": base_loc_id + 11,
    "Dodgeball: Beat Normal Mushroom Cup Round 3": base_loc_id + 12,
    "Dodgeball: Beat Normal Flower Cup Round 1": base_loc_id + 13,
    "Dodgeball: Beat Normal Flower Cup Round 2": base_loc_id + 14,
    "Dodgeball: Beat Normal Flower Cup Round 3": base_loc_id + 15,
    "Dodgeball: Beat Normal Star Cup Round 1": base_loc_id + 16,
    "Dodgeball: Beat Normal Star Cup Round 2": base_loc_id + 17,
    "Dodgeball: Beat Normal Star Cup Round 3": base_loc_id + 18,

    # Volleyball
    "Volleyball: Beat Normal Mushroom Cup Round 1": base_loc_id + 19,
    "Volleyball: Beat Normal Mushroom Cup Round 2": base_loc_id + 20,
    "Volleyball: Beat Normal Mushroom Cup Round 3": base_loc_id + 21,
    "Volleyball: Beat Normal Flower Cup Round 1": base_loc_id + 22,
    "Volleyball: Beat Normal Flower Cup Round 2": base_loc_id + 23,
    "Volleyball: Beat Normal Flower Cup Round 3": base_loc_id + 24,
    "Volleyball: Beat Normal Star Cup Round 1": base_loc_id + 25,
    "Volleyball: Beat Normal Star Cup Round 2": base_loc_id + 26,
    "Volleyball: Beat Normal Star Cup Round 3": base_loc_id + 27,

    # Hockey
    "Hockey: Beat Normal Mushroom Cup Round 1": base_loc_id + 28,
    "Hockey: Beat Normal Mushroom Cup Round 2": base_loc_id + 29,
    "Hockey: Beat Normal Mushroom Cup Round 3": base_loc_id + 30,
    "Hockey: Beat Normal Flower Cup Round 1": base_loc_id + 31,
    "Hockey: Beat Normal Flower Cup Round 2": base_loc_id + 32,
    "Hockey: Beat Normal Flower Cup Round 3": base_loc_id + 33,
    "Hockey: Beat Normal Star Cup Round 1": base_loc_id + 34,
    "Hockey: Beat Normal Star Cup Round 2": base_loc_id + 35,
    "Hockey: Beat Normal Star Cup Round 3": base_loc_id + 36,

    # Basketball
    "Basketball: Beat Hard Mushroom Cup Round 1": base_loc_id + 37,
    "Basketball: Beat Hard Mushroom Cup Round 2": base_loc_id + 38,
    "Basketball: Beat Hard Mushroom Cup Round 3": base_loc_id + 39,
    "Basketball: Beat Hard Flower Cup Round 1": base_loc_id + 40,
    "Basketball: Beat Hard Flower Cup Round 2": base_loc_id + 41,
    "Basketball: Beat Hard Flower Cup Round 3": base_loc_id + 42,
    "Basketball: Beat Hard Star Cup Round 1": base_loc_id + 43,
    "Basketball: Beat Hard Star Cup Round 2": base_loc_id + 44,
    "Basketball: Beat Hard Star Cup Round 3": base_loc_id + 45,

    # Dodgeball
    "Dodgeball: Beat Hard Mushroom Cup Round 1": base_loc_id + 46,
    "Dodgeball: Beat Hard Mushroom Cup Round 2": base_loc_id + 47,
    "Dodgeball: Beat Hard Mushroom Cup Round 3": base_loc_id + 48,
    "Dodgeball: Beat Hard Flower Cup Round 1": base_loc_id + 49,
    "Dodgeball: Beat Hard Flower Cup Round 2": base_loc_id + 50,
    "Dodgeball: Beat Hard Flower Cup Round 3": base_loc_id + 51,
    "Dodgeball: Beat Hard Star Cup Round 1": base_loc_id + 52,
    "Dodgeball: Beat Hard Star Cup Round 2": base_loc_id + 53,
    "Dodgeball: Beat Hard Star Cup Round 3": base_loc_id + 54,

    # Volleyball
    "Volleyball: Beat Hard Mushroom Cup Round 1": base_loc_id + 55,
    "Volleyball: Beat Hard Mushroom Cup Round 2": base_loc_id + 56,
    "Volleyball: Beat Hard Mushroom Cup Round 3": base_loc_id + 57,
    "Volleyball: Beat Hard Flower Cup Round 1": base_loc_id + 58,
    "Volleyball: Beat Hard Flower Cup Round 2": base_loc_id + 59,
    "Volleyball: Beat Hard Flower Cup Round 3": base_loc_id + 60,
    "Volleyball: Beat Hard Star Cup Round 1": base_loc_id + 61,
    "Volleyball: Beat Hard Star Cup Round 2": base_loc_id + 62,
    "Volleyball: Beat Hard Star Cup Round 3": base_loc_id + 63,

    # Hockey
    "Hockey: Beat Hard Mushroom Cup Round 1": base_loc_id + 64,
    "Hockey: Beat Hard Mushroom Cup Round 2": base_loc_id + 65,
    "Hockey: Beat Hard Mushroom Cup Round 3": base_loc_id + 66,
    "Hockey: Beat Hard Flower Cup Round 1": base_loc_id + 67,
    "Hockey: Beat Hard Flower Cup Round 2": base_loc_id + 68,
    "Hockey: Beat Hard Flower Cup Round 3": base_loc_id + 69,
    "Hockey: Beat Hard Star Cup Round 1": base_loc_id + 70,
    "Hockey: Beat Hard Star Cup Round 2": base_loc_id + 71,
    "Hockey: Beat Hard Star Cup Round 3": base_loc_id + 72,

    # Sports Mix
    "Sports Mix: Beat Mushroom Cup Round 1": base_loc_id + 73,
    "Sports Mix: Beat Mushroom Cup Round 2": base_loc_id + 74,
    "Sports Mix: Beat Mushroom Cup Round 3": base_loc_id + 75,
    "Sports Mix: Beat Flower Cup Round 1": base_loc_id + 76,
    "Sports Mix: Beat Flower Cup Round 2": base_loc_id + 77,
    "Sports Mix: Beat Flower Cup Round 3": base_loc_id + 78,
    "Sports Mix: Beat Star Cup Round 1": base_loc_id + 79,
    "Sports Mix: Beat Star Cup Round 2": base_loc_id + 80,
    "Sports Mix: Beat Star Cup Round 3": base_loc_id + 81,



    # Easy Exhibition Locations
    # Basketball
    "Basketball Ex: Beat Mario Stadium (Easy)": base_loc_id + 200,
    "Basketball Ex: Beat Koopa Troopa Beach (Easy)": base_loc_id + 201,
    "Basketball Ex: Beat DK Dock (Easy)": base_loc_id + 202,
    "Basketball Ex: Beat Luigi's Mansion (Easy)": base_loc_id + 203,
    "Basketball Ex: Beat Western Junction (Easy)": base_loc_id + 204,
    "Basketball Ex: Beat Daisy Garden (Easy)": base_loc_id + 205,
    "Basketball Ex: Beat Bowser Jr. Blvd. (Easy)": base_loc_id + 206,
    "Basketball Ex: Beat Bowser's Castle (Easy)": base_loc_id + 207,
    "Basketball Ex: Beat Star Ship (Easy)": base_loc_id + 208,
    "Basketball Ex: Beat Peach's Castle (Easy)": base_loc_id + 209,
    "Basketball Ex: Beat Wario Factory (Easy)": base_loc_id + 210,
    "Basketball Ex: Beat Ghoulish Galleon (Easy)": base_loc_id + 211,

    # Dodgeball
    "Dodgeball Ex: Beat Mario Stadium (Easy)": base_loc_id + 212,
    "Dodgeball Ex: Beat Koopa Troopa Beach (Easy)": base_loc_id + 213,
    "Dodgeball Ex: Beat Peach's Castle (Easy)": base_loc_id + 214,
    "Dodgeball Ex: Beat DK Dock (Easy)": base_loc_id + 215,
    "Dodgeball Ex: Beat Toad Park (Easy)": base_loc_id + 216,
    "Dodgeball Ex: Beat Daisy Garden (Easy)": base_loc_id + 217,
    "Dodgeball Ex: Beat Wario Factory (Easy)": base_loc_id + 218,
    "Dodgeball Ex: Beat Bowser's Castle (Easy)": base_loc_id + 219,
    "Dodgeball Ex: Beat Star Ship (Easy)": base_loc_id + 220,
    "Dodgeball Ex: Beat Western Junction (Easy)": base_loc_id + 221,
    "Dodgeball Ex: Beat Waluigi Pinball (Easy)": base_loc_id + 222,
    "Dodgeball Ex: Beat Ghoulish Galleon (Easy)": base_loc_id + 223,

    # Volleyball
    "Volleyball Ex: Beat Mario Stadium (Easy)": base_loc_id + 224,
    "Volleyball Ex: Beat Koopa Troopa Beach (Easy)": base_loc_id + 225,
    "Volleyball Ex: Beat Peach's Castle (Easy)": base_loc_id + 226,
    "Volleyball Ex: Beat DK Dock (Easy)": base_loc_id + 227,
    "Volleyball Ex: Beat Luigi's Mansion (Easy)": base_loc_id + 228,
    "Volleyball Ex: Beat Western Junction (Easy)": base_loc_id + 229,
    "Volleyball Ex: Beat Bowser Jr. Blvd. (Easy)": base_loc_id + 230,
    "Volleyball Ex: Beat Bowser's Castle (Easy)": base_loc_id + 231,
    "Volleyball Ex: Beat Star Ship (Easy)": base_loc_id + 232,
    "Volleyball Ex: Beat Wario Factory (Easy)": base_loc_id + 233,
    "Volleyball Ex: Beat Waluigi Pinball (Easy)": base_loc_id + 234,
    "Volleyball Ex: Beat Ghoulish Galleon (Easy)": base_loc_id + 235,

    # Hockey
    "Hockey Ex: Beat Mario Stadium (Easy)": base_loc_id + 236,
    "Hockey Ex: Beat Toad Park (Easy)": base_loc_id + 237,
    "Hockey Ex: Beat Peach's Castle (Easy)": base_loc_id + 238,
    "Hockey Ex: Beat Western Junction (Easy)": base_loc_id + 239,
    "Hockey Ex: Beat Wario Factory (Easy)": base_loc_id + 240,
    "Hockey Ex: Beat Daisy Garden (Easy)": base_loc_id + 241,
    "Hockey Ex: Beat Bowser Jr. Blvd. (Easy)": base_loc_id + 242,
    "Hockey Ex: Beat Waluigi Pinball (Easy)": base_loc_id + 243,
    "Hockey Ex: Beat Star Ship (Easy)": base_loc_id + 244,
    "Hockey Ex: Beat Koopa Troopa Beach (Easy)": base_loc_id + 245,
    "Hockey Ex: Beat Ghoulish Galleon (Easy)": base_loc_id + 246,
    "Hockey Ex: Beat Bowser's Castle (Easy)": base_loc_id + 247,

    # Normal Exhibition Locations
    # Basketball
    "Basketball Ex: Beat Mario Stadium (Normal)": base_loc_id + 300,
    "Basketball Ex: Beat Koopa Troopa Beach (Normal)": base_loc_id + 301,
    "Basketball Ex: Beat DK Dock (Normal)": base_loc_id + 302,
    "Basketball Ex: Beat Luigi's Mansion (Normal)": base_loc_id + 303,
    "Basketball Ex: Beat Western Junction (Normal)": base_loc_id + 304,
    "Basketball Ex: Beat Daisy Garden (Normal)": base_loc_id + 305,
    "Basketball Ex: Beat Bowser Jr. Blvd. (Normal)": base_loc_id + 306,
    "Basketball Ex: Beat Bowser's Castle (Normal)": base_loc_id + 307,
    "Basketball Ex: Beat Star Ship (Normal)": base_loc_id + 308,
    "Basketball Ex: Beat Peach's Castle (Normal)": base_loc_id + 309,
    "Basketball Ex: Beat Wario Factory (Normal)": base_loc_id + 310,
    "Basketball Ex: Beat Ghoulish Galleon (Normal)": base_loc_id + 311,

    # Dodgeball
    "Dodgeball Ex: Beat Mario Stadium (Normal)": base_loc_id + 312,
    "Dodgeball Ex: Beat Koopa Troopa Beach (Normal)": base_loc_id + 313,
    "Dodgeball Ex: Beat Peach's Castle (Normal)": base_loc_id + 314,
    "Dodgeball Ex: Beat DK Dock (Normal)": base_loc_id + 315,
    "Dodgeball Ex: Beat Toad Park (Normal)": base_loc_id + 316,
    "Dodgeball Ex: Beat Daisy Garden (Normal)": base_loc_id + 317,
    "Dodgeball Ex: Beat Wario Factory (Normal)": base_loc_id + 318,
    "Dodgeball Ex: Beat Bowser's Castle (Normal)": base_loc_id + 319,
    "Dodgeball Ex: Beat Star Ship (Normal)": base_loc_id + 320,
    "Dodgeball Ex: Beat Western Junction (Normal)": base_loc_id + 321,
    "Dodgeball Ex: Beat Waluigi Pinball (Normal)": base_loc_id + 322,
    "Dodgeball Ex: Beat Ghoulish Galleon (Normal)": base_loc_id + 323,

    # Volleyball
    "Volleyball Ex: Beat Mario Stadium (Normal)": base_loc_id + 324,
    "Volleyball Ex: Beat Koopa Troopa Beach (Normal)": base_loc_id + 325,
    "Volleyball Ex: Beat Peach's Castle (Normal)": base_loc_id + 326,
    "Volleyball Ex: Beat DK Dock (Normal)": base_loc_id + 327,
    "Volleyball Ex: Beat Luigi's Mansion (Normal)": base_loc_id + 328,
    "Volleyball Ex: Beat Western Junction (Normal)": base_loc_id + 329,
    "Volleyball Ex: Beat Bowser Jr. Blvd. (Normal)": base_loc_id + 330,
    "Volleyball Ex: Beat Bowser's Castle (Normal)": base_loc_id + 331,
    "Volleyball Ex: Beat Star Ship (Normal)": base_loc_id + 332,
    "Volleyball Ex: Beat Wario Factory (Normal)": base_loc_id + 333,
    "Volleyball Ex: Beat Waluigi Pinball (Normal)": base_loc_id + 334,
    "Volleyball Ex: Beat Ghoulish Galleon (Normal)": base_loc_id + 335,

    # Hockey
    "Hockey Ex: Beat Mario Stadium (Normal)": base_loc_id + 336,
    "Hockey Ex: Beat Toad Park (Normal)": base_loc_id + 337,
    "Hockey Ex: Beat Peach's Castle (Normal)": base_loc_id + 338,
    "Hockey Ex: Beat Western Junction (Normal)": base_loc_id + 339,
    "Hockey Ex: Beat Wario Factory (Normal)": base_loc_id + 340,
    "Hockey Ex: Beat Daisy Garden (Normal)": base_loc_id + 341,
    "Hockey Ex: Beat Bowser Jr. Blvd. (Normal)": base_loc_id + 342,
    "Hockey Ex: Beat Waluigi Pinball (Normal)": base_loc_id + 343,
    "Hockey Ex: Beat Star Ship (Normal)": base_loc_id + 344,
    "Hockey Ex: Beat Koopa Troopa Beach (Normal)": base_loc_id + 345,
    "Hockey Ex: Beat Ghoulish Galleon (Normal)": base_loc_id + 346,
    "Hockey Ex: Beat Bowser's Castle (Normal)": base_loc_id + 347,

    # Hard Exhibition Locations
    #Basketball
    "Basketball Ex: Beat Mario Stadium (Hard)": base_loc_id + 400,
    "Basketball Ex: Beat Koopa Troopa Beach (Hard)": base_loc_id + 401,
    "Basketball Ex: Beat DK Dock (Hard)": base_loc_id + 402,
    "Basketball Ex: Beat Luigi's Mansion (Hard)": base_loc_id + 403,
    "Basketball Ex: Beat Western Junction (Hard)": base_loc_id + 404,
    "Basketball Ex: Beat Daisy Garden (Hard)": base_loc_id + 405,
    "Basketball Ex: Beat Bowser Jr. Blvd. (Hard)": base_loc_id + 406,
    "Basketball Ex: Beat Bowser's Castle (Hard)": base_loc_id + 407,
    "Basketball Ex: Beat Star Ship (Hard)": base_loc_id + 408,
    "Basketball Ex: Beat Peach's Castle (Hard)": base_loc_id + 409,
    "Basketball Ex: Beat Wario Factory (Hard)": base_loc_id + 410,
    "Basketball Ex: Beat Ghoulish Galleon (Hard)": base_loc_id + 411,

    # Dodgeball
    "Dodgeball Ex: Beat Mario Stadium (Hard)": base_loc_id + 412,
    "Dodgeball Ex: Beat Koopa Troopa Beach (Hard)": base_loc_id + 413,
    "Dodgeball Ex: Beat Peach's Castle (Hard)": base_loc_id + 414,
    "Dodgeball Ex: Beat DK Dock (Hard)": base_loc_id + 415,
    "Dodgeball Ex: Beat Toad Park (Hard)": base_loc_id + 416,
    "Dodgeball Ex: Beat Daisy Garden (Hard)": base_loc_id + 417,
    "Dodgeball Ex: Beat Wario Factory (Hard)": base_loc_id + 418,
    "Dodgeball Ex: Beat Bowser's Castle (Hard)": base_loc_id + 419,
    "Dodgeball Ex: Beat Star Ship (Hard)": base_loc_id + 420,
    "Dodgeball Ex: Beat Western Junction (Hard)": base_loc_id + 421,
    "Dodgeball Ex: Beat Waluigi Pinball (Hard)": base_loc_id + 422,
    "Dodgeball Ex: Beat Ghoulish Galleon (Hard)": base_loc_id + 423,

    # Volleyball
    "Volleyball Ex: Beat Mario Stadium (Hard)": base_loc_id + 424,
    "Volleyball Ex: Beat Koopa Troopa Beach (Hard)": base_loc_id + 425,
    "Volleyball Ex: Beat Peach's Castle (Hard)": base_loc_id + 426,
    "Volleyball Ex: Beat DK Dock (Hard)": base_loc_id + 427,
    "Volleyball Ex: Beat Luigi's Mansion (Hard)": base_loc_id + 428,
    "Volleyball Ex: Beat Western Junction (Hard)": base_loc_id + 429,
    "Volleyball Ex: Beat Bowser Jr. Blvd. (Hard)": base_loc_id + 430,
    "Volleyball Ex: Beat Bowser's Castle (Hard)": base_loc_id + 431,
    "Volleyball Ex: Beat Star Ship (Hard)": base_loc_id + 432,
    "Volleyball Ex: Beat Wario Factory (Hard)": base_loc_id + 433,
    "Volleyball Ex: Beat Waluigi Pinball (Hard)": base_loc_id + 434,
    "Volleyball Ex: Beat Ghoulish Galleon (Hard)": base_loc_id + 435,

    # Hockey
    "Hockey Ex: Beat Mario Stadium (Hard)": base_loc_id + 436,
    "Hockey Ex: Beat Toad Park (Hard)": base_loc_id + 437,
    "Hockey Ex: Beat Peach's Castle (Hard)": base_loc_id + 438,
    "Hockey Ex: Beat Western Junction (Hard)": base_loc_id + 439,
    "Hockey Ex: Beat Wario Factory (Hard)": base_loc_id + 440,
    "Hockey Ex: Beat Daisy Garden (Hard)": base_loc_id + 441,
    "Hockey Ex: Beat Bowser Jr. Blvd. (Hard)": base_loc_id + 442,
    "Hockey Ex: Beat Waluigi Pinball (Hard)": base_loc_id + 443,
    "Hockey Ex: Beat Star Ship (Hard)": base_loc_id + 444,
    "Hockey Ex: Beat Koopa Troopa Beach (Hard)": base_loc_id + 445,
    "Hockey Ex: Beat Ghoulish Galleon (Hard)": base_loc_id + 446,
    "Hockey Ex: Beat Bowser's Castle (Hard)": base_loc_id + 447,

    # Expert Exhibition Locations
    # Basketball
    "Basketball Ex: Beat Mario Stadium (Expert)": base_loc_id + 500,
    "Basketball Ex: Beat Koopa Troopa Beach (Expert)": base_loc_id + 501,
    "Basketball Ex: Beat DK Dock (Expert)": base_loc_id + 502,
    "Basketball Ex: Beat Luigi's Mansion (Expert)": base_loc_id + 503,
    "Basketball Ex: Beat Western Junction (Expert)": base_loc_id + 504,
    "Basketball Ex: Beat Daisy Garden (Expert)": base_loc_id + 505,
    "Basketball Ex: Beat Bowser Jr. Blvd. (Expert)": base_loc_id + 506,
    "Basketball Ex: Beat Bowser's Castle (Expert)": base_loc_id + 507,
    "Basketball Ex: Beat Star Ship (Expert)": base_loc_id + 508,
    "Basketball Ex: Beat Peach's Castle (Expert)": base_loc_id + 509,
    "Basketball Ex: Beat Wario Factory (Expert)": base_loc_id + 510,
    "Basketball Ex: Beat Ghoulish Galleon (Expert)": base_loc_id + 511,

    # Dodgeball
    "Dodgeball Ex: Beat Mario Stadium (Expert)": base_loc_id + 512,
    "Dodgeball Ex: Beat Koopa Troopa Beach (Expert)": base_loc_id + 513,
    "Dodgeball Ex: Beat Peach's Castle (Expert)": base_loc_id + 514,
    "Dodgeball Ex: Beat DK Dock (Expert)": base_loc_id + 515,
    "Dodgeball Ex: Beat Toad Park (Expert)": base_loc_id + 516,
    "Dodgeball Ex: Beat Daisy Garden (Expert)": base_loc_id + 517,
    "Dodgeball Ex: Beat Wario Factory (Expert)": base_loc_id + 518,
    "Dodgeball Ex: Beat Bowser's Castle (Expert)": base_loc_id + 519,
    "Dodgeball Ex: Beat Star Ship (Expert)": base_loc_id + 520,
    "Dodgeball Ex: Beat Western Junction (Expert)": base_loc_id + 521,
    "Dodgeball Ex: Beat Waluigi Pinball (Expert)": base_loc_id + 522,
    "Dodgeball Ex: Beat Ghoulish Galleon (Expert)": base_loc_id + 523,

    # Hockey
    "Volleyball Ex: Beat Mario Stadium (Expert)": base_loc_id + 524,
    "Volleyball Ex: Beat Koopa Troopa Beach (Expert)": base_loc_id + 525,
    "Volleyball Ex: Beat Peach's Castle (Expert)": base_loc_id + 526,
    "Volleyball Ex: Beat DK Dock (Expert)": base_loc_id + 527,
    "Volleyball Ex: Beat Luigi's Mansion (Expert)": base_loc_id + 528,
    "Volleyball Ex: Beat Western Junction (Expert)": base_loc_id + 529,
    "Volleyball Ex: Beat Bowser Jr. Blvd. (Expert)": base_loc_id + 530,
    "Volleyball Ex: Beat Bowser's Castle (Expert)": base_loc_id + 531,
    "Volleyball Ex: Beat Star Ship (Expert)": base_loc_id + 532,
    "Volleyball Ex: Beat Wario Factory (Expert)": base_loc_id + 533,
    "Volleyball Ex: Beat Waluigi Pinball (Expert)": base_loc_id + 534,
    "Volleyball Ex: Beat Ghoulish Galleon (Expert)": base_loc_id + 535,

    # Hockey
    "Hockey Ex: Beat Mario Stadium (Expert)": base_loc_id + 536,
    "Hockey Ex: Beat Toad Park (Expert)": base_loc_id + 537,
    "Hockey Ex: Beat Peach's Castle (Expert)": base_loc_id + 538,
    "Hockey Ex: Beat Western Junction (Expert)": base_loc_id + 539,
    "Hockey Ex: Beat Wario Factory (Expert)": base_loc_id + 540,
    "Hockey Ex: Beat Daisy Garden (Expert)": base_loc_id + 541,
    "Hockey Ex: Beat Bowser Jr. Blvd. (Expert)": base_loc_id + 542,
    "Hockey Ex: Beat Waluigi Pinball (Expert)": base_loc_id + 543,
    "Hockey Ex: Beat Star Ship (Expert)": base_loc_id + 544,
    "Hockey Ex: Beat Koopa Troopa Beach (Expert)": base_loc_id + 545,
    "Hockey Ex: Beat Ghoulish Galleon (Expert)": base_loc_id + 546,
    "Hockey Ex: Beat Bowser's Castle (Expert)": base_loc_id + 547,


   # Special Sanity Locations
    "Use Mario's Special!": base_loc_id + 560,
    "Use Luigi's Special!": base_loc_id + 561,
    "Use Peach's Special!": base_loc_id + 562,
    "Use Daisy's Special!": base_loc_id + 563,
    "Use Yoshi's Special!": base_loc_id + 564,
    "Use Wario's Special!": base_loc_id + 565,
    "Use Waluigi's Special!": base_loc_id + 566,
    "Use Donkey Kong's Special!": base_loc_id + 567,
    "Use Diddy Kong's Special!": base_loc_id + 568,
    "Use Toad's Special!": base_loc_id + 569,
    "Use Bowser's Special!": base_loc_id + 570,
    "Use Bowser Jr's Special!": base_loc_id + 571,
    "Use Moogle's Special!": base_loc_id + 572,
    "Use Cactuar's Special!": base_loc_id + 573,
    "Use Ninja's Special!": base_loc_id + 574,
    "Use White Mage's Special!": base_loc_id + 575,
    "Use Slime's Special!": base_loc_id + 576,
    "Use Black Mage's Special!": base_loc_id + 577,

    # Party Mode: Feed Petey Locations
    "FP: Get 10 Points!": base_loc_id + 600,
    "FP: Get 20 Points!": base_loc_id + 601,
    "FP: Get 30 Points!": base_loc_id + 602,
    "FP: Get 40 Points!": base_loc_id + 603,
    "FP: Get 50 Points!": base_loc_id + 604,
    "FP: Get 60 Points!": base_loc_id + 605,
    "FP: Get 70 Points!": base_loc_id + 606,
    "FP: Get 80 Points!": base_loc_id + 607,
    "FP: Get 90 Points!": base_loc_id + 608,
    "FP: Get 100 Points!": base_loc_id + 609,

    # If goal condition is defeating Behemoth King create an item for defeating Behemoth
    "Defeated Behemoth!": base_loc_id + 2000,

}


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_regular_locations(world: MSMWorld) -> None:
    main_menu = world.get_region("Main Menu")
    # Basketball
    b_exhibition_e = world.get_region("Basketball: Exhibition (Easy)")
    b_exhibition_n = world.get_region("Basketball: Exhibition (Normal)")
    b_exhibition_h = world.get_region("Basketball: Exhibition (Hard)")
    b_exhibition_ex = world.get_region("Basketball: Exhibition (Expert)")
    b_mushroom_cup_n = world.get_region("Basketball: Mushroom Cup (Normal)")
    b_flower_cup_n = world.get_region("Basketball: Flower Cup (Normal)")
    b_star_cup_n = world.get_region("Basketball: Star Cup (Normal)")
    b_mushroom_cup_h = world.get_region("Basketball: Mushroom Cup (Hard)")
    b_flower_cup_h = world.get_region("Basketball: Flower Cup (Hard)")
    b_star_cup_h = world.get_region("Basketball: Star Cup (Hard)")
    # Dodgeball
    d_exhibition_e = world.get_region("Dodgeball: Exhibition (Easy)")
    d_exhibition_n = world.get_region("Dodgeball: Exhibition (Normal)")
    d_exhibition_h = world.get_region("Dodgeball: Exhibition (Hard)")
    d_exhibition_ex = world.get_region("Dodgeball: Exhibition (Expert)")
    d_mushroom_cup_n = world.get_region("Dodgeball: Mushroom Cup (Normal)")
    d_flower_cup_n = world.get_region("Dodgeball: Flower Cup (Normal)")
    d_star_cup_n = world.get_region("Dodgeball: Star Cup (Normal)")
    d_mushroom_cup_h = world.get_region("Dodgeball: Mushroom Cup (Hard)")
    d_flower_cup_h = world.get_region("Dodgeball: Flower Cup (Hard)")
    d_star_cup_h = world.get_region("Dodgeball: Star Cup (Hard)")
    # Volleyball
    v_exhibition_e = world.get_region("Volleyball: Exhibition (Easy)")
    v_exhibition_n = world.get_region("Volleyball: Exhibition (Normal)")
    v_exhibition_h = world.get_region("Volleyball: Exhibition (Hard)")
    v_exhibition_ex = world.get_region("Volleyball: Exhibition (Expert)")
    v_mushroom_cup_n = world.get_region("Volleyball: Mushroom Cup (Normal)")
    v_flower_cup_n = world.get_region("Volleyball: Flower Cup (Normal)")
    v_star_cup_n = world.get_region("Volleyball: Star Cup (Normal)")
    v_mushroom_cup_h = world.get_region("Volleyball: Mushroom Cup (Hard)")
    v_flower_cup_h = world.get_region("Volleyball: Flower Cup (Hard)")
    v_star_cup_h = world.get_region("Volleyball: Star Cup (Hard)")
    # Hockey
    h_exhibition_e = world.get_region("Hockey: Exhibition (Easy)")
    h_exhibition_n = world.get_region("Hockey: Exhibition (Normal)")
    h_exhibition_h = world.get_region("Hockey: Exhibition (Hard)")
    h_exhibition_ex = world.get_region("Hockey: Exhibition (Expert)")
    h_mushroom_cup_n = world.get_region("Hockey: Mushroom Cup (Normal)")
    h_flower_cup_n = world.get_region("Hockey: Flower Cup (Normal)")
    h_star_cup_n = world.get_region("Hockey: Star Cup (Normal)")
    h_mushroom_cup_h = world.get_region("Hockey: Mushroom Cup (Hard)")
    h_flower_cup_h = world.get_region("Hockey: Flower Cup (Hard)")
    h_star_cup_h = world.get_region("Hockey: Star Cup (Hard)")
    # Sports Mix
    sports_mix_mushroom = world.get_region("Sports Mix: Mushroom Cup")
    sm_mushroom_locations = get_location_names_with_ids(["Sports Mix: Beat Mushroom Cup Round 1",
    "Sports Mix: Beat Mushroom Cup Round 2", "Sports Mix: Beat Mushroom Cup Round 3"])
    sports_mix_mushroom.add_locations(sm_mushroom_locations, MSMLocation)
    sports_mix_flower = world.get_region("Sports Mix: Flower Cup")
    sm_flower_locations = get_location_names_with_ids(["Sports Mix: Beat Flower Cup Round 1",
    "Sports Mix: Beat Flower Cup Round 2", "Sports Mix: Beat Flower Cup Round 3"])
    sports_mix_flower.add_locations(sm_flower_locations, MSMLocation)
    sports_mix_star = world.get_region("Sports Mix: Star Cup")
    sm_star_locations = get_location_names_with_ids(["Sports Mix: Beat Star Cup Round 1",
    "Sports Mix: Beat Star Cup Round 2", "Sports Mix: Beat Star Cup Round 3"])
    sports_mix_star.add_locations(sm_star_locations, MSMLocation)

    feed_petey = world.get_region("Party Mode: Feed Petey")
    feed_petey_locations = get_location_names_with_ids(["FP: Get 10 Points!", "FP: Get 20 Points!", "FP: Get 30 Points!",
    "FP: Get 40 Points!", "FP: Get 50 Points!", "FP: Get 60 Points!", "FP: Get 70 Points!", "FP: Get 80 Points!",
    "FP: Get 90 Points!", "FP: Get 100 Points!"])
    feed_petey.add_locations(feed_petey_locations, MSMLocation)

    # Normal Difficulty

    # Basketball (Normal)
    b_mushroom_n_locations = get_location_names_with_ids(["Basketball: Beat Normal Mushroom Cup Round 1",
    "Basketball: Beat Normal Mushroom Cup Round 2", "Basketball: Beat Normal Mushroom Cup Round 3"])
    b_mushroom_cup_n.add_locations(b_mushroom_n_locations, MSMLocation)
    b_flower_n_locations = get_location_names_with_ids(["Basketball: Beat Normal Flower Cup Round 1",
    "Basketball: Beat Normal Flower Cup Round 2", "Basketball: Beat Normal Flower Cup Round 3"])
    b_flower_cup_n.add_locations(b_flower_n_locations, MSMLocation)
    b_star_n_locations = get_location_names_with_ids(["Basketball: Beat Normal Star Cup Round 1",
    "Basketball: Beat Normal Star Cup Round 2", "Basketball: Beat Normal Star Cup Round 3"])
    b_star_cup_n.add_locations(b_star_n_locations, MSMLocation)

    # Dodgeball (Normal)
    d_mushroom_n_locations = get_location_names_with_ids(["Dodgeball: Beat Normal Mushroom Cup Round 1",
    "Dodgeball: Beat Normal Mushroom Cup Round 2", "Dodgeball: Beat Normal Mushroom Cup Round 3"])
    d_mushroom_cup_n.add_locations(d_mushroom_n_locations, MSMLocation)
    d_flower_n_locations = get_location_names_with_ids(["Dodgeball: Beat Normal Flower Cup Round 1",
    "Dodgeball: Beat Normal Flower Cup Round 2", "Dodgeball: Beat Normal Flower Cup Round 3"])
    d_flower_cup_n.add_locations(d_flower_n_locations, MSMLocation)
    d_star_n_locations = get_location_names_with_ids(["Dodgeball: Beat Normal Star Cup Round 1",
    "Dodgeball: Beat Normal Star Cup Round 2", "Dodgeball: Beat Normal Star Cup Round 3"])
    d_star_cup_n.add_locations(d_star_n_locations, MSMLocation)

    # Volleyball (Normal)
    v_mushroom_n_locations = get_location_names_with_ids(["Volleyball: Beat Normal Mushroom Cup Round 1",
    "Volleyball: Beat Normal Mushroom Cup Round 2", "Volleyball: Beat Normal Mushroom Cup Round 3"])
    v_mushroom_cup_n.add_locations(v_mushroom_n_locations, MSMLocation)
    v_flower_n_locations = get_location_names_with_ids(["Volleyball: Beat Normal Flower Cup Round 1",
    "Volleyball: Beat Normal Flower Cup Round 2", "Volleyball: Beat Normal Flower Cup Round 3"])
    v_flower_cup_n.add_locations(v_flower_n_locations, MSMLocation)
    v_star_n_locations = get_location_names_with_ids(["Volleyball: Beat Normal Star Cup Round 1",
    "Volleyball: Beat Normal Star Cup Round 2", "Volleyball: Beat Normal Star Cup Round 3"])
    v_star_cup_n.add_locations(v_star_n_locations, MSMLocation)

    # Hockey (Normal)
    h_mushroom_n_locations = get_location_names_with_ids(["Hockey: Beat Normal Mushroom Cup Round 1",
    "Hockey: Beat Normal Mushroom Cup Round 2", "Hockey: Beat Normal Mushroom Cup Round 3"])
    h_mushroom_cup_n.add_locations(h_mushroom_n_locations, MSMLocation)
    h_flower_n_locations = get_location_names_with_ids(["Hockey: Beat Normal Flower Cup Round 1",
    "Hockey: Beat Normal Flower Cup Round 2", "Hockey: Beat Normal Flower Cup Round 3"])
    h_flower_cup_n.add_locations(h_flower_n_locations, MSMLocation)
    h_star_n_locations = get_location_names_with_ids(["Hockey: Beat Normal Star Cup Round 1",
    "Hockey: Beat Normal Star Cup Round 2", "Hockey: Beat Normal Star Cup Round 3"])
    h_star_cup_n.add_locations(h_star_n_locations, MSMLocation)

    # Hard Difficulty

    # Basketball (Hard)
    b_mushroom_h_locations = get_location_names_with_ids(["Basketball: Beat Hard Mushroom Cup Round 1",
    "Basketball: Beat Hard Mushroom Cup Round 2", "Basketball: Beat Hard Mushroom Cup Round 3"])
    b_mushroom_cup_h.add_locations(b_mushroom_h_locations, MSMLocation)
    b_flower_h_locations = get_location_names_with_ids(["Basketball: Beat Hard Flower Cup Round 1",
    "Basketball: Beat Hard Flower Cup Round 2", "Basketball: Beat Hard Flower Cup Round 3"])
    b_flower_cup_h.add_locations(b_flower_h_locations, MSMLocation)
    b_star_h_locations = get_location_names_with_ids(["Basketball: Beat Hard Star Cup Round 1",
    "Basketball: Beat Hard Star Cup Round 2", "Basketball: Beat Hard Star Cup Round 3"])
    b_star_cup_h.add_locations(b_star_h_locations, MSMLocation)

    # Dodgeball (Hard)
    d_mushroom_h_locations = get_location_names_with_ids(["Dodgeball: Beat Hard Mushroom Cup Round 1",
    "Dodgeball: Beat Hard Mushroom Cup Round 2", "Dodgeball: Beat Hard Mushroom Cup Round 3"])
    d_mushroom_cup_h.add_locations(d_mushroom_h_locations, MSMLocation)
    d_flower_h_locations = get_location_names_with_ids(["Dodgeball: Beat Hard Flower Cup Round 1",
    "Dodgeball: Beat Hard Flower Cup Round 2", "Dodgeball: Beat Hard Flower Cup Round 3"])
    d_flower_cup_h.add_locations(d_flower_h_locations, MSMLocation)
    d_star_h_locations = get_location_names_with_ids(["Dodgeball: Beat Hard Star Cup Round 1",
    "Dodgeball: Beat Hard Star Cup Round 2", "Dodgeball: Beat Hard Star Cup Round 3"])
    d_star_cup_h.add_locations(d_star_h_locations, MSMLocation)

    # Volleyball (Hard)
    v_mushroom_h_locations = get_location_names_with_ids(["Volleyball: Beat Hard Mushroom Cup Round 1",
    "Volleyball: Beat Hard Mushroom Cup Round 2", "Volleyball: Beat Hard Mushroom Cup Round 3"])
    v_mushroom_cup_h.add_locations(v_mushroom_h_locations, MSMLocation)
    v_flower_h_locations = get_location_names_with_ids(["Volleyball: Beat Hard Flower Cup Round 1",
    "Volleyball: Beat Hard Flower Cup Round 2", "Volleyball: Beat Hard Flower Cup Round 3"])
    v_flower_cup_h.add_locations(v_flower_h_locations, MSMLocation)
    v_star_h_locations = get_location_names_with_ids(["Volleyball: Beat Hard Star Cup Round 1",
    "Volleyball: Beat Hard Star Cup Round 2", "Volleyball: Beat Hard Star Cup Round 3"])
    v_star_cup_h.add_locations(v_star_h_locations, MSMLocation)

    # Hockey (Hard)
    h_mushroom_h_locations = get_location_names_with_ids(["Hockey: Beat Hard Mushroom Cup Round 1",
    "Hockey: Beat Hard Mushroom Cup Round 2", "Hockey: Beat Hard Mushroom Cup Round 3"])
    h_mushroom_cup_h.add_locations(h_mushroom_h_locations, MSMLocation)
    h_flower_h_locations = get_location_names_with_ids(["Hockey: Beat Hard Flower Cup Round 1",
    "Hockey: Beat Hard Flower Cup Round 2", "Hockey: Beat Hard Flower Cup Round 3"])
    h_flower_cup_h.add_locations(h_flower_h_locations, MSMLocation)
    h_star_h_locations = get_location_names_with_ids(["Hockey: Beat Hard Star Cup Round 1",
    "Hockey: Beat Hard Star Cup Round 2", "Hockey: Beat Hard Star Cup Round 3"])
    h_star_cup_h.add_locations(h_star_h_locations, MSMLocation)

    # Exhibition Locations for each difficulty
    # Basketball
    b_exhibition_locations_e = get_location_names_with_ids([
    "Basketball Ex: Beat Mario Stadium (Easy)",
    "Basketball Ex: Beat Koopa Troopa Beach (Easy)",
    "Basketball Ex: Beat DK Dock (Easy)",
    "Basketball Ex: Beat Luigi's Mansion (Easy)",
    "Basketball Ex: Beat Western Junction (Easy)",
    "Basketball Ex: Beat Daisy Garden (Easy)",
    "Basketball Ex: Beat Bowser Jr. Blvd. (Easy)",
    "Basketball Ex: Beat Bowser's Castle (Easy)",
    "Basketball Ex: Beat Star Ship (Easy)",
    "Basketball Ex: Beat Peach's Castle (Easy)",
    "Basketball Ex: Beat Wario Factory (Easy)",
    "Basketball Ex: Beat Ghoulish Galleon (Easy)"])
    b_exhibition_locations_n = get_location_names_with_ids(["Basketball Ex: Beat Mario Stadium (Normal)",
    "Basketball Ex: Beat Koopa Troopa Beach (Normal)",
    "Basketball Ex: Beat DK Dock (Normal)",
    "Basketball Ex: Beat Luigi's Mansion (Normal)",
    "Basketball Ex: Beat Western Junction (Normal)",
    "Basketball Ex: Beat Daisy Garden (Normal)",
    "Basketball Ex: Beat Bowser Jr. Blvd. (Normal)",
    "Basketball Ex: Beat Bowser's Castle (Normal)",
    "Basketball Ex: Beat Star Ship (Normal)",
    "Basketball Ex: Beat Peach's Castle (Normal)",
    "Basketball Ex: Beat Wario Factory (Normal)",
    "Basketball Ex: Beat Ghoulish Galleon (Normal)"])
    b_exhibition_locations_h = get_location_names_with_ids(["Basketball Ex: Beat Mario Stadium (Hard)",
    "Basketball Ex: Beat Koopa Troopa Beach (Hard)",
    "Basketball Ex: Beat DK Dock (Hard)",
    "Basketball Ex: Beat Luigi's Mansion (Hard)",
    "Basketball Ex: Beat Western Junction (Hard)",
    "Basketball Ex: Beat Daisy Garden (Hard)",
    "Basketball Ex: Beat Bowser Jr. Blvd. (Hard)",
    "Basketball Ex: Beat Bowser's Castle (Hard)",
    "Basketball Ex: Beat Star Ship (Hard)",
    "Basketball Ex: Beat Peach's Castle (Hard)",
    "Basketball Ex: Beat Wario Factory (Hard)",
    "Basketball Ex: Beat Ghoulish Galleon (Hard)"])
    b_exhibition_locations_ex = get_location_names_with_ids(["Basketball Ex: Beat Mario Stadium (Expert)",
    "Basketball Ex: Beat Koopa Troopa Beach (Expert)",
    "Basketball Ex: Beat DK Dock (Expert)",
    "Basketball Ex: Beat Luigi's Mansion (Expert)",
    "Basketball Ex: Beat Western Junction (Expert)",
    "Basketball Ex: Beat Daisy Garden (Expert)",
    "Basketball Ex: Beat Bowser Jr. Blvd. (Expert)",
    "Basketball Ex: Beat Bowser's Castle (Expert)",
    "Basketball Ex: Beat Star Ship (Expert)",
    "Basketball Ex: Beat Peach's Castle (Expert)",
    "Basketball Ex: Beat Wario Factory (Expert)",
    "Basketball Ex: Beat Ghoulish Galleon (Expert)"])
    b_exhibition_e.add_locations(b_exhibition_locations_e)
    b_exhibition_n.add_locations(b_exhibition_locations_n)
    b_exhibition_h.add_locations(b_exhibition_locations_h)
    b_exhibition_ex.add_locations(b_exhibition_locations_ex)
    # Dodgeball
    d_exhibition_locations_e = get_location_names_with_ids([
    "Dodgeball Ex: Beat Mario Stadium (Easy)",
    "Dodgeball Ex: Beat Koopa Troopa Beach (Easy)",
    "Dodgeball Ex: Beat Peach's Castle (Easy)",
    "Dodgeball Ex: Beat DK Dock (Easy)",
    "Dodgeball Ex: Beat Toad Park (Easy)",
    "Dodgeball Ex: Beat Daisy Garden (Easy)",
    "Dodgeball Ex: Beat Wario Factory (Easy)",
    "Dodgeball Ex: Beat Bowser's Castle (Easy)",
    "Dodgeball Ex: Beat Star Ship (Easy)",
    "Dodgeball Ex: Beat Western Junction (Easy)",
    "Dodgeball Ex: Beat Waluigi Pinball (Easy)",
    "Dodgeball Ex: Beat Ghoulish Galleon (Easy)"])
    d_exhibition_locations_n = get_location_names_with_ids([
    "Dodgeball Ex: Beat Mario Stadium (Normal)",
    "Dodgeball Ex: Beat Koopa Troopa Beach (Normal)",
    "Dodgeball Ex: Beat Peach's Castle (Normal)",
    "Dodgeball Ex: Beat DK Dock (Normal)",
    "Dodgeball Ex: Beat Toad Park (Normal)",
    "Dodgeball Ex: Beat Daisy Garden (Normal)",
    "Dodgeball Ex: Beat Wario Factory (Normal)",
    "Dodgeball Ex: Beat Bowser's Castle (Normal)",
    "Dodgeball Ex: Beat Star Ship (Normal)",
    "Dodgeball Ex: Beat Western Junction (Normal)",
    "Dodgeball Ex: Beat Waluigi Pinball (Normal)",
    "Dodgeball Ex: Beat Ghoulish Galleon (Normal)"])
    d_exhibition_locations_h = get_location_names_with_ids([
    "Dodgeball Ex: Beat Mario Stadium (Hard)",
    "Dodgeball Ex: Beat Koopa Troopa Beach (Hard)",
    "Dodgeball Ex: Beat Peach's Castle (Hard)",
    "Dodgeball Ex: Beat DK Dock (Hard)",
    "Dodgeball Ex: Beat Toad Park (Hard)",
    "Dodgeball Ex: Beat Daisy Garden (Hard)",
    "Dodgeball Ex: Beat Wario Factory (Hard)",
    "Dodgeball Ex: Beat Bowser's Castle (Hard)",
    "Dodgeball Ex: Beat Star Ship (Hard)",
    "Dodgeball Ex: Beat Western Junction (Hard)",
    "Dodgeball Ex: Beat Waluigi Pinball (Hard)",
    "Dodgeball Ex: Beat Ghoulish Galleon (Hard)"])
    d_exhibition_locations_ex = get_location_names_with_ids([
    "Dodgeball Ex: Beat Mario Stadium (Expert)",
    "Dodgeball Ex: Beat Koopa Troopa Beach (Expert)",
    "Dodgeball Ex: Beat Peach's Castle (Expert)",
    "Dodgeball Ex: Beat DK Dock (Expert)",
    "Dodgeball Ex: Beat Toad Park (Expert)",
    "Dodgeball Ex: Beat Daisy Garden (Expert)",
    "Dodgeball Ex: Beat Wario Factory (Expert)",
    "Dodgeball Ex: Beat Bowser's Castle (Expert)",
    "Dodgeball Ex: Beat Star Ship (Expert)",
    "Dodgeball Ex: Beat Western Junction (Expert)",
    "Dodgeball Ex: Beat Waluigi Pinball (Expert)",
    "Dodgeball Ex: Beat Ghoulish Galleon (Expert)"])
    d_exhibition_e.add_locations(d_exhibition_locations_e)
    d_exhibition_n.add_locations(d_exhibition_locations_n)
    d_exhibition_h.add_locations(d_exhibition_locations_h)
    d_exhibition_ex.add_locations(d_exhibition_locations_ex)
    # Volleyball
    v_exhibition_locations_e = get_location_names_with_ids([
        "Volleyball Ex: Beat Mario Stadium (Easy)",
        "Volleyball Ex: Beat Koopa Troopa Beach (Easy)",
        "Volleyball Ex: Beat Peach's Castle (Easy)",
        "Volleyball Ex: Beat DK Dock (Easy)",
        "Volleyball Ex: Beat Luigi's Mansion (Easy)",
        "Volleyball Ex: Beat Western Junction (Easy)",
        "Volleyball Ex: Beat Bowser Jr. Blvd. (Easy)",
        "Volleyball Ex: Beat Bowser's Castle (Easy)",
        "Volleyball Ex: Beat Star Ship (Easy)",
        "Volleyball Ex: Beat Wario Factory (Easy)",
        "Volleyball Ex: Beat Waluigi Pinball (Easy)",
        "Volleyball Ex: Beat Ghoulish Galleon (Easy)"])
    v_exhibition_locations_n = get_location_names_with_ids([
        "Volleyball Ex: Beat Mario Stadium (Normal)",
        "Volleyball Ex: Beat Koopa Troopa Beach (Normal)",
        "Volleyball Ex: Beat Peach's Castle (Normal)",
        "Volleyball Ex: Beat DK Dock (Normal)",
        "Volleyball Ex: Beat Luigi's Mansion (Normal)",
        "Volleyball Ex: Beat Western Junction (Normal)",
        "Volleyball Ex: Beat Bowser Jr. Blvd. (Normal)",
        "Volleyball Ex: Beat Bowser's Castle (Normal)",
        "Volleyball Ex: Beat Star Ship (Normal)",
        "Volleyball Ex: Beat Wario Factory (Normal)",
        "Volleyball Ex: Beat Waluigi Pinball (Normal)",
        "Volleyball Ex: Beat Ghoulish Galleon (Normal)"])
    v_exhibition_locations_h = get_location_names_with_ids([
        "Volleyball Ex: Beat Mario Stadium (Hard)",
        "Volleyball Ex: Beat Koopa Troopa Beach (Hard)",
        "Volleyball Ex: Beat Peach's Castle (Hard)",
        "Volleyball Ex: Beat DK Dock (Hard)",
        "Volleyball Ex: Beat Luigi's Mansion (Hard)",
        "Volleyball Ex: Beat Western Junction (Hard)",
        "Volleyball Ex: Beat Bowser Jr. Blvd. (Hard)",
        "Volleyball Ex: Beat Bowser's Castle (Hard)",
        "Volleyball Ex: Beat Star Ship (Hard)",
        "Volleyball Ex: Beat Wario Factory (Hard)",
        "Volleyball Ex: Beat Waluigi Pinball (Hard)",
        "Volleyball Ex: Beat Ghoulish Galleon (Hard)"])
    v_exhibition_locations_ex = get_location_names_with_ids([
        "Volleyball Ex: Beat Mario Stadium (Expert)",
        "Volleyball Ex: Beat Koopa Troopa Beach (Expert)",
        "Volleyball Ex: Beat Peach's Castle (Expert)",
        "Volleyball Ex: Beat DK Dock (Expert)",
        "Volleyball Ex: Beat Luigi's Mansion (Expert)",
        "Volleyball Ex: Beat Western Junction (Expert)",
        "Volleyball Ex: Beat Bowser Jr. Blvd. (Expert)",
        "Volleyball Ex: Beat Bowser's Castle (Expert)",
        "Volleyball Ex: Beat Star Ship (Expert)",
        "Volleyball Ex: Beat Wario Factory (Expert)",
        "Volleyball Ex: Beat Waluigi Pinball (Expert)",
        "Volleyball Ex: Beat Ghoulish Galleon (Expert)"])
    v_exhibition_e.add_locations(v_exhibition_locations_e)
    v_exhibition_n.add_locations(v_exhibition_locations_n)
    v_exhibition_h.add_locations(v_exhibition_locations_h)
    v_exhibition_ex.add_locations(v_exhibition_locations_ex)
    # Hockey
    h_exhibition_locations_e = get_location_names_with_ids([
        "Hockey Ex: Beat Mario Stadium (Easy)",
        "Hockey Ex: Beat Toad Park (Easy)",
        "Hockey Ex: Beat Peach's Castle (Easy)",
        "Hockey Ex: Beat Western Junction (Easy)",
        "Hockey Ex: Beat Wario Factory (Easy)",
        "Hockey Ex: Beat Daisy Garden (Easy)",
        "Hockey Ex: Beat Bowser Jr. Blvd. (Easy)",
        "Hockey Ex: Beat Waluigi Pinball (Easy)",
        "Hockey Ex: Beat Star Ship (Easy)",
        "Hockey Ex: Beat Koopa Troopa Beach (Easy)",
        "Hockey Ex: Beat Ghoulish Galleon (Easy)",
        "Hockey Ex: Beat Bowser's Castle (Easy)"])
    h_exhibition_locations_n = get_location_names_with_ids([
        "Hockey Ex: Beat Mario Stadium (Normal)",
        "Hockey Ex: Beat Toad Park (Normal)",
        "Hockey Ex: Beat Peach's Castle (Normal)",
        "Hockey Ex: Beat Western Junction (Normal)",
        "Hockey Ex: Beat Wario Factory (Normal)",
        "Hockey Ex: Beat Daisy Garden (Normal)",
        "Hockey Ex: Beat Bowser Jr. Blvd. (Normal)",
        "Hockey Ex: Beat Waluigi Pinball (Normal)",
        "Hockey Ex: Beat Star Ship (Normal)",
        "Hockey Ex: Beat Koopa Troopa Beach (Normal)",
        "Hockey Ex: Beat Ghoulish Galleon (Normal)",
        "Hockey Ex: Beat Bowser's Castle (Normal)"])
    h_exhibition_locations_h = get_location_names_with_ids([
        "Hockey Ex: Beat Mario Stadium (Hard)",
        "Hockey Ex: Beat Toad Park (Hard)",
        "Hockey Ex: Beat Peach's Castle (Hard)",
        "Hockey Ex: Beat Western Junction (Hard)",
        "Hockey Ex: Beat Wario Factory (Hard)",
        "Hockey Ex: Beat Daisy Garden (Hard)",
        "Hockey Ex: Beat Bowser Jr. Blvd. (Hard)",
        "Hockey Ex: Beat Waluigi Pinball (Hard)",
        "Hockey Ex: Beat Star Ship (Hard)",
        "Hockey Ex: Beat Koopa Troopa Beach (Hard)",
        "Hockey Ex: Beat Ghoulish Galleon (Hard)",
        "Hockey Ex: Beat Bowser's Castle (Hard)"])
    h_exhibition_locations_ex = get_location_names_with_ids([
        "Hockey Ex: Beat Mario Stadium (Expert)",
        "Hockey Ex: Beat Toad Park (Expert)",
        "Hockey Ex: Beat Peach's Castle (Expert)",
        "Hockey Ex: Beat Western Junction (Expert)",
        "Hockey Ex: Beat Wario Factory (Expert)",
        "Hockey Ex: Beat Daisy Garden (Expert)",
        "Hockey Ex: Beat Bowser Jr. Blvd. (Expert)",
        "Hockey Ex: Beat Waluigi Pinball (Expert)",
        "Hockey Ex: Beat Star Ship (Expert)",
        "Hockey Ex: Beat Koopa Troopa Beach (Expert)",
        "Hockey Ex: Beat Ghoulish Galleon (Expert)",
        "Hockey Ex: Beat Bowser's Castle (Expert)"])
    h_exhibition_e.add_locations(h_exhibition_locations_e)
    h_exhibition_n.add_locations(h_exhibition_locations_n)
    h_exhibition_h.add_locations(h_exhibition_locations_h)
    h_exhibition_ex.add_locations(h_exhibition_locations_ex)


def create_events(world: "MSMWorld") -> None:
    if world.options.goal_condition == GoalCondition.option_defeat_behemoth:
        world.get_region("Behemoth Boss Battle").add_event(
            "Defeated Behemoth!", "Victory", location_type=MSMLocation, item_type=items.MSMItem
        )

    if world.options.goal_condition == GoalCondition.option_defeat_behemoth_king:
        # This is causing issues I don't like you
        # normal_behemoth_loc = get_location_names_with_ids(["Defeated Behemoth!"])
        # behemoth_boss = world.get_region("Behemoth Boss Battle")
        # behemoth_boss.add_locations(normal_behemoth_loc, MSMLocation)
        world.get_region("Behemoth King Boss Battle").add_event(
            "Defeated Behemoth King!", "Victory", location_type=MSMLocation,
            item_type=items.MSMItem)

    if world.options.goal_condition == GoalCondition.option_win_cups:
        world.get_region("Main Menu").add_event(f"Win {world.options.cups_required.value} Cups!",
                                                "Victory", location_type=MSMLocation, item_type=items.MSMItem)
