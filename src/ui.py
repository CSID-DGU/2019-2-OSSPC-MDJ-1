import pygame
from pygame.locals import *

pygame.init()

class ui_variables:
    # Fonts
    font_path = "../assets/fonts/OpenSans-Light.ttf"
    font_path_b = "../assets/fonts/OpenSans-Bold.ttf"
    font_path_i = "../assets/fonts/Inconsolata/Inconsolata.otf"
    # 폰트 추가
    font_path_DOSGothic = "../assets/fonts/DOSGothic.ttf"
    font_path_DOSSaemmul = "../assets/fonts/DOSSaemmul.ttf"
    font_path_DGM = "../assets/fonts/DungGeunMo.ttf"


    h1 = pygame.font.Font(font_path, 50)
    h2 = pygame.font.Font(font_path, 30)
    h4 = pygame.font.Font(font_path, 20)
    h5 = pygame.font.Font(font_path, 13)
    h6 = pygame.font.Font(font_path, 10)

    h1_b = pygame.font.Font(font_path_b, 50)
    h2_b = pygame.font.Font(font_path_b, 30)
    h3_b = pygame.font.Font(font_path_b, 35)

    h2_i = pygame.font.Font(font_path_i, 30)
    h3_i = pygame.font.Font(font_path_i, 24)
    h5_i = pygame.font.Font(font_path_i, 13)

    #새 폰트
    DG80 = pygame.font.Font(font_path_DGM, 80)
    DG20 = pygame.font.Font(font_path_DGM, 20)
    DGM23 = pygame.font.Font(font_path_DGM, 23)
    DGM13 = pygame.font.Font(font_path_DGM, 13)


    # Sounds
    click_sound = pygame.mixer.Sound("../assets/sounds/SFX_ButtonUp.wav")
    move_sound = pygame.mixer.Sound("../assets/sounds/SFX_PieceMoveLR.wav")
    drop_sound = pygame.mixer.Sound("../assets/sounds/SFX_PieceHardDrop.wav")
    single_sound = pygame.mixer.Sound("../assets/sounds/SFX_SpecialLineClearSingle.wav")
    double_sound = pygame.mixer.Sound("../assets/sounds/SFX_SpecialLineClearDouble.wav")
    triple_sound = pygame.mixer.Sound("../assets/sounds/SFX_SpecialLineClearTriple.wav")
    tetris_sound = pygame.mixer.Sound("../assets/sounds/SFX_SpecialTetris.wav")

    # Background colors
    black = (0,0,0) #rgb(10, 10, 10)
    white = (255, 255, 255) #rgb(255, 255, 255)
    grey_1 = (26, 26, 26) #rgb(26, 26, 26)
    grey_2 = (35, 35, 35) #rgb(35, 35, 35)
    grey_3 = (55, 55, 55) #rgb(55, 55, 55)

    # Tetrimino colors
    cyan = (69, 206, 204) #rgb(69, 206, 204) # I
    blue = (64, 111, 249) #rgb(64, 111, 249) # J
    orange = (253, 189, 53) #rgb(253, 189, 53) # L
    yellow = (246, 227, 90) #rgb(246, 227, 90) # O
    green = (98, 190, 68) #rgb(98, 190, 68) # S
    pink = (242, 64, 235) #rgb(242, 64, 235) # T
    red = (225, 13, 27) #rgb(225, 13, 27) # Z

    t_color = [grey_2, cyan, blue, orange, yellow, green, pink, red, grey_3]
