import pygame
###########################################################
# 기본 초기화 (필수)
pygame.init()

# 화면 크기
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption("PBJ Balls")

# FPS
clock = pygame.time.Clock()
###########################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경 이미지 불러오기
background = pygame.image.load("Python\pygame_basic\background.png")


# 캐릭터 불러오기
character = pygame.image.load("C:/Python/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지크기
character_width = character_size[0] # 캐릭터 가로크기
character_height = character_size[1] # 캐릭터 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 1/2 크기에 위치
character_y_pos = screen_height - character_height # 화면 세로의+가장 아래에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 enemy 캐릭터
enemy = pygame.image.load("C:/Python/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size # 이미지 크기
enemy_width = enemy_size[0] # 캐릭터 가로크기
enemy_height = enemy_size[1] # 캐릭터 세로크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 가로의 1/2 크기에 위치
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # 화면 세로의+가장 아래에 위치


# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 20

# 시작 시간
start_ticks = pygame.time.get_ticks() # 현재 tick을 받아옴

# 이벤트 루프
running = True # 게임진행중?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정

# 캐릭터가 100만큼 이동해야함
# 10 fps : 1초 동안 10번 동작 -> 한번에 10만큼 이동
# 20 fps : 1초 동안 20번 동작     

    print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get(): #이벤트 발생체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생?
            running = False # 게임진행x

        if event.type == pygame.KEYDOWN: # 키 눌렀는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터 왼쪽이동
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터 오른쪽이동
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터 위쪽이동
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터 아래쪽이동
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0      

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
   
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width       
        
    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height    


    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
    
    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    # 타이머 집어넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10,10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update() # 게임화면 다시 그리기

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기(ms)           

# pygame 종료
pygame.quit()