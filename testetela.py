import pygame
#José Augusto, Leticia e Mateus
#Inicialização de modulos
pygame.init()
def telaGameOver(situacao):
    #Cores
    preto=(0,0,0)
    branco=(255,255,255)
    vermelho=(255,0,0)
    verde=(0,255,0)
    azul=(0,0,255)

    #Criando janela
    largura=900
    altura=600
    janela=pygame.display.set_mode((largura, altura))  # Tamanho fixo 900x600

    #Título da janela
    pygame.display.set_caption("Resultado")

    #Configurações Circulo
    raio=8
    velocidadey=8

    #distancia entre os circulos
    distancia= 50

    #qtds circulo cabem na janela
    qtdCirc=largura//distancia
    circulos=[]

    # Inicializando posições e velocidades dos círculos
    for i in range(qtdCirc):
        #calcula a posição x e y usando a distancia para que o circulo não se sobrepoem
        x=i*distancia 
        y=-i*distancia
        circulos.append([x, y])

    # Configuração da fonte
    fonte = pygame.font.SysFont(None, 74)

    aberto = True

    # Loop do jogo
    while aberto:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                aberto=False

        #Atualizando a posição circulo
        for circulo in circulos:
            #atualiza a posição de y fazendo se mover para baixo
            circulo[1]+=velocidadey 

            #Caso o circulo atingir o limite ele volta ao inicio/topo
            if circulo[1]-raio>altura:
                circulo[1]=-raio

        janela.fill(preto)
        largRet=largura* 0.9
        altRet=150

        #Calcular posição x e y do retangulo centralizado
        posxret=(largura-largRet)//2
        posyret=(altura-altRet)//2

        for circulo in circulos:
            #Desenha o circulo usando as posições guardadas
            pygame.draw.circle(janela, azul, (circulo[0], circulo[1]), raio)
        #Desenha o retangulo no meio da tela
        ret = pygame.Rect(posxret, posyret, largRet, altRet)
        pygame.draw.rect(janela, branco, ret,9)

        #Renderizando e desenhando o texto "LOSE" no meio do retângulo
        if situacao == "ganhou":
            texto = fonte.render("Você Ganhou", True, verde)
        else:
            texto = fonte.render("Você Perdeu", True, vermelho)

        #Obtém as dimensão das palavras
        largura_texto,altura_texto=texto.get_size()

        #Calcula x e y para centralizar texto dentro do retangulo
        posx_texto=posxret+(largRet-largura_texto)//2
        posy_texto=posyret+(altRet-altura_texto)//2
        janela.blit(texto,(posx_texto, posy_texto))

        #Atualizando a tela
        pygame.display.flip()

        #Controlando a taxa de atualização
        pygame.time.delay(30)

#Encerrando módulos
pygame.quit()
