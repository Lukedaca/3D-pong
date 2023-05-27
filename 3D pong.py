import pygame
from pygame.locals import *
import random
import sys

# Inicializace knihovny Pygame
pygame.init()

# Nastavení velikosti okna
screen = pygame.display.set_mode((800, 600))

# Nastavení barvy
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
# Nastavení počátečního skóre
player_score = 0
computer_score = 0

# Nastavení počáteční pozice míčku
ball_pos = [400, 300]

# Nastavení počáteční rychlosti míčku
ball_vel = [2, 2]

# Nastavení počáteční pozice pálky
player_paddle_pos = [375, 580]
computer_paddle_pos = [375, 20]

# Nastavení stavu pauzy
paused = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_p:  # Pokud hráč stiskne 'p', hra se pauzuje / pokračuje
                paused = not paused
    if not paused:
        # Aktualizace pozice míčku
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

        # Kontrola, zda míček narazil na stěnu
        if ball_pos[0] <= 0 or ball_pos[0] >= 790:
            ball_vel[0] = -ball_vel[0]
        if ball_pos[1] <= 20:
            ball_vel[1] = -ball_vel[1]
            player_score += 1  # Hráč získává bod, pokud míček narazí na horní okraj
        if ball_pos[1] >= 580:
            ball_vel[1] = -ball_vel[1]
            computer_score += 1  # Počítač získává bod, pokud míček narazí na dolní okraj

        # Kontrola, zda míček narazil na pálečku
        if 570 <= ball_pos[1] <= 580 and player_paddle_pos[0] <= ball_pos[0] <= player_paddle_pos[0] + 50:
            ball_vel[1] = -ball_vel[1]
        if 20 <= ball_pos[1] <= 30 and computer_paddle_pos[0] <= ball_pos[0] <= computer_paddle_pos[0] + 50:
            ball_vel[1]# Assistant will continue from the previous message
            ball_vel[1] = -ball_vel[1]

        # Omezení pohybu páleček
        if player_paddle_pos[0] <= 0:
            player_paddle_pos[0] = 0
        if player_paddle_pos[0] >= 750:
            player_paddle_pos[0] = 750
        if computer_paddle_pos[0] <= 0:
            computer_paddle_pos[0] = 0
        if computer_paddle_pos[0] >= 750:
            computer_paddle_pos[0] = 750
        # Počítačová pálečka následuje míček s určitou chybovostí
        if ball_pos[0] > computer_paddle_pos[0] + 25 and random.random() < 0.95:
            computer_paddle_pos[0] += 2
        if ball_pos[0] < computer_paddle_pos[0] + 25 and random.random() < 0.95:
            computer_paddle_pos[0] -= 2

        # Hráč ovládá pálečku pomocí klávesnice
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            player_paddle_pos[0] -= 2
        if keys[K_RIGHT]:
            player_paddle_pos[0] += 2

        # Vykreslení herních prvků
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, pygame.Rect(ball_pos[0], ball_pos[1], 10, 10))
        pygame.draw.rect(screen, RED, pygame.Rect(player_paddle_pos[0], player_paddle_pos[1], 50, 10))
        pygame.draw.rect(screen, RED, pygame.Rect(computer_paddle_pos[0], computer_paddle_pos[1], 50, 10))

        # Vykreslení skóre
        font = pygame.font.Font(None, 36)
        score_text = font.render("Player1: " + str(player_score) + " : " + str(computer_score) + " Computer", 1, WHITE)
        screen.blit(score_text, (20, 280))

        # Aktualizace obrazovky
        pygame.display.flip()
        pygame.time.delay(10)
