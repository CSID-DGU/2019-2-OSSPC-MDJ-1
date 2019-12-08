import pygame
from pygame.locals import *

pygame.init()

class ui_variables:
    # Fonts
    font_path_DOSGothic = "../assets/fonts/DOSGothic.ttf"
    font_path_DOSSaemmul = "../assets/fonts/DOSSaemmul.ttf"
    font_path_DGM = "../assets/fonts/DungGeunMo.ttf"

    #새 폰트
    DG_big = pygame.font.Font(font_path_DGM, 100)
    DG_70 = pygame.font.Font(font_path_DGM, 70)
    DG_v_small = pygame.font.Font(font_path_DGM, 25)
    DG_small = pygame.font.Font(font_path_DGM, 30)

    DGM23 = pygame.font.Font(font_path_DGM, 23)
    DGM13 = pygame.font.Font(font_path_DGM, 13)
    DGM40 = pygame.font.Font(font_path_DGM, 40)


    # Background colors
    black = (0,0,0) #rgb(10, 10, 10)
    black_t = (0, 0, 0, 127) #transparent black
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
