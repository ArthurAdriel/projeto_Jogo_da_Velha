import pygame
import time

pygame.init()

largura, altura = 600, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Velha')

estado = 'menu'

branco = (255, 255, 255)
preto = (0, 0, 0)

fonte_botao = pygame.font.SysFont('Open Sans', 30)
fonte_titulo = pygame.font.SysFont('Open Sans', 70)

def desenhar_menu():
    tela.fill((branco))
    pygame.draw.rect(tela, preto, (200, 250, 200, 100), 0)
    msg_botao = fonte_botao.render('Iniciar o Jogo', True, branco)
    tela.blit(msg_botao, (232, 292))
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

def marcar_vencedor(tabuleiro):
    for c, linha in enumerate(tabuleiro):
        if linha[0] == linha[1] == linha[2] and linha[0] is not None:
            if c == 0:
                pygame.draw.line(tela, preto, (25, 100), (575, 100), 10)
            elif c == 1:
                pygame.draw.line(tela, preto, (25, 300), (575, 300), 10)
            elif c == 2:
                pygame.draw.line(tela, preto, (25, 500), (575, 500), 10)
            return linha[0]
    
    for c in range(3):
        if tabuleiro[0][c] == tabuleiro[1][c] == tabuleiro[2][c] and tabuleiro[0][c] is not None:
            if c == 0:
                pygame.draw.line(tela, preto, (100, 25), (100, 575), 10)
            elif c == 1:
                pygame.draw.line(tela, preto, (300, 25), (300, 575), 10)
            elif c == 2:
                pygame.draw.line(tela, preto, (500, 25), (500, 575), 10)
            return tabuleiro[0][c]
        
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] is not None:
        pygame.draw.line(tela, preto, (50, 50), (550, 550), 20)
        return tabuleiro[0][0]
    
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] is not None:
        pygame.draw.line(tela, preto, (50, 550), (550, 50), 20)
        return tabuleiro[0][2]
    
def tela_de_saida(vencedor):
    tela.fill((branco))
    if vencedor is not None:
        msg_vencedor = fonte_titulo.render(f'O jogador {vencedor} ganhou!', True, preto)
        tela.blit(msg_vencedor, (65, 50))
    else:
        msg_vencedor = fonte_titulo.render(f'O jogo deu velha!', True, preto)
        tela.blit(msg_vencedor, (85, 50))

    pygame.draw.rect(tela, preto, (200, 200, 200, 100), 0)
    pygame.draw.rect(tela, preto, (200, 400, 200, 100), 0)
    msg_reinicio = fonte_botao.render('Jogar denovo', True, branco)
    msg_sair = fonte_botao.render('Sair', True, branco)
    tela.blit(msg_reinicio, (232, 240))
    tela.blit(msg_sair, (280, 440))

desenhar_menu()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            
            if estado == 'menu':
                if x > 200 and x < 400 and y > 250 and y < 350:
                    estado = 'jogando'
                    cont = 0
                    vencedor = None
                    tabuleiro = [[None for _ in range(3)] for _ in range(3)]
                    desenhar_grade()
            elif estado == 'jogando':
                coluna = x // 200
                linha = y // 200
                if tabuleiro[linha][coluna] is None:
                    if cont % 2 == 0:
                        desenhar_o(linha, coluna)
                        tabuleiro[linha][coluna] = 'O'
                    else:
                        desenhar_x(linha, coluna)
                        tabuleiro[linha][coluna] = 'X'
                    cont += 1            
                    
                    vencedor = marcar_vencedor(tabuleiro)
                    if vencedor is not None or cont == 9:
                        estado = 'fim'
                        tempo_fim = time.time()

            elif estado == 'opcoes':
                tela_de_saida(vencedor)
                if x > 200 and x < 400 and y > 200 and y < 300:
                    estado = 'menu'
                    desenhar_menu()
                if x > 200 and x < 400 and y > 400 and y < 500:
                    rodando = False
    if estado == 'fim':
        if time.time() - tempo_fim >= 2:
            estado = 'opcoes'
            tela_de_saida(vencedor)

    pygame.display.update()

pygame.quit()
