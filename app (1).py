import pygame

pygame.init()

TILE_SIZE = 64

WIDTH = TILE_SIZE * 10
HEIGHT = TILE_SIZE * 10

circulo_x = 32
circulo_y = 32

labirinto =[[0, 0, 0, 1, 1, 0, 0, 0, 0, 1], 
            [0, 1, 1, 0, 1, 0, 1, 1, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0], 
            [0, 0, 0, 1, 1, 1, 1, 0, 1, 0], 
            [1, 1, 0, 0, 1, 1, 0, 0, 1, 1], 
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1], 
            [0, 1, 1, 0, 1, 1, 0, 1, 0, 1], 
            [0, 1, 0, 0, 1, 1, 0, 0, 0, 1], 
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 1]]

tela = pygame.display.set_mode([WIDTH, HEIGHT])

circulo = pygame.Rect((0, 0), (TILE_SIZE, TILE_SIZE))

colisao_x = []
colisao_y = []

clock = pygame.time.Clock()

rodando = True

def gerarLabirinto(labirinto):
    
    for i in range(len(labirinto)):
        for j in range(len(labirinto)):

            pos_x = j * TILE_SIZE
            pos_y = i * TILE_SIZE

            quadrado = pygame.Rect((pos_x, pos_y), (TILE_SIZE, TILE_SIZE))

            if labirinto[i][j] == 0:

                pygame.draw.rect(tela, (255, 255, 255), quadrado, TILE_SIZE)
            
            if labirinto[i][j] == 1:

                colisao_x.append(quadrado.top)
                colisao_y.append(quadrado.left)

                pygame.draw.rect(tela, (0, 0, 0), quadrado, TILE_SIZE)
                

while rodando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.fill((255, 255, 255))
    clock.tick(250)

    keys = pygame.key.get_pressed()

    gerarLabirinto(labirinto)

    if (keys[pygame.K_a] and circulo_x > 0) or (keys[pygame.K_LEFT] and circulo_x > 0):
        circulo_x -= 1
        
        if circulo_x in colisao_x and circulo_y in colisao_y:
            circulo_x += 1

    if (keys[pygame.K_d] and circulo_x < WIDTH) or (keys[pygame.K_RIGHT] and circulo_x < WIDTH):    
        circulo_x += 1

        if circulo_x in colisao_x and circulo_y in colisao_y:
            circulo_x -= 1

    if (keys[pygame.K_w] and circulo_y > 0) or (keys[pygame.K_UP] and circulo_y > 0):    
        circulo_y -= 1

        if circulo_y in colisao_y and circulo_x in colisao_x:
            circulo_y += 1

    if (keys[pygame.K_s] and circulo_y < HEIGHT) or (keys[pygame.K_DOWN] and circulo_y < HEIGHT):
        circulo_y += 1

        if circulo_y in colisao_y and circulo_x in colisao_x:
            circulo_y -= 1

    pygame.draw.circle(tela, (0, 0, 200), (circulo_x, circulo_y), 10.00, TILE_SIZE)  

    pygame.display.flip()