import pygame

pygame.init()

largura, altura = 600, 600
cont = 0
rodar_jogo = False

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Velha')

branco = (255, 255, 255)
preto = (0, 0, 0)

tela.fill((branco))

pygame.draw.rect(tela, preto, (200, 250, 200, 100), 0)

fonte_botao = pygame.font.SysFont('Open Sans', 30)
msg_botao = fonte_botao.render('Iniciar o Jogo', True, branco)
tela.blit(msg_botao, (232, 292))

fonte_titulo = pygame.font.SysFont('Open Sans', 70)
titulo = fonte_titulo.render('Jogo da Velha', True, preto)
tela.blit(titulo, (130, 50))

def desenhar_grade():
    tela.fill((branco))
    pygame.draw.line(tela, preto, (200, 0), (200, 600), 5)
    pygame.draw.line(tela, preto, (400, 0), (400, 600), 5)
    pygame.draw.line(tela, preto, (0, 200), (600, 200), 5)
    pygame.draw.line(tela, preto, (0, 400), (600, 400), 5)

def desenhar_x(linha, coluna):
    x = coluna * 200
    y = linha * 200
    margem = 30
    pygame.draw.line(tela, preto, (x+margem, y+margem), (x+200-margem, y+200-margem), 10)
    pygame.draw.line(tela, preto, (x+200-margem, y+margem), (x+margem, y+200-margem), 10)

def desenhar_o(linha, coluna):
    x = coluna * 200 + 100
    y = linha * 200 + 100
    raio = 70
    pygame.draw.circle(tela, preto, (x, y), raio, 10)
    pygame.draw.circle(tela, preto, (x, y), raio, 10)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos

            if rodar_jogo == False:
                if x > 200 and x < 400 and y > 250 and y < 350:
                    rodar_jogo = True
                    desenhar_grade()
            else:
                coluna = x // 200
                linha = y // 200

                if cont % 2 == 0:
                    desenhar_o(linha, coluna)
                else:
                    desenhar_x(linha, coluna)
                            
                cont += 1

    pygame.display.update()

pygame.quit()
print(cont)