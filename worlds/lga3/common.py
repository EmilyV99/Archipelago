from enum import StrEnum

base_number_id = 100000
gamename = 'ZQC LGA3 Remastered'
game_disp_name = 'Link\'s Grand Adventure 3: Remastered'

class RID(StrEnum):
    MENU = 'Menu'
    GRASSLAND = 'Grassland'
    KAKARIKO = 'Kakariko'
    MOUNTAIN = 'Mountain'
    DESERT = 'Desert'
    GRAVEYARD = 'Graveyard'
    ICE = 'Ice'
    LEVEL_1 = 'Level 1'
    LEVEL_1_R = 'Level 1 Right' #post-key
    LEVEL_1_B = 'Level 1 Boss' #post-bkey
    LEVEL_2 = 'Level 2'
    LEVEL_2_B = 'Level 2 Boss' #post-bkey
    LEVEL_3_F = 'Level 3 Front' #pre-jump
    LEVEL_3 = 'Level 3'
    LEVEL_3_R = 'Level 3 Right' #post-key
    LEVEL_3_R2 = 'Level 3 Right 2' #post-hookshot
    LEVEL_3_B = 'Level 3 Boss' #post-bkey
    LEVEL_4_F = 'Level 4 Front' #pre-jump2
    LEVEL_4 = 'Level 4'
    LEVEL_5 = 'Level 5'
    LEVEL_5_U = 'Level 5 Upper' #post-key
    LEVEL_5_B = 'Level 5 Boss' #post-bkey
    LEVEL_6_1F_F = 'Level 6 1F Front' #pre-wand check
    LEVEL_6_1F_B = 'Level 6 1F Back' #post-wand check
    LEVEL_6_1F_L = 'Level 6 1F Left' #post-wand check, OR from 2F Front + melee
    LEVEL_6_2F_F = 'Level 6 2F Front' #post-1-key + wpn
    LEVEL_6_2F_B = 'Level 6 2F Back' #post-2-key + melee
    LEVEL_6_B = 'Level 6 Boss' #post-bkey
    LEVEL_7 = 'Level 7'
    LEVEL_8 = 'Level 8'
    LEVEL_9 = 'Level 9'


