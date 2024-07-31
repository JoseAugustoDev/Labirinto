import pygame

pygame.init()

TILE_SIZE = 64

WIDTH = TILE_SIZE * 10
HEIGHT = TILE_SIZE * 10

circulo_x = WIDTH / 20
circulo_y = HEIGHT / 20

labirinto = [[0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
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

rodando = True

clock = pygame.time.Clock()

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.fill((255, 255, 255))
    clock.tick(250)

    keys = pygame.key.get_pressed()

    novo_x, novo_y = circulo_x, circulo_y

    if (keys[pygame.K_a] and novo_x > 0) or (keys[pygame.K_LEFT] and novo_x > 0):
        novo_x -= 1
    if (keys[pygame.K_d] and novo_x < WIDTH) or (keys[pygame.K_RIGHT] and novo_x < WIDTH):
        novo_x += 1
    if (keys[pygame.K_w] and novo_y > 0) or (keys[pygame.K_UP] and novo_y > 0):
        novo_y -= 1
    if (keys[pygame.K_s] and novo_y < HEIGHT) or (keys[pygame.K_DOWN] and novo_y < HEIGHT):
        novo_y += 1

    linha = int(novo_x // TILE_SIZE)
    coluna = int(novo_y // TILE_SIZE)

    if 0 <= linha < len(labirinto[0]) and 0 <= coluna < len(labirinto):

        if labirinto[coluna][linha] != 1:
            circulo_x, circulo_y = novo_x, novo_y

    tela.fill((0, 0, 0))

    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            pos_x = j * TILE_SIZE
            pos_y = i * TILE_SIZE

            quadrado = pygame.Rect((pos_x, pos_y), (TILE_SIZE, TILE_SIZE))

            if labirinto[i][j] == 0:
                pygame.draw.rect(tela, (255, 255, 255), quadrado, TILE_SIZE)

            elif labirinto[i][j] == 1:
                pygame.draw.rect(tela, (0, 0, 0), quadrado, TILE_SIZE)

    pygame.draw.circle(tela, (255, 0, 0), (circulo_x, circulo_y), 10)

    pygame.display.flip()

