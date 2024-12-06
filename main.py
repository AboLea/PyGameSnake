import pygame
import pygame_menu
import random
import pickle

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

start = True

def start_menu():
    pygame.display.set_caption("Main menu")
    while True:
        screen.fill("black")

def main():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        if start:
            start_menu()



        pygame.display.update()
        clock.tick(60)



if __name__ == "__main__":
    main()