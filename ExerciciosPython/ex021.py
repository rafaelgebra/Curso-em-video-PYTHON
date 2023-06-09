import pygame
pygame.init()
pygame.mixes.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()