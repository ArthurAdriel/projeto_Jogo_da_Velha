import pygame

pygame.init()

largura, altura = 600, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Velha')

branco = (255, 255, 255)
preto = (0, 0, 0)

tela.fill((branco))

pygame.draw.line(tela, preto, (200, 0), (200, 600), 5)
pygame.draw.line(tela, preto, (400, 0), (400, 600), 5)
pygame.draw.line(tela, preto, (0, 200), (600, 200), 5)
pygame.draw.line(tela, preto, (0, 400), (600, 400), 5)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.quit():
            rodando = False

pygame.quit()
