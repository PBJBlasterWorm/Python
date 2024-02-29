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

#이벤트 루프
running = True # 게임진행중?
while running:
    for event in pygame.event.get(): #이벤트 발생체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생?
            running = False # 게임진행x
    #screen.fill((0, 0, 255))
    screen.blit(background, (0, 0)) #배경 그리기

    pygame.display.update() # 게임화면 다시 그리기       

# pygame 종료
pygame.quit()