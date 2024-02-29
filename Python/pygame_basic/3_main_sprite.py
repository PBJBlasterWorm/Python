import pygame

pygame.init() #초기화

#화면 크기
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption("balls") #게임 이름

#배경 이미지 불러오기
background = pygame.image.load("C:/Python/pygame_basic/background.png")


# 캐릭터 불러오기
character = pygame.image.load("C:/Python/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지크기
character_width = character_size[0] # 캐릭터 가로크기
character_height = character_size[0] # 캐릭터 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 1/2 크기에 위치
character_y_pos = screen_height - character_height # 화면 세로의+가장 아래에 위치

#이벤트 루프
running = True # 게임진행중?
while running:
    for event in pygame.event.get(): #이벤트 발생체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생?
            running = False # 게임진행x
    #screen.fill((0, 0, 255))
    screen.blit(background, (0, 0)) #배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기

    pygame.display.update() # 게임화면 다시 그리기       

# pygame 종료
pygame.quit()